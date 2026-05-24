+++
date = '2025-07-01T22:09:21+07:00'
draft = false
title = 'Tip Move Repo Gitlab Github'
author = []
description = "Mirror a repository from GitLab to GitHub while preserving full commit history, branches, and tags."
slug = "tip-move-repo-gitlab-github"
summary = "How to move a repo from GitLab to GitHub (or vice versa) and keep all history, branches, and tags with just a few bash commands."
tags = ["git", "github", "gitlab", "mirror", "tip"]
+++


Want to move a repo from GitLab to GitHub and keep **all commits, branches, and tags**? Here's a super simple way 👇

```bash
#!/bin/bash

# Replace these with your info
GITLAB_REPO="https://gitlab.com/yourname/your-repo.git"
GITHUB_REPO="https://github.com/yourname/your-repo.git"

# Clone from GitLab
git clone --mirror "$GITLAB_REPO"
cd your-repo.git

# Push to GitHub (with all history + branches + tags)
git remote set-url origin "$GITHUB_REPO"
git push --mirror

# Done!
echo "✅ Repo migrated from GitLab to GitHub!"
