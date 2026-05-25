+++
date = '2025-07-03T10:17:23+07:00'
draft = false
title = 'Handle Json Key Case'
description = "Normalize inconsistent JSON key casing before mapping data in your application."
summary = "Normalize inconsistent JSON key casing before mapping data in your application."
slug = "handle-json-key-case"
authors = []
tags = ["json", "python", "data-cleaning", "tip"]
categories = []
externalLink = ''
series = []
+++

When working with JSON data from different sources, you might see inconsistent key names, like:

```json
{
  "tTien": 1000,
  "ttien": 1000,
  "tthue": 100,
  "tThue": 100,
  "TThue": 100
}
```

Different places use different names, which is annoying. Using try/except, if/else, or match/case makes the code messy and error-prone.

Simple solution:
Before processing, convert all keys to lowercase. It's fast and easy to maintain: `data = {k.lower(): v for k, v in original_data.items()}` Now you can just use `data['ttien']`, `data['tthue']` without writing long code.

Bonus:
If keys have spaces or dashes (-, _), you can normalize further:
```python
import re

def normalize_key(k):
    return re.sub(r'\W+', '', k).lower()

data = {normalize_key(k): v for k, v in original_data.items()}
