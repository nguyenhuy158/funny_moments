+++
date = '2025-07-04T11:05:43+07:00'
draft = false
title = 'Convert Html to Markdown'
description = "Một vài cách chuyển nội dung HTML sang Markdown để dễ chỉnh sửa và đăng bài hơn."
summary = "Một vài cách chuyển nội dung HTML sang Markdown để dễ chỉnh sửa và đăng bài hơn."
slug = "convert-html-to-markdown"
authors = []
tags = []
categories = []
externalLink = ''
series = []
+++

Trong một số tình huống như:

- Bạn đang lấy nội dung HTML từ email hoặc web
- Muốn dán nó lên Slack cho gọn gàng
- Hoặc muốn paste vô Hugo để viết blog mà không bị lỗi format

Thì Markdown là chuẩn nhất. Nhưng convert bằng tay thì mệt. Vậy thì...

## 🛠 Giải pháp: Dùng Python convert HTML → Markdown

Có 2 thư viện cực tiện:

### 1. `html2text` — dễ xài, cài 1 phát là chiến

```bash
pip install html2text
import html2text
html = "<b>Hello</b> <a href='https://example.com'>Click me</a>"
markdown = html2text.html2text(html)
print(markdown)
# **Hello** [Click me](https://example.com)
```
2. markdownify — xịn hơn, tùy chỉnh mạnh
```bash
pip install markdownify
from markdownify import markdownify as md
html = "<h1>Title</h1><p>This is <b>bold</b></p>"
markdown = md(html)
print(markdown)
# # Title
# This is **bold**
```

✨ Tại sao nên dùng?
Slack không hỗ trợ HTML ⇒ cần Markdown
Hugo viết bài cũng dùng Markdown
Làm việc nhanh hơn, đỡ sửa tay

## 🎯 Tip nhỏ
Dùng strip() sau khi convert để loại bỏ dòng trống: `md = html2text.html2text(html).strip()`
