+++
date = '2025-07-02T16:53:20+07:00'
draft = false
title = 'Special Characters'
description = ''
slug = ''
authors = []
tags = []
categories = []
externalLink = ''
series = []
+++


Khi viết blog, bạn có thể cần dùng các ký tự như `>`, `<`, `<=`, `>=`, `&`.

Để tránh lỗi hiển thị, hãy chuyển chúng như sau:

- `>` → `&gt;`
- `<` → `&lt;`
- `<=` → `&lt;=`
- `>=` → `&gt;=`
- `&` → `&amp;`

Ví dụ code hiển thị đúng:

```html
if (a &lt;= b &amp;&amp; b &gt;= c) {
  return true;
}
```