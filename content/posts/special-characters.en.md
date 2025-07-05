+++
date = "2025-07-02T16:53:20+07:00"
draft = false
title = "Special Characters"
description = ""
slug = ""
authors = [ ]
tags = [ ]
categories = [ ]
externalLink = ""
series = [ ]
fmContentType = "default"
+++


When writing a blog, you might need to use characters like `>`, `<`, `<=`, `>=`, `&`.

## To avoid display errors, change them like this:

- `>` → `>`
- `<` → `<`
- `<=` → `<=`
- `>=` → `>=`
- `&` → `&`

## For example, the code displays correctly:

```html
if (a <= b && b >= c) {
  return true;
}