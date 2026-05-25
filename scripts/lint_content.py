#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = ROOT / "content" / "posts"
CONTENT_DIR = ROOT / "content"
CONFIG_FILE = ROOT / "config.yaml"
SEARCH_FILES = [
    ROOT / "content" / "search.md",
    ROOT / "content" / "search.vi.md",
]
ARCHIVE_FILES = [
    ROOT / "content" / "archives.md",
    ROOT / "content" / "archives.vi.md",
]

PLACEHOLDERS = {
    "The Best Widgets on Earth": "config subtitle placeholder",
    "<link or path of image for opengraph, twitter-cards>": "Open Graph image placeholder",
    "XYZabc": "site verification placeholder",
    "Search demo site with full text fuzzy search ...": "search placeholder text",
    "Discover insights and updates in my first blog post. Join me on this exciting journey of sharing thoughts and experiences!": "generic placeholder description",
    "TODO: add a one-sentence description.": "draft description placeholder",
}


def load_toml_frontmatter(text: str) -> dict[str, str]:
    parts = text.split("+++", 2)
    if len(parts) != 3:
        raise ValueError("missing TOML frontmatter wrapped by +++")
    frontmatter = parts[1]
    data: dict[str, str] = {}
    for key in ("title", "description", "slug", "summary"):
        match = re.search(rf"^{key}\s*=\s*(['\"])(.*?)\1\s*$", frontmatter, re.MULTILINE)
        if match:
            data[key] = match.group(2)
    images_match = re.search(r"^images\s*=\s*\[(.*?)\]\s*$", frontmatter, re.MULTILINE | re.DOTALL)
    if images_match:
        image_values = [match[1] for match in re.findall(r"(['\"])(.*?)\1", images_match.group(1), re.DOTALL)]
        data["images"] = ",".join(image_values)
    cover_match = re.search(r"^image\s*=\s*(['\"])(.*?)\1\s*$", frontmatter, re.MULTILINE)
    if cover_match:
        data["image"] = cover_match.group(2)
    return data


def load_yaml_frontmatter(text: str) -> dict[str, str]:
    parts = text.split("---", 2)
    if len(parts) != 3:
        raise ValueError("missing YAML frontmatter wrapped by ---")
    frontmatter = parts[1]
    data: dict[str, str] = {}
    for key in ("title", "description", "slug", "summary"):
        match = re.search(rf"^{key}:\s*(['\"]?)(.*?)\1\s*$", frontmatter, re.MULTILINE)
        if match:
            data[key] = match.group(2)
    return data


def load_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if text.startswith("+++"):
        return load_toml_frontmatter(text)
    if text.startswith("---"):
        return load_yaml_frontmatter(text)
    raise ValueError("missing supported frontmatter")


def infer_language(path: Path) -> str:
    name = path.name
    if name.endswith(".en.md"):
        return "en"
    if name.endswith(".vi.md"):
        return "vi"
    return "default"


def validate_image_path(path: Path, image_path: str, errors: list[str]) -> None:
    if not image_path or "://" in image_path or image_path.startswith("data:"):
        return

    normalized = image_path.strip()
    if normalized.startswith("/"):
        candidate = ROOT / "static" / normalized.lstrip("/")
    else:
        candidate = path.parent / normalized

    if not candidate.exists():
        errors.append(
            f"{path.relative_to(ROOT)}: references missing image `{image_path}`"
        )


def validate_posts(errors: list[str]) -> None:
    seen_slugs: dict[tuple[str, str], Path] = {}
    post_variants: dict[str, set[str]] = {}

    for path in sorted(POSTS_DIR.glob("*.md")):
        try:
            frontmatter = load_frontmatter(path)
        except Exception as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
            continue

        for key in ("title", "description", "slug", "summary"):
            value = frontmatter.get(key)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{path.relative_to(ROOT)}: missing or empty `{key}`")

        slug = frontmatter.get("slug", "").strip()
        if slug:
            language = infer_language(path)
            slug_key = (language, slug)
            previous = seen_slugs.get(slug_key)
            if previous is not None:
                errors.append(
                    f"{path.relative_to(ROOT)}: duplicate slug `{slug}` for language `{language}`; already used by {previous.relative_to(ROOT)}"
                )
            else:
                seen_slugs[slug_key] = path

        images = frontmatter.get("images", "")
        if images:
            for image_path in [item.strip() for item in images.split(",") if item.strip()]:
                validate_image_path(path, image_path, errors)

        image = frontmatter.get("image", "").strip()
        if image:
            validate_image_path(path, image, errors)

        language = infer_language(path)
        if language == "default":
            errors.append(
                f"{path.relative_to(ROOT)}: post files must use `.en.md` or `.vi.md`, plain `.md` is not allowed"
            )
            continue

        base_name = path.name.rsplit(f".{language}.md", 1)[0]
        post_variants.setdefault(base_name, set()).add(language)

    for base_name, languages in sorted(post_variants.items()):
        if languages != {"en", "vi"}:
            missing = sorted({"en", "vi"} - languages)
            errors.append(
                f"content/posts/{base_name}: missing translation variant(s): {', '.join(missing)}"
            )


def validate_pages(errors: list[str]) -> None:
    for path in sorted(CONTENT_DIR.rglob("*.md")):
        if path.parent == POSTS_DIR:
            continue

        try:
            frontmatter = load_frontmatter(path)
        except Exception as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
            continue

        for key in ("title", "description", "summary"):
            value = frontmatter.get(key)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{path.relative_to(ROOT)}: missing or empty `{key}`")


def validate_placeholders(errors: list[str]) -> None:
    config_text = CONFIG_FILE.read_text(encoding="utf-8")
    for needle, label in PLACEHOLDERS.items():
        if needle in config_text:
            errors.append(f"{CONFIG_FILE.relative_to(ROOT)}: contains {label}")

    for path in SEARCH_FILES + ARCHIVE_FILES:
        text = path.read_text(encoding="utf-8")
        if "demo site" in text:
            errors.append(f"{path.relative_to(ROOT)}: contains placeholder search copy")


def main() -> int:
    errors: list[str] = []
    validate_posts(errors)
    validate_pages(errors)
    validate_placeholders(errors)

    if errors:
        print("Content lint failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Content lint passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
