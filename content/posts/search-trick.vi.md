+++
date = "2025-08-28T10:57:37+07:00"
draft = false
title = 'Search Trick'
description = "Ghi chú nhanh về cách gom ID từ các bảng liên quan trước khi query bảng chính để trả kết quả tìm kiếm."
summary = "Ghi chú nhanh về cách gom ID từ các bảng liên quan trước khi query bảng chính để trả kết quả tìm kiếm."
slug = "search-trick"
authors = [ ]
tags = [ "backend", "search", "sql" ]
categories = [ ]
externalLink = ""
series = [ ]
images = [ ]
+++

Khi điều kiện tìm kiếm phụ thuộc vào nhiều bảng liên quan, hãy query từng bảng trước, lấy ra tập ID chung, gộp chúng bằng `AND` hoặc `OR`, rồi mới query bảng chính để hiển thị kết quả.

- `handle` thuộc tầng UI
- `server` thuộc tầng business logic
