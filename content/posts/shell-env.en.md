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

Use `/usr/bin/env` in Shell Scripts
When writing shell scripts, avoid hardcoding the full path to the shell.
Instead, use the environment path to make your script more portable across different systems.

## ✅ Recommended:

`#!/usr/bin/env bash`

## 🚫 Not recommended:

`#!/usr/bin/bash`

Using env ensures the system uses the correct version of the shell from the user's environment.