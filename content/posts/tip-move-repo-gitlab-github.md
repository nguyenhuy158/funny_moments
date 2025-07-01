+++
date = '2025-07-01T22:09:21+07:00'
draft = true
title = 'Tip Move Repo Gitlab Github'
author = "nguyenhuy158"
summary = "Cách chuyển repo từ GitLab sang GitHub (hoặc ngược lại) mà giữ nguyên lịch sử, branch, tag chỉ với vài dòng lệnh bash."
tags = ["git", "github", "gitlab", "mirror", "tip"]
+++


Bạn muốn chuyển repo từ GitLab sang GitHub mà giữ **toàn bộ commit, branch và tag**? Đây là cách siêu gọn 👇

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
```