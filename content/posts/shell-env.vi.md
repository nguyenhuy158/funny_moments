+++
date = "2025-07-08T23:00:53+07:00"
draft = false
title = 'Shell Env'
description = "Best practice when writing shell scripts"
slug = ""
authors = []
tags = []
categories = []
externalLink = ""
series = []
images = []
+++

Nên sử dụng `/usr/bin/env` trong viết viết shell script.
Tránh hardcore shell path nên dùng environment.

# ✅ Nên dùng:

`#!/usr/bin/env bash`

# 🚫 Nên tránh:

`#!/usr/bin/bash`

