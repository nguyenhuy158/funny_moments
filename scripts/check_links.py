#!/usr/bin/env python3

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen
import argparse
import sys


SKIPPED_SCHEMES = ("mailto:", "tel:", "javascript:", "data:")
SKIPPED_STATUSES = {401, 403, 405}
INTERNAL_HOSTS = {"huyab.click", "www.huyab.click", "profile.huycode.workers.dev"}
SKIPPED_EXTERNAL_HOSTS = {"www.linkedin.com", "linkedin.com", "www.willus.com", "willus.com"}


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for key, value in attrs:
            if key in {"href", "src"} and value:
                self.links.append(value)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("public_dir", nargs="?", default="public")
    parser.add_argument("--external", action="store_true")
    parser.add_argument("--timeout", type=int, default=10)
    return parser.parse_args()


def html_path_to_url_path(root: Path, html_path: Path) -> str:
    relative = html_path.relative_to(root).as_posix()
    if relative == "index.html":
        return "/"
    if relative.endswith("/index.html"):
        return f"/{relative[:-10]}/"
    return f"/{relative}"


def collect_html_links(root: Path) -> tuple[list[str], dict[Path, list[str]]]:
    external_links: list[str] = []
    internal_errors: dict[Path, list[str]] = {}

    for html_path in sorted(root.rglob("*.html")):
        parser = LinkParser()
        if not html_path.exists():
            continue
        parser.feed(html_path.read_text(encoding="utf-8"))
        source_url = html_path_to_url_path(root, html_path)

        for raw_link in parser.links:
            if raw_link.startswith("#") or raw_link.startswith(SKIPPED_SCHEMES):
                continue
            if raw_link.startswith("/livereload.js"):
                continue

            is_absolute_link = raw_link.startswith(("http://", "https://", "//"))
            resolved = urlparse(urljoin(f"https://example.invalid{source_url}", raw_link))
            if is_absolute_link and resolved.scheme in {"http", "https"} and resolved.netloc and resolved.netloc not in INTERNAL_HOSTS:
                external_links.append(resolved.geturl())
                continue

            normalized_path = resolved.path or "/"
            target = resolve_internal_target(root, normalized_path)
            if target is None:
                internal_errors.setdefault(html_path, []).append(raw_link)

    return sorted(set(external_links)), internal_errors


def resolve_internal_target(root: Path, path: str) -> Path | None:
    if path == "/":
        candidate = root / "index.html"
        return candidate if candidate.exists() else None

    relative = path.lstrip("/")
    candidate = root / relative
    if candidate.exists():
        return candidate

    if path.endswith("/"):
        candidate = root / relative / "index.html"
        return candidate if candidate.exists() else None

    if Path(relative).suffix:
        return None

    html_candidate = root / f"{relative}.html"
    if html_candidate.exists():
        return html_candidate

    index_candidate = root / relative / "index.html"
    if index_candidate.exists():
        return index_candidate

    return None


def verify_external_link(url: str, timeout: int) -> str | None:
    parsed = urlparse(url)
    if parsed.netloc in SKIPPED_EXTERNAL_HOSTS:
        return None

    request = Request(url, method="HEAD", headers={"User-Agent": "funny-moments-link-check/1.0"})
    try:
        with urlopen(request, timeout=timeout):
            return None
    except HTTPError as exc:
        if exc.code == 405:
            return verify_external_link_with_get(url, timeout)
        if exc.code in SKIPPED_STATUSES:
            return None
        return f"{url} -> HTTP {exc.code}"
    except URLError as exc:
        return f"{url} -> {exc.reason}"


def verify_external_link_with_get(url: str, timeout: int) -> str | None:
    request = Request(url, method="GET", headers={"User-Agent": "funny-moments-link-check/1.0"})
    try:
        with urlopen(request, timeout=timeout):
            return None
    except HTTPError as exc:
        if exc.code in SKIPPED_STATUSES:
            return None
        return f"{url} -> HTTP {exc.code}"
    except URLError as exc:
        return f"{url} -> {exc.reason}"


def main() -> int:
    args = parse_args()
    root = Path(args.public_dir).resolve()

    if not root.exists():
        print(f"Public directory not found: {root}")
        return 1

    external_links, internal_errors = collect_html_links(root)

    if internal_errors:
        print("Internal link audit failed:")
        for html_path, links in internal_errors.items():
            for link in links:
                print(f"- {html_path.relative_to(root)} -> {link}")
        return 1

    if args.external:
        external_failures = []
        for url in external_links:
            failure = verify_external_link(url, args.timeout)
            if failure:
                external_failures.append(failure)

        if external_failures:
            print("External link audit failed:")
            for failure in external_failures:
                print(f"- {failure}")
            return 1

    print(f"Link audit passed for {root}.")
    if args.external:
        print(f"Checked {len(external_links)} external links.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
