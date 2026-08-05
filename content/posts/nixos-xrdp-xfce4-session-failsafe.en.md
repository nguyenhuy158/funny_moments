+++
date = "2026-08-05T23:15:00+07:00"
draft = false
title = 'NixOS xrdp black screen: "Unable to load a failsafe session"'
description = "Why adding the xfce4-session package alone breaks xrdp on NixOS, and the one-line fix that actually works."
summary = "Why adding the xfce4-session package alone breaks xrdp on NixOS, and the one-line fix that actually works."
slug = "nixos-xrdp-xfce4-session-failsafe"
authors = [ ]
tags = [ "nixos", "xrdp", "xfce" ]
categories = [ "sysadmin" ]
externalLink = ""
series = [ ]
images = [ ]
+++

## The setup

`services.xrdp.enable = true;` with `defaultWindowManager = "xfce4-session";` on NixOS. Connect from macOS with a RDP client, and instead of a desktop you get either:

- a black screen, or
- an error dialog: **"Unable to load a failsafe session"** with the message:

```
Unable to determine failsafe session name. Possible causes: xfconfd isn't
running (D-Bus setup problem); environment variable $XDG_CONFIG_DIRS is set
incorrectly (must include "/nix/store/<hash>-xfce4-session-.../etc"), or
xfce4-session is installed incorrectly.
```

## First (wrong) fix

The obvious move: `xfce4-session: command not found` shows up in
`journalctl -u xrdp-sesman`, so just add the package:

```nix
environment.systemPackages = with pkgs; [
  xfce.xfce4-session
];
```

That gets rid of "command not found" — but now you get the failsafe-session
error above instead. Progress, but still broken.

## Root cause

On a normal Linux distro, `xfce4-session`'s config lives under `/etc/xdg`,
which is already in every process's default `$XDG_CONFIG_DIRS`. On NixOS,
the package's config lives inside its own Nix store path
(`/nix/store/<hash>-xfce4-session-4.20.3/etc`), and nothing sets
`$XDG_CONFIG_DIRS` to include it — unless something wraps the environment
for you.

That "something" is `services.xserver.desktopManager.xfce`. It's not just a
convenience wrapper for a login manager — it's the thing that actually
patches the session environment variables (`XDG_CONFIG_DIRS`,
`XDG_DATA_DIRS`, etc.) so XFCE tools can find their own config at runtime.
Installing `xfce.xfce4-session` as a bare package skips all of that wiring.

## The real fix

```nix
services.xserver.enable = true;
services.xserver.desktopManager.xfce.enable = true;

services.xrdp = {
  enable = true;
  defaultWindowManager = "xfce4-session";
  openFirewall = true;
};
```

Note there's no `displayManager` here — xrdp spins up its own X session per
RDP connection, it doesn't use the system's login manager. You only need
the desktop manager to get the correct environment wrapping; you don't need
GDM/LightDM sitting on top of it.

Remove the bare `xfce.xfce4-session` package once `desktopManager.xfce` is
enabled — it already pulls in `xfce4-session` as a dependency, with the
environment wired correctly this time.

## Lesson

On NixOS, "the binary is on PATH" and "the binary works correctly" are two
different guarantees. Desktop environment packages usually carry
NixOS-specific environment wiring that only gets set up through the
matching `services.xserver.desktopManager.*` module — installing the raw
package is not equivalent to enabling the module.
