.PHONY: new post commit

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
