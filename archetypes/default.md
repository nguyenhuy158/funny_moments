+++
date = "{{ .Date }}"
draft = false
title = '{{ replace .File.ContentBaseName "-" " " | title }}'
description = "TODO: add a one-sentence description."
slug = '{{ replace .File.ContentBaseName "." "-" }}'
authors = [ ]
tags = [ ]
categories = [ ]
externalLink = ""
series = [ ]
images = [ ]
+summary = ""
+++
