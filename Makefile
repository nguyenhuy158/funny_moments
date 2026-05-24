.PHONY: new post commit content-lint ci

HUGO ?= $(shell command -v hugo 2>/dev/null || printf '%s' /opt/homebrew/bin/hugo)
BASE_URL ?= $(shell if [ -f CNAME ]; then printf 'https://%s' "$$(tr -d '\n' < CNAME)"; else printf '/'; fi)
HUGO_CACHE_DIR ?= $(CURDIR)/.hugo_cache

# Create a new post
new:
	@if [ -z "$(POST)" ]; then \
		echo "Usage: make new POST=post-name"; \
		exit 1; \
	fi
	hugo new posts/$(POST).md

# Commit and push the new post
post:
	@if [ -z "$(POST)" ]; then \
		echo "Usage: make post POST=post-name"; \
		exit 1; \
	fi
	git add content/posts/$(POST).md
	git commit -m "Add new post: $(POST)"
	git push origin main

# General commit (for other changes)
commit:
	@if [ -z "$(MSG)" ]; then \
		echo "Usage: make commit MSG='commit message'"; \
		exit 1; \
	fi
	git add .
	git commit -m "$(MSG)"
	git push origin main

# Validate content metadata and site placeholders
content-lint:
	python3 scripts/lint_content.py

# Run the same Hugo build check used by CI
ci:
	@if [ ! -x "$(HUGO)" ]; then \
		echo "Hugo not found. Set HUGO=/path/to/hugo"; \
		exit 1; \
	fi
	$(MAKE) content-lint
	HUGO_CACHEDIR="$(HUGO_CACHE_DIR)" "$(HUGO)" \
		--buildDrafts=false \
		--buildFuture=false \
		--gc \
		--minify \
		--baseURL "$(BASE_URL)"
