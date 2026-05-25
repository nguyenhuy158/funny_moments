+++
date = "2025-08-28T16:57:25+07:00"
draft = false
title = 'Kind Trick'
description = "Một vài ghi chú và lệnh nhỏ để làm việc hiệu quả hơn với ebook và các công cụ liên quan."
summary = "Một vài ghi chú và lệnh nhỏ để làm việc hiệu quả hơn với ebook và các công cụ liên quan."
slug = "kind-trick"
authors = [ ]
tags = [ "ebook", "tool", "pdf" ]
categories = [ ]
externalLink = ""
series = [ ]
images = [ ]
+++

## Chuyển đổi

- [k2pdfopt](https://www.willus.com/k2pdfopt/) dùng để tối ưu PDF dễ đọc hơn bằng cách cắt lề và reflow.
- [pdf2epub](https://github.com/overcuriousity/pdf2epub) chuyển PDF sang EPUB với hỗ trợ AI.
- [Translator](https://github.com/bookfere/Ebook-Translator-Calibre-Plugin) là plugin Calibre để dịch ebook.

### k2pdfopt

```bash
k2pdfopt -dev kpw -dpi 300 -mode fitwidth -as -ui- -o out.pdf input.pdf
```

### pdf2epub

```bash
python main.py filename.pdf
```
