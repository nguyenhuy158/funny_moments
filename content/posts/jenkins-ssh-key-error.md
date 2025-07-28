+++
date = "2025-07-28T22:55:22+07:00"
draft = false
title = 'Jenkins Ssh Key Error'
description = ""
slug = ""
authors = [ ]
tags = [ ]
categories = [ ]
externalLink = ""
series = [ ]
images = [ ]
+++


```bash
docker exec -it <jenkins-container> bash
mkdir -p /var/jenkins_home/.ssh
ssh-keyscan -t ed25519 gitlab.com >> /var/jenkins_home/.ssh/known_hosts
chown -R jenkins:jenkins /var/jenkins_home/.ssh
chmod 600 /var/jenkins_home/.ssh/known_hosts
```