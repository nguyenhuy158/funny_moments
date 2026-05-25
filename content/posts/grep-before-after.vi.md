+++
date = "2025-07-22T08:53:02+07:00"
draft = false
title = 'Grep Before After'
description = "Ví dụ dùng các cờ context của grep để hiển thị thêm dòng trước và sau kết quả khớp."
summary = "Ví dụ dùng các cờ context của grep để hiển thị thêm dòng trước và sau kết quả khớp."
slug = "grep-before-after"
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
