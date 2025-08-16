+++
date = "2025-08-16T15:49:12+07:00"
draft = false
title = 'Ssh Trick'
description = ""
slug = ""
authors = [ ]
tags = [ ]
categories = [ ]
externalLink = ""
series = [ ]
images = [ ]
+++

## gen public key from private key

```bash
ssh-keygen -y -f ~/.ssh/id_rsa > ~/.ssh/id_rsa.pub
```