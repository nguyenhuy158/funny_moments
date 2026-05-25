# Content Checklist

Use this checklist before publishing a new post or updating an existing one.

## Frontmatter

- `title` is specific and readable.
- `description` is one sentence and not a placeholder.
- `slug` is stable and unique for the target language.
- `tags` and `categories` are intentional, not empty by accident.
- `images` points to existing assets when Open Graph coverage matters.

## Content

- English and Vietnamese versions are both created when the topic should be bilingual.
- Internal links point to real pages.
- External links are still reachable.
- Code blocks and commands were copied exactly.
- Search/title/summary still make sense out of context.

## Validation

- `python3 scripts/lint_content.py`
- `hugo --buildDrafts=false --buildFuture=false --gc --minify --baseURL "https://huyab.click"`
- `python3 scripts/check_public.py public`
- `python3 scripts/check_links.py public`

## Production

- Push to `main`
- Confirm GitHub Actions CI is green
- Run production smoke check or wait for the automated smoke workflow
