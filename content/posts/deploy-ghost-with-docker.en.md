+++
draft = false
date = 2025-07-01T21:59:31+07:00
title = "Deploy Ghost With Docker"
description = ""
slug = ""
authors = []
tags = []
categories = []
externalLink = ""
series = []
+++

Ghost is one of the best platforms for beginners who wanna start blogging fast.
Below is a simple `docker-compose.yml` setup to get you going right away:

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

