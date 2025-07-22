+++
date = "2025-07-22T08:52:58+07:00"
draft = false
title = 'Grep Before After'
description = ""
slug = ""
authors = [ ]
tags = [ ]
categories = [ ]
externalLink = ""
series = [ ]
images = [ ]
+++

```sh
grep --context 3 "search_pattern" path/to/file
grep --before-context 3 "search_pattern" path/to/file
grep --after-context 3 "search_pattern" path/to/file
```

```sh
grep -C 3 "search_pattern" path/to/file
grep -A 3 "search_pattern" path/to/file
grep -B 3 "search_pattern" path/to/file
```