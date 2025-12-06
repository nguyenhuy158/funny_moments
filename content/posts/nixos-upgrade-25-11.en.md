+++
title = "How to Upgrade NixOS to 25.11"
date = 2025-12-06T00:54:21+07:00
description = "A step-by-step guide to upgrading your NixOS system to the latest 25.11 release."
slug = "nixos-upgrade-25-11"
tags = ["nixos", "linux", "upgrade", "tutorial"]
categories = ["Linux", "NixOS"]
draft = false
authors = []
series = []
images = []
+++

Upgrading NixOS is a straightforward process, but it's important to follow the correct steps to ensure a smooth transition. Here is a guide on how to upgrade your system to NixOS 25.11.

## 1. List Current Channels

First, it's a good idea to verify your current channels.

```bash
nix-channel --list
```

## 2. Add the New 25.11 Channel

Add the new NixOS 25.11 channel to your system.

```bash
sudo nix-channel --add https://nixos.org/channels/nixos-25.11 nixos
```

## 3. Update All Channels

Update your channels to download the new package definitions.

```bash
sudo nix-channel --update
```

## 4. Read the Release Notes

**Crucial Step:** Before proceeding, make sure to read the release notes for any breaking changes that might affect your configuration.

Check the release notes at: [nixos.org/manual/nixos/25.11/release-notes](https://nixos.org/manual/nixos/25.11/release-notes)

## 5. Rebuild Your System

Now, rebuild your system. This process will take some time as it downloads and compiles the new packages.

Use the `--upgrade` flag to automatically apply fixes for some common changes.

```bash
sudo nixos-rebuild switch --upgrade
```

Alternatively, if you want to build and boot into the new system without activating it immediately:

```bash
sudo nixos-rebuild boot --upgrade
```

## 6. Reboot

If you used the `boot` command or want to be fully on the new system, perform a reboot.

```bash
sudo reboot