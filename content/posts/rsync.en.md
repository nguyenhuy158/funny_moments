+++
date = "2025-07-15T11:01:19+07:00"
draft = false
title = 'Rsync'
description = "Useful rsync commands as a safer and more flexible alternative to plain cp."
slug = "rsync"
authors = [ ]
tags = [ ]
categories = [ ]
externalLink = ""
series = [ ]
images = [ ]
+++

## Alternative cp command [dry run]
```bash
rsync -hav --progress source dest --dry-run
```

## Alternative cp command
```bash
rsync -hav --progress source dest
```
