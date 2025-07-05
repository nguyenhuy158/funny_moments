+++
date = '2025-07-03T10:17:23+07:00'
draft = false
title = 'Handle Json Key Case'
description = ''
slug = ''
authors = []
tags = ["json", "python", "data-cleaning", "tips"]
categories = []
externalLink = ''
series = []
+++

Khi làm việc với dữ liệu JSON từ nhiều nguồn, chắc chắn bạn từng gặp cảnh key không đồng nhất như:

```json
{
  "tTien": 1000,
  "ttien": 1000,
  "tthue": 100,
  "tThue": 100,
  "TThue": 100
}
```

Mỗi nơi đặt tên mỗi kiểu, khó xử lý. Nếu cứ try/except, if/else hay match/case thì code sẽ loằng ngoằng và dễ lỗi.

Giải pháp gọn nhẹ
Trước khi xử lý, convert hết key về lowercase. Cực nhanh và dễ maintain: `data = {k.lower(): v for k, v in original_data.items()}` Giờ thì chỉ cần `data['ttien']`, `data['tthue']` thôi, khỏi lo viết dài dòng.

Bonus
Nếu key có dấu cách hoặc dấu gạch (-, _), có thể normalize thêm:
```python
import re

def normalize_key(k):
    return re.sub(r'\W+', '', k).lower()

data = {normalize_key(k): v for k, v in original_data.items()}
```
