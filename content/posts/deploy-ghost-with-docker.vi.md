+++
draft = false
date = 2025-07-01T21:59:31+07:00
title = "Deploy Ghost With Docker"
description = "Cấu hình Docker Compose tối giản để chạy Ghost ở máy local hoặc trên server nhỏ."
summary = "Cấu hình Docker Compose tối giản để chạy Ghost ở máy local hoặc trên server nhỏ."
slug = "deploy-ghost-with-docker"
authors = []
tags = []
categories = []
externalLink = ""
series = []
+++

Ghost là một nền tảng khá phù hợp cho người mới bắt đầu blog nhanh.
Dưới đây là một cấu hình `docker-compose.yml` đơn giản để chạy ngay:

```yaml
services:
  ghost:
    image: ghost
    container_name: ghost
    ports:
      - "2368:2368"
    environment:
      - NODE_ENV=development
      - database__connection__filename=/var/lib/ghost/content/data/ghost.db
      - url=http://localhost:2368
    volumes:
      - ./ghost-data:/var/lib/ghost/content
```
