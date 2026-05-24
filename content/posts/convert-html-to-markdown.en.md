+++
date = '2025-07-04T11:05:43+07:00'
draft = false
title = 'Convert Html to Markdown'
description = "Simple ways to convert HTML content into Markdown for easier editing and publishing."
slug = "convert-html-to-markdown"
authors = []
tags = []
categories = []
externalLink = ''
series = []
+++

In some situations, such as:

- You are getting HTML content from email or the web
- Want to paste it into Slack neatly
- Or want to paste it into Hugo to write a blog without format errors

Then Markdown is the best standard. But converting by hand is tiring. So...

## 🛠 Solution: Use Python to convert HTML → Markdown

There are 2 extremely convenient libraries:

### 1. `html2text` — easy to use, install and you're ready to go

```bash
pip install html2text
import html2text
html = "<b>Hello</b> <a href='https://example.com'>Click me</a>"
markdown = html2text.html2text(html)
print(markdown)
# **Hello** [Click me](https://example.com)
```
2. markdownify — more advanced, highly customizable
```bash
pip install markdownify
from markdownify import markdownify as md
html = "<h1>Title</h1><p>This is <b>bold</b></p>"
markdown = md(html)
print(markdown)
# # Title
# This is **bold**
```

✨ Why use it?
Slack does not support HTML ⇒ Markdown is needed
Hugo also uses Markdown to write articles
Work faster, less manual editing

## 🎯 Small tip
Use strip() after converting to remove blank lines: `md = html2text.html2text(html).strip()`
