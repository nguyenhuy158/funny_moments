+++
date = "2025-08-28T10:57:37+07:00"
draft = false
title = 'Search Trick'
description = "Quick note on combining IDs from related tables before querying the main table for search results."
summary = "Quick note on combining IDs from related tables before querying the main table for search results."
slug = "search-trick"
authors = [ ]
tags = [ "backend", "search", "sql" ]
categories = [ ]
externalLink = ""
series = [ ]
images = [ ]
+++

When search conditions depend on multiple related tables, query each table first, collect the shared IDs, combine them with `AND` or `OR`, and only then query the main table for display.

- `handle` belongs to the UI layer
- `server` belongs to the business logic layer
