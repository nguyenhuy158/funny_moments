+++
date = "2026-08-05T23:15:00+07:00"
draft = false
title = 'NixOS xrdp màn hình đen: "Unable to load a failsafe session"'
description = "Vì sao chỉ thêm package xfce4-session làm xrdp trên NixOS bị lỗi, và cách sửa đúng chỉ mất một dòng config."
summary = "Vì sao chỉ thêm package xfce4-session làm xrdp trên NixOS bị lỗi, và cách sửa đúng chỉ mất một dòng config."
slug = "nixos-xrdp-xfce4-session-failsafe"
authors = [ ]
tags = [ "nixos", "xrdp", "xfce" ]
categories = [ "sysadmin" ]
externalLink = ""
series = [ ]
images = [ ]
+++

## Bối cảnh

Máy NixOS bật `services.xrdp.enable = true;` với
`defaultWindowManager = "xfce4-session";`. Từ macOS connect RDP vào, thay vì
vào được desktop thì gặp:

- màn hình đen, hoặc
- một hộp thoại lỗi: **"Unable to load a failsafe session"** với nội dung:

```
Unable to determine failsafe session name. Possible causes: xfconfd isn't
running (D-Bus setup problem); environment variable $XDG_CONFIG_DIRS is set
incorrectly (must include "/nix/store/<hash>-xfce4-session-.../etc"), or
xfce4-session is installed incorrectly.
```

## Lần sửa đầu tiên (sai)

Cách nghĩ hiển nhiên nhất: log `journalctl -u xrdp-sesman` báo
`xfce4-session: command not found`, nên cứ thêm package vào là xong:

```nix
environment.systemPackages = with pkgs; [
  xfce.xfce4-session
];
```

Lỗi "command not found" hết thật — nhưng đổi sang lỗi failsafe session ở
trên. Có tiến triển, nhưng vẫn chưa chạy được.

## Nguyên nhân gốc

Ở các distro Linux thông thường, config của `xfce4-session` nằm ở
`/etc/xdg`, vốn đã có sẵn trong `$XDG_CONFIG_DIRS` mặc định của mọi process.
Trên NixOS, config của package lại nằm trong path riêng của Nix store
(`/nix/store/<hash>-xfce4-session-4.20.3/etc`), và không có gì tự thêm nó
vào `$XDG_CONFIG_DIRS` — trừ khi có thứ gì đó wrap môi trường giúp mình.

Thứ đó chính là `services.xserver.desktopManager.xfce`. Nó không chỉ là
wrapper tiện lợi cho login manager — nó là thứ thật sự vá lại các biến môi
trường của session (`XDG_CONFIG_DIRS`, `XDG_DATA_DIRS`, ...) để các tool
XFCE tìm đúng config của mình lúc chạy. Cài `xfce.xfce4-session` như một
package trần thì bỏ qua hết phần dây nhợ này.

## Cách sửa đúng

```nix
services.xserver.enable = true;
services.xserver.desktopManager.xfce.enable = true;

services.xrdp = {
  enable = true;
  defaultWindowManager = "xfce4-session";
  openFirewall = true;
};
```

Chú ý là không cần khai `displayManager` ở đây — xrdp tự spawn X session
riêng cho mỗi lần connect RDP, không dùng display manager của hệ thống.
Chỉ cần bật desktop manager để có đúng phần wrap môi trường; không cần
GDM/LightDM chạy phía trên.

Bỏ luôn package `xfce.xfce4-session` trần một khi đã bật
`desktopManager.xfce` — nó đã tự kéo `xfce4-session` vào như dependency,
lần này với môi trường được nối dây đúng.

## Bài học

Trên NixOS, "binary có trong PATH" và "binary chạy đúng" là hai điều đảm
bảo khác nhau. Các package desktop environment thường mang theo phần nối
dây môi trường đặc thù của NixOS, chỉ được thiết lập đúng qua module
`services.xserver.desktopManager.*` tương ứng — cài package thô không
tương đương với bật module.
