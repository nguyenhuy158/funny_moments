+++
date = "2025-07-08T23:00:53+07:00"
draft = false
title = 'Shell Env'
description = "Why /usr/bin/env is a safer shebang choice for portable shell scripts across environments."
slug = "shell-env"
authors = []
tags = []
categories = []
externalLink = ""
series = []
images = []
+++

Use `/usr/bin/env` in Shell Scripts
When writing shell scripts, avoid hardcoding the full path to the shell.
Instead, use the environment path to make your script more portable across different systems.

## ✅ Recommended:

`#!/usr/bin/env bash`

## 🚫 Not recommended:

`#!/usr/bin/bash`

Using env ensures the system uses the correct version of the shell from the user's environment.
