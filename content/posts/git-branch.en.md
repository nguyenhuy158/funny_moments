+++
date = "2025-07-11T14:44:47+07:00"
draft = false
title = 'Git Branch'
description = "Common Git branch commands for creating, deleting, and cleaning up branches."
summary = "Common Git branch commands for creating, deleting, and cleaning up branches."
slug = "git-branch"
authors = [ ]
tags = [ ]
categories = [ ]
externalLink = ""
series = [ ]
images = [ ]
+++

## Create branch
```
git checkout -b branch_name
```

## Delete branch
```
git checkout other_branch
git branch -D branch_name
git push origin --delete branch_name
```
