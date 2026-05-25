+++
date = "2025-08-16T15:49:12+07:00"
draft = false
title = 'Ssh Trick'
description = "Tạo public key từ private key hiện có chỉ với một lệnh ssh-keygen."
summary = "Tạo public key từ private key hiện có chỉ với một lệnh ssh-keygen."
slug = "ssh-trick"
authors = [ ]
tags = [ "ssh", "cli" ]
categories = [ ]
externalLink = ""
series = [ ]
images = [ ]
+++

## Tạo public key từ private key

```bash
ssh-keygen -y -f ~/.ssh/id_rsa > ~/.ssh/id_rsa.pub
```
