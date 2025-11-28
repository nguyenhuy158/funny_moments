# AGENTS.md - Development Guidelines for Funny Moments Blog

## Build Commands
- **Development server**: `hugo server --disableFastRender --noHTTPCache --ignoreCache`
- **Production build**: `hugo --buildDrafts=false --buildFuture=false --minify`
- **New post**: `make new POST=post-name` or `hugo new posts/post-name.md`

## Testing & Quality
- **No automated tests** - Manual content review required
- **Build validation**: Run production build to check for Hugo errors
- **Content validation**: Check frontmatter syntax and markdown formatting

## Code Style Guidelines
- **Content**: Markdown with Hugo frontmatter (TOML format)
- **Frontmatter fields**: title, date, description, slug, tags, categories, draft
- **Naming**: Kebab-case for slugs and filenames (e.g., `hello-world.en.md`)
- **Language support**: Bilingual content (en/vi) - use `.en.md`/`.vi.md` suffixes for translations, `.md` for single-language posts
- **Imports**: No code imports - pure content site
- **Error handling**: Hugo build errors indicate syntax issues

## Development Workflow
- **Spec-driven development**: Use `.specify/` scripts for feature planning
- **Content creation**: Follow Hugo archetypes in `archetypes/default.md`
- **Git workflow**: Feature branches with PR reviews
- **Deployment**: Automated via Jenkins/GitHub Pages on main branch

## File Structure
- `content/posts/`: Blog posts with frontmatter
- `themes/papermod/`: Hugo theme (submodule)
- `static/`: Static assets (images, etc.)
- `layouts/`: Custom Hugo templates
- `.specify/`: Development workflow tools</content>
<parameter name="filePath">AGENTS.md