+++
date = '2026-05-24T10:34:07+07:00'
draft = false
title = '2 Cleanup Tools for Node.js and Python'
author = []
description = "Two lightweight CLI tools to clean up old node_modules, Python virtual environments, and cache directories."
slug = "npkill-killpy"
summary = "Two small but useful CLIs: `npx npkill` to clean up `node_modules`, and `uvx killpy` to find and remove Python virtual environments and caches eating disk space."
tags = ["nodejs", "python", "cli", "tool", "tip", "disk"]
+++

If your dev machine handles both **Node.js** and **Python**, sooner or later your disk will get crowded with:

- `node_modules`
- `.venv`
- `__pycache__`
- caches from `poetry`, `pipx`, `uv`, `tox`, and more

These are 2 tools worth keeping in mind.

## 1. `npx npkill`

When you want to find and remove old `node_modules` folders, `npkill` is a very fast option:

```bash
npx npkill
```

It scans from the current directory, lists detected `node_modules`, and shows their sizes so you can delete them interactively in the terminal.

What I like about it:

- no global install needed
- easy to spot folders eating several GB
- interactive deletion, so no need for ugly `find ... -exec rm -rf`

If you want to scan a specific directory:

```bash
npx npkill -d ~/Projects
```

## 2. `uvx killpy`

If `npkill` is the cleanup tool for Node.js, then `killpy` feels like the Python equivalent:

```bash
uvx killpy --path ~
```

`killpy` can find things like:

- `.venv`
- `poetry` environments
- `conda` environments
- envs from `pipenv`, `pipx`, `pyenv`, `uv`
- caches such as `__pycache__`, `.pytest_cache`, `.mypy_cache`

The nice part is that it gathers everything in one place instead of forcing you to remember scattered paths across your home directory.

If you only want to scan the current folder:

```bash
uvx killpy
```

## When should you use them?

I usually run:

- `npx npkill` when old Node.js repos are taking too much space
- `uvx killpy --path ~` when I want to do a general Python cleanup on my machine

Both tools fit the same pattern:

- run once when needed
- no permanent install required
- very useful when your disk is full and you are not sure why

If you work across multiple stacks, these 2 commands can save quite a few GB:

```bash
npx npkill
uvx killpy --path ~
```
