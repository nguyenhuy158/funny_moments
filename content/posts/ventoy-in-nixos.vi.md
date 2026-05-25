+++
date = "2025-07-13T00:40:37+07:00"
draft = false
title = 'Ventoy in Nixos'
description = "Ghi chú để chạy Ventoy trên NixOS 25 khi cấu hình mặc định gặp lỗi."
summary = "Ghi chú để chạy Ventoy trên NixOS 25 khi cấu hình mặc định gặp lỗi."
slug = "ventoy-in-nixos"
authors = [ ]
tags = [ ]
categories = [ ]
externalLink = ""
series = [ ]
images = [ ]
+++

## Lỗi

Ventoy hiện có thể gặp lỗi khi chạy trên NixOS 25.

## Cách xử lý

Chỉ cần export biến môi trường và thêm `--impure` vào lệnh cuối:

```bash
export NIXPKGS_ALLOW_INSECURE=1
nix run .#huy --impure
```
