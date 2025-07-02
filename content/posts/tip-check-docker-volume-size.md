+++
date = '2025-07-01T22:07:45+07:00'
draft = false
title = 'Tip Check Docker Volume Size'
author = "nguyenhuy158"
summary = "Cách kiểm tra dung lượng Docker volume một cách nhanh gọn bằng lệnh CLI."
tags = ["docker", "tip", "volume"]
+++

Muốn xem dung lượng Docker volumes đang chiếm bao nhiêu? Dễ lắm!

Chạy lệnh sau trong terminal:

```bash
docker system df -v
```