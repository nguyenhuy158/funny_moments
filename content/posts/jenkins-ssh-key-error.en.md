+++
date = "2025-07-28T22:55:22+07:00"
draft = false
title = 'Jenkins Ssh Key Error'
description = "Fix Jenkins SSH host key errors by adding the remote host to known_hosts inside the container."
summary = "Fix Jenkins SSH host key errors by adding the remote host to known_hosts inside the container."
slug = "jenkins-ssh-key-error"
authors = [ ]
tags = [ "jenkins", "ssh", "gitlab" ]
categories = [ ]
externalLink = ""
series = [ ]
images = [ ]
+++

When Jenkins fails because the SSH host key is missing, add the remote host to `known_hosts` inside the container:

```bash
docker exec -it <jenkins-container> bash
mkdir -p /var/jenkins_home/.ssh
ssh-keyscan -t ed25519 gitlab.com >> /var/jenkins_home/.ssh/known_hosts
chown -R jenkins:jenkins /var/jenkins_home/.ssh
chmod 600 /var/jenkins_home/.ssh/known_hosts
```
