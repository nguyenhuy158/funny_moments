+++
date = "{{ .Date }}"
draft = false
title = '{{ replace .File.ContentBaseName "-" " " | title }}'
description = ""
slug = '{{ replace .File.ContentBaseName "." "-" }}'
authors = [ ]
tags = [ ]
categories = [ ]
externalLink = ""
series = [ ]
images = [ ]
+++
