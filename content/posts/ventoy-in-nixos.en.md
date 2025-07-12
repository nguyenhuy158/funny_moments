+++
date = "2025-07-13T00:40:37+07:00"
draft = false
title = 'Ventoy in Nixos'
description = ""
slug = ""
authors = [ ]
tags = [ ]
categories = [ ]
externalLink = ""
series = [ ]
images = [ ]
+++


## Error
ventoy currently error when using nixos version 25

## solution 

just export enviroment variable and append **--impure** to the last command script
```bash
export NIXPKGS_ALLOW_INSECURE=1
nix run .#huy --impure
```