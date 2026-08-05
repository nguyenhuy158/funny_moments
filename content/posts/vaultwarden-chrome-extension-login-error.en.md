+++
date = '2026-08-05T21:10:00+07:00'
draft = false
title = 'Vaultwarden: Web login works but Chrome Extension says "An error has occurred"'
author = []
summary = "Debugging a self-hosted Vaultwarden issue where the Chrome extension fails to log in while the web vault works fine - turned out to be a stale server version."
tags = ["docker", "vaultwarden", "selfhost", "bitwarden", "chrome"]
+++

Self-hosting Vaultwarden (a Bitwarden-compatible server) behind a Cloudflare Tunnel, everything was smooth until one day the Chrome extension refused to log in with the utterly unhelpful message: **"An error has occurred"**. No error code, no details. Meanwhile the web vault (`https://your-domain/`) logged in just fine.

## Step 1: Check the container logs

First rule of self-hosting debugging: always check logs first.

```bash
docker logs -f vaultwarden
```

Logging in via web was clean:

```
POST /identity/connect/token => 200 OK
GET /api/sync => 200 OK
GET /api/accounts/profile => 200 OK
```

But trying to log in from the Chrome extension spammed this repeatedly:

```
POST /identity/accounts/prelogin/password => 404 Not Found
```

Same request retried every few seconds, eventually ending with:

```
POST /api/accounts/password-hint => 400 Bad Request
[ERROR] This server is not configured to provide password hints.
```

## Step 2: Root cause

`/identity/accounts/prelogin/password` is a **newer** endpoint used by Bitwarden clients (including the Chrome extension) as part of the pre-login auth flow. The server returned 404 because the running Vaultwarden version simply **didn't implement that endpoint yet**.

Checked the running version:

```bash
docker logs vaultwarden 2>&1 | grep Version
# Version 1.35.7
```

Fairly old. Meanwhile the Chrome extension auto-updates itself to the latest client, and the newer client expects the server to support the new login flow.

**Lesson learned:** when self-hosting a client-server app where the client auto-updates (browser extensions, mobile apps...), keep the server in sync too. Version drift between client and server is one of the most common causes of confusing, generic-looking errors.

## Step 3: Update the server

```bash
docker pull vaultwarden/server:latest
docker compose up -d
```

After upgrading to `1.37.1`, the Chrome extension login worked immediately - no more `404` on `prelogin/password`.

## A few safety notes

- If you're pinning `:latest` in `compose.yml`, the old image isn't deleted automatically - it just gets untagged. `docker images -a` will still show the old image ID, so you can pin it back if you ever need to roll back.
- **Back up your database before upgrading**, even though version bumps rarely touch the schema. Better safe than sorry - especially if you're also planning to switch database backends (e.g. SQLite ↔ Postgres) around the same time. Do those changes separately so it's easier to isolate issues.
- `docker logs -f <container>` is your first and best debugging tool for self-hosted services - don't guess, read the logs.

Bottom line: sometimes a scary generic error like "An error has occurred" is just the server being **older than the client expects**. Upgrading to the latest version fixes it.
