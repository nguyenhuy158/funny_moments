+++
date = "2025-07-15T15:59:19+07:00"
draft = false
title = 'Git Config'
description = "Quick notes on global and local Git configuration scopes and where they are stored."
slug = "git-config"
authors = [ ]
tags = [ ]
categories = [ ]
externalLink = "https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration"
series = [ ]
images = [ ]
+++

## Global

location store is `~/.gitconfig`

```bash
git config --global key value
```

## Local

location store is `.git/config`
```bash
git config --local key value
```
