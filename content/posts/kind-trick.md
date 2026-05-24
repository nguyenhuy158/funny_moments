+++
date = "2025-08-28T16:57:25+07:00"
draft = false
title = 'Kind Trick'
description = "Small notes and commands for working more effectively with kind and related tooling."
slug = "kind-trick"
authors = [ ]
tags = [ "app", "tools", "kindle" ]
categories = [ ]
externalLink = ""
series = [ ]
images = [ ]
+++

## Convert

- [k2pdfopt](https://www.willus.com/k2pdfopt/) : tool convert pdf to pdf (*crop margin, reflow, ..*).
- [pdf2epub](https://github.com/overcuriousity/pdf2epub) : pdf to epub (using ai model).
- [Translator](https://github.com/bookfere/Ebook-Translator-Calibre-Plugin) : tool translator ebook (plugin in calibre).

### k2pdfopt

```
k2pdfopt -dev kpw -dpi 300 -mode fitwidth -as -ui- -o out.pdf input.pdf
```

### pdf2epub

```
python main.py filename.pdf
```
