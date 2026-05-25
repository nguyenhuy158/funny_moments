# AGENTS.md - Development Guidelines for Funny Moments Blog

## Build Commands
- **Development server**: `hugo server --disableFastRender --noHTTPCache --ignoreCache`
- **Production build**: `hugo --buildDrafts=false --buildFuture=false --minify`
- **New post**: `make new POST=post-name.en` and create the matching `*.vi.md` variant before merging

## Testing & Quality
- **Build validation**: Run `make ci` or at minimum the production Hugo build
- **Content validation**: `python3 scripts/lint_content.py`
- **Output validation**: `python3 scripts/check_public.py public`
- **Link validation**: `python3 scripts/check_links.py public`
- **Production smoke**: `python3 scripts/smoke_site.py --base-url "https://huyab.click"`

## Code Style Guidelines
- **Content**: Markdown with Hugo frontmatter (TOML format)
- **Frontmatter fields for posts**: title, date, description, summary, slug, tags, categories, draft
- **Frontmatter fields for pages**: title, description, summary
- **Naming**: Kebab-case for slugs and filenames (e.g., `hello-world.en.md`)
- **Language support**: All posts must be bilingual. Use `.en.md` and `.vi.md` pairs. Do not create single-language post files such as `post-name.md`.
- **Imports**: No code imports - pure content site
- **Error handling**: Hugo build errors indicate syntax issues

## Development Workflow
- **Spec-driven development**: Use `.specify/` scripts for feature planning
- **Content creation**: Follow Hugo archetypes in `archetypes/default.md`
- **Bilingual rule**: CI fails if a post is missing either the English or Vietnamese variant
- **Git workflow**: Feature branches with PR reviews
- **Deployment**: Automated via Jenkins/GitHub Pages on main branch
- **Release CI**: GitHub Actions release workflow runs on version tags and creates GitHub Releases
- **Release tag naming**: `vMAJOR.MINOR.PATCH` for stable releases, `vMAJOR.MINOR.PATCH-suffix` for pre-releases such as `v1.2.3-rc.1`

## File Structure
- `content/posts/`: Blog posts with frontmatter
- `themes/papermod/`: Hugo theme (submodule)
- `static/`: Static assets (images, etc.)
- `layouts/`: Custom Hugo templates
- `.specify/`: Development workflow tools</content>
<parameter name="filePath">AGENTS.md
