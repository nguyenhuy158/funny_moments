+++
date = "2025-08-28T16:57:25+07:00"
draft = false
title = 'Kind Trick'
description = "Small notes and commands for working more effectively with kind and related tooling."
summary = "Small notes and commands for working more effectively with kind and related tooling."
slug = "kind-trick"
authors = [ ]
tags = [ "ebook", "tool", "pdf" ]
categories = [ ]
externalLink = ""
series = [ ]
images = [ ]
+++

## Convert

- [k2pdfopt](https://www.willus.com/k2pdfopt/) converts PDF to a more readable PDF with margin crop and reflow.
- [pdf2epub](https://github.com/overcuriousity/pdf2epub) converts PDF to EPUB with AI support.
- [Translator](https://github.com/bookfere/Ebook-Translator-Calibre-Plugin) translates ebooks through a Calibre plugin.

### k2pdfopt

```bash
k2pdfopt -dev kpw -dpi 300 -mode fitwidth -as -ui- -o out.pdf input.pdf
```

### pdf2epub

```bash
python main.py filename.pdf
```
