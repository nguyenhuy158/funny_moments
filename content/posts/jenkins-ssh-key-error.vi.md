+++
date = "2025-07-28T22:55:22+07:00"
draft = false
title = 'Jenkins Ssh Key Error'
description = "Sửa lỗi Jenkins không xác thực được SSH host key bằng cách thêm remote host vào known_hosts trong container."
summary = "Sửa lỗi Jenkins không xác thực được SSH host key bằng cách thêm remote host vào known_hosts trong container."
slug = "jenkins-ssh-key-error"
authors = [ ]
tags = [ "jenkins", "ssh", "gitlab" ]
categories = [ ]
externalLink = ""
series = [ ]
images = [ ]
+++

Khi Jenkins báo lỗi vì thiếu SSH host key, hãy thêm remote host vào `known_hosts` bên trong container:

```bash
docker exec -it <jenkins-container> bash
mkdir -p /var/jenkins_home/.ssh
ssh-keyscan -t ed25519 gitlab.com >> /var/jenkins_home/.ssh/known_hosts
chown -R jenkins:jenkins /var/jenkins_home/.ssh
chmod 600 /var/jenkins_home/.ssh/known_hosts
```
