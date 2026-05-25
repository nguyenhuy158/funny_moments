+++
date = "2025-08-16T15:49:12+07:00"
draft = false
title = 'Ssh Trick'
description = "Generate a public key from an existing private key with a single ssh-keygen command."
summary = "Generate a public key from an existing private key with a single ssh-keygen command."
slug = "ssh-trick"
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
