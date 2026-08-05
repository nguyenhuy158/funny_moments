#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path
import sys


REQUIRED_PATHS = [
    "index.html",
    "404.html",
    "index.xml",
    "index.json",
    "about/index.html",
    "now/index.html",
    "uses/index.html",
    "notes/index.html",
    "feeds/index.html",
    "search/index.html",
    "tags/index.html",
    "categories/index.html",
    "vi/index.html",
    "vi/index.xml",
    "vi/about/index.html",
    "vi/now/index.html",
    "vi/uses/index.html",
    "vi/notes/index.html",
    "vi/feeds/index.html",
    "vi/search/index.html",
    "vi/tags/index.html",
    "vi/categories/index.html",
]


def check_path(root: Path, relative_path: str, errors: list[str]) -> None:
    candidate = root / relative_path
    if not candidate.exists():
        errors.append(f"missing expected output `{relative_path}`")


def check_html_contains(root: Path, relative_path: str, needles: list[str], errors: list[str]) -> None:
    candidate = root / relative_path
    if not candidate.exists():
        return

    text = candidate.read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text:
            errors.append(f"`{relative_path}` is missing `{needle}`")


def main() -> int:
    if len(sys.argv) > 2:
        print("Usage: check_public.py [public_dir]")
        return 2

    public_dir = Path(sys.argv[1] if len(sys.argv) == 2 else "public").resolve()
    errors: list[str] = []

    if not public_dir.exists():
        print(f"Build output directory does not exist: {public_dir}")
        return 1

    for relative_path in REQUIRED_PATHS:
        check_path(public_dir, relative_path, errors)

    check_html_contains(
        public_dir,
        "index.html",
        [
            "application/ld+json",
            "SearchAction",
            "rel=me",
            "https://profile.huyab.click/search/?q={search_term_string}",
        ],
        errors,
    )
    check_html_contains(
        public_dir,
        "vi/index.html",
        [
            "application/ld+json",
            "SearchAction",
            "rel=me",
            "https://profile.huyab.click/vi/search/?q={search_term_string}",
        ],
        errors,
    )
    check_html_contains(
        public_dir,
        "tags/index.html",
        ["Tags", "Explore posts by tag"],
        errors,
    )
    check_html_contains(
        public_dir,
        "categories/index.html",
        ["Categories", "Browse posts by topic"],
        errors,
    )
    check_html_contains(
        public_dir,
        "about/index.html",
        ["About", "technical notes"],
        errors,
    )
    check_html_contains(
        public_dir,
        "now/index.html",
        ["Current focus", "deployment reliability"],
        errors,
    )
    check_html_contains(
        public_dir,
        "uses/index.html",
        ["Tools I reach for most often", "GitHub Actions and Cloudflare"],
        errors,
    )
    check_html_contains(
        public_dir,
        "notes/index.html",
        ["Notes", "short-form notes"],
        errors,
    )
    check_html_contains(
        public_dir,
        "feeds/index.html",
        ["Feeds", "Main RSS feed", "Sitemap"],
        errors,
    )
    check_html_contains(
        public_dir,
        "search/index.html",
        ["Search", "assets/js/search.", "searchStatus", "search-result-snippet"],
        errors,
    )
    check_html_contains(
        public_dir,
        "vi/search/index.html",
        ["Tìm kiếm", "assets/js/search.", "searchStatus", "search-result-snippet"],
        errors,
    )
    check_html_contains(
        public_dir,
        "posts/tmux-cheatsheet/index.html",
        ["image/webp", "post-freshness", "lightbox_open"],
        errors,
    )
    check_html_contains(
        public_dir,
        "vi/notes/index.html",
        ["Ghi chú", "TIL"],
        errors,
    )
    check_html_contains(
        public_dir,
        "vi/feeds/index.html",
        ["Nguồn cấp", "RSS chính", "Sitemap"],
        errors,
    )
    check_html_contains(
        public_dir,
        "index.html",
        ["/notes/", "/feeds/", "/sitemap.xml"],
        errors,
    )

    if errors:
        print("Public output audit failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Public output audit passed for {public_dir}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
