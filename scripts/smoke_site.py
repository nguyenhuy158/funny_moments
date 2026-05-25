#!/usr/bin/env python3

from __future__ import annotations

from dataclasses import dataclass
from time import sleep
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
import argparse
import sys


@dataclass(frozen=True)
class SmokeCase:
    path: str
    expected_status: int
    expected_text: str


SMOKE_CASES = [
    SmokeCase("/", 200, "Build, Break, Learn"),
    SmokeCase("/search/", 200, "Search"),
    SmokeCase("/notes/", 200, "Notes"),
    SmokeCase("/feeds/", 200, "Feeds"),
    SmokeCase("/tags/", 200, "Tags"),
    SmokeCase("/categories/", 200, "Categories"),
    SmokeCase("/archives/", 200, "Archive"),
    SmokeCase("/vi/", 200, "Build, Break, Learn"),
    SmokeCase("/vi/search/", 200, "Tìm kiếm"),
    SmokeCase("/vi/notes/", 200, "Ghi chú"),
    SmokeCase("/vi/feeds/", 200, "Nguồn cấp"),
    SmokeCase("/vi/tags/", 200, "Thẻ"),
    SmokeCase("/vi/categories/", 200, "Chuyên mục"),
    SmokeCase("/vi/archives/", 200, "Lưu trữ"),
    SmokeCase("/index.xml", 200, "<rss"),
    SmokeCase("/vi/index.xml", 200, "<rss"),
    SmokeCase("/sitemap.xml", 200, "<sitemap"),
    SmokeCase("/vi/sitemap.xml", 200, "<urlset"),
    SmokeCase("/this-path-should-not-exist-12345", 404, "404"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="https://huyab.click")
    parser.add_argument("--retries", type=int, default=1)
    parser.add_argument("--delay", type=int, default=10)
    parser.add_argument("--timeout", type=int, default=15)
    return parser.parse_args()


def fetch(url: str, timeout: int) -> tuple[int, str]:
    request = Request(url, headers={"User-Agent": "funny-moments-smoke/1.0"})
    try:
        with urlopen(request, timeout=timeout) as response:
            body = response.read().decode("utf-8", errors="replace")
            return response.getcode(), body
    except HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        return exc.code, body
    except URLError as exc:
        raise RuntimeError(f"{url}: {exc.reason}") from exc


def run_suite(base_url: str, timeout: int) -> list[str]:
    failures: list[str] = []

    for case in SMOKE_CASES:
        url = f"{base_url.rstrip('/')}{case.path}"
        try:
            status, body = fetch(url, timeout)
        except RuntimeError as exc:
            failures.append(str(exc))
            continue

        if status != case.expected_status:
            failures.append(f"{url}: expected HTTP {case.expected_status}, got {status}")
            continue

        if case.expected_text not in body:
            failures.append(f"{url}: missing expected text `{case.expected_text}`")

    return failures


def main() -> int:
    args = parse_args()

    for attempt in range(1, args.retries + 1):
        failures = run_suite(args.base_url, args.timeout)
        if not failures:
            print(f"Smoke check passed for {args.base_url}.")
            return 0

        if attempt < args.retries:
            print(f"Smoke attempt {attempt}/{args.retries} failed, retrying in {args.delay}s...")
            for failure in failures:
                print(f"- {failure}")
            sleep(args.delay)
            continue

        print(f"Smoke check failed for {args.base_url}:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    return 1


if __name__ == "__main__":
    sys.exit(main())
