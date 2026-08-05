+++
date = '2026-08-05T21:10:00+07:00'
draft = false
title = 'Vaultwarden: Login web OK nhưng Chrome Extension báo "An error has occurred"'
author = []
summary = "Debug lỗi Chrome extension không login được vào Vaultwarden self-host trong khi web vẫn login bình thường - nguyên nhân là version server quá cũ."
tags = ["docker", "vaultwarden", "selfhost", "bitwarden", "chrome"]
+++

Đang self-host Vaultwarden (Bitwarden server thay thế) đằng sau Cloudflare Tunnel, mọi thứ chạy êm re cho tới một ngày mở Chrome extension login thì chỉ nhận được câu thông báo vô nghĩa: **"An error has occurred"**. Không mã lỗi, không chi tiết gì thêm. Trong khi đó login qua web vault (`https://your-domain/`) thì vẫn vào bình thường, không có vấn đề gì.

## Bước 1: Xem log container

Việc đầu tiên khi self-host bị lỗi kỳ lạ: luôn luôn xem log trước.

```bash
docker logs -f vaultwarden
```

Login qua web thì log sạch đẹp:

```
POST /identity/connect/token => 200 OK
GET /api/sync => 200 OK
GET /api/accounts/profile => 200 OK
```

Nhưng khi bấm login từ Chrome extension, log lại spam liên tục dòng này:

```
POST /identity/accounts/prelogin/password => 404 Not Found
```

Cứ vài giây lại có một request y chang, rồi cuối cùng dừng lại ở:

```
POST /api/accounts/password-hint => 400 Bad Request
[ERROR] This server is not configured to provide password hints.
```

## Bước 2: Xác định nguyên nhân

Endpoint `/identity/accounts/prelogin/password` là API **mới** mà Bitwarden client (bao gồm Chrome extension) dùng để xác thực trước khi login. Server trả 404 vì đơn giản là **bản Vaultwarden đang chạy chưa hỗ trợ endpoint này**.

Kiểm tra version đang chạy:

```bash
docker logs vaultwarden 2>&1 | grep Version
# Version 1.35.7
```

Đây là bản khá cũ, ra mắt cách đây một thời gian, còn Chrome extension thì tự động update lên bản mới nhất - và bản extension mới yêu cầu server phải hỗ trợ flow login mới.

**Bài học:** khi self-host một service kiểu client-server mà client tự động update (extension, mobile app...), nhớ để ý server cũng phải theo kịp. Chênh version giữa client và server là một trong những nguyên nhân phổ biến nhất gây lỗi khó hiểu như thế này.

## Bước 3: Update server

```bash
docker pull vaultwarden/server:latest
docker compose up -d
```

Sau khi lên `1.37.1`, thử login lại bằng Chrome extension - pass ngay, không còn `404` trên `prelogin/password` nữa.

## Một vài lưu ý an toàn khi làm theo

- Nếu bạn dùng tag `:latest` trong `compose.yml`, image cũ chỉ bị **untag** chứ Docker không tự xoá nếu container cũ còn tồn tại - `docker images -a` vẫn thấy image ID cũ, có thể pin lại để rollback khi cần.
- **Backup database trước khi update**, dù việc update version thường không đụng tới schema, nhưng cẩn tắc vô áy náy - đặc biệt nếu bạn còn đang có ý định đổi backend database (SQLite ↔ Postgres) cùng lúc, tách 2 việc đó ra làm riêng để dễ debug nếu có sự cố.
- `docker logs -f <container>` là công cụ đầu tiên và tốt nhất khi debug self-host - đừng đoán, đọc log trước.

Kết luận: đôi khi lỗi generic tệ hại như "An error has occurred" chỉ đơn giản là do **server quá cũ so với client**. Update lên bản mới nhất là xong.
