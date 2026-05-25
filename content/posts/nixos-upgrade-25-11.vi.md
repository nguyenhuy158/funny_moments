+++
title = "How to Upgrade NixOS to 25.11"
date = 2025-12-06T00:54:21+07:00
description = "Hướng dẫn từng bước để nâng cấp hệ thống NixOS của bạn lên bản 25.11."
summary = "Hướng dẫn từng bước để nâng cấp hệ thống NixOS của bạn lên bản 25.11."
slug = "nixos-upgrade-25-11"
tags = ["nixos", "linux", "upgrade", "tutorial"]
categories = ["Linux", "NixOS"]
draft = false
authors = []
series = []
images = []
+++

Nâng cấp NixOS khá đơn giản, nhưng vẫn nên đi đúng thứ tự để tránh lỗi không cần thiết. Đây là các bước để nâng cấp hệ thống lên NixOS 25.11.

## 1. Kiểm tra channel hiện tại

```bash
nix-channel --list
```

## 2. Thêm channel 25.11 mới

```bash
sudo nix-channel --add https://nixos.org/channels/nixos-25.11 nixos
```

## 3. Cập nhật toàn bộ channel

```bash
sudo nix-channel --update
```

## 4. Đọc release notes

Đây là bước quan trọng. Hãy đọc release notes để biết các thay đổi có thể ảnh hưởng đến cấu hình hiện tại.

Xem tại: [nixos.org/manual/nixos/stable/release-notes](https://nixos.org/manual/nixos/stable/release-notes)

## 5. Rebuild hệ thống

Lúc này bạn có thể rebuild hệ thống. Quá trình này sẽ tải và build các package mới.

Dùng `--upgrade` để áp dụng một số fix phổ biến tự động:

```bash
sudo nixos-rebuild switch --upgrade
```

Hoặc nếu muốn build trước và kích hoạt sau khi reboot:

```bash
sudo nixos-rebuild boot --upgrade
```

## 6. Khởi động lại

Nếu bạn dùng lệnh `boot` hoặc muốn chắc chắn hệ thống chạy hoàn toàn trên bản mới, hãy reboot:

```bash
sudo reboot
```
