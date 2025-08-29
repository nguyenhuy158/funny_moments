+++
date = "2025-08-29T17:28:03+07:00"
draft = false
title = 'The Art of Readable Code'
description = ""
slug = ""
authors = [ ]
tags = [ ]
categories = [ ]
externalLink = ""
series = [ ]
images = [ ]
+++

# 📖 Summary of *The Art of Readable Code*

## 1. Code Should Be Easy to Understand

-   **Ý chính:** Giảm *thời gian để hiểu code*.\

-   Code dễ đọc quan trọng hơn code ngắn.\

-   Ví dụ:

    ``` cpp
    // Khó hiểu
    return exponent >= 0 ? mantissa * (1 << exponent) : mantissa / (1 << -exponent);

    // Rõ ràng hơn
    if (exponent >= 0) {
        return mantissa * (1 << exponent);
    } else {
        return mantissa / (1 << -exponent);
    }
    ```

------------------------------------------------------------------------

## 2. Packing Information into Names

-   **Tên là comment ngắn.**\

-   Dùng từ cụ thể, rõ ràng.\

-   Thêm đơn vị hoặc thuộc tính nếu quan trọng.\

-   Ví dụ:

    ``` python
    # Không tốt
    def GetPage(url): ...

    # Tốt hơn
    def FetchPage(url): ...
    ```

-   Ví dụ có đơn vị:

    ``` js
    var elapsed_ms = (new Date()).getTime() - start_ms;
    ```

------------------------------------------------------------------------

## 3. Names That Can't Be Misconstrued

-   Tránh tên gây nhầm lẫn.\

-   Dùng `min_`/`max_` cho giới hạn, `first/last` cho phạm vi bao gồm,
    `begin/end` cho phạm vi nửa mở.\

-   Boolean nên bắt đầu bằng `is_`, `has_`, `can_`.\

-   Ví dụ:

    ``` python
    # Không rõ nghĩa
    read_password = True

    # Rõ ràng hơn
    need_password = True
    ```

------------------------------------------------------------------------

## 4. Aesthetics

-   Code nên **sạch và gọn**.\

-   Quy tắc: layout đồng nhất, code giống nhau nên trông giống nhau,
    nhóm dòng liên quan.\

-   Dùng helper method để rút gọn test case.\

-   Ví dụ:

    ``` cpp
    // Trước
    assert(ExpandFullName("Doug Adams") == "Mr. Douglas Adams");
    assert(ExpandFullName("No Such Guy") == "");

    // Sau
    CheckFullName("Doug Adams", "Mr. Douglas Adams", "");
    CheckFullName("No Such Guy", "", "no match found");
    ```

------------------------------------------------------------------------

## 5. Knowing What to Comment

-   Comment nên giải thích **tại sao**, không lặp lại **cái gì**.\

-   Tránh comment hiển nhiên.\

-   Viết điều giúp người đọc sau này hiểu nhanh hơn.\

-   Ví dụ:

    ``` cpp
    // Phiên bản nhanh của "hash = (65599 * hash) + c"
    hash = (hash << 6) + (hash << 16) - hash + c;
    ```

------------------------------------------------------------------------

## 6. Making Comments Precise and Compact

-   Comment phải ngắn gọn, chính xác.\

-   Tránh dùng đại từ mơ hồ ("it", "this").\

-   Dùng ví dụ input/output, đặc biệt với edge case.\

-   Ví dụ:

    ``` python
    # Cắt chuỗi nếu dài quá max_chars và thêm "..."
    def Truncate(text, max_chars): ...
    ```

------------------------------------------------------------------------

## 7. Making Control Flow Easy to Read

-   Viết `if/else` rõ ràng.\

-   Dùng return sớm để giảm nesting.\

-   Tránh `goto` và `do/while`.\

-   Ví dụ:

    ``` python
    # Lồng nhiều tầng
    if user:
        if user.is_active:
            return True
        else:
            return False

    # Return sớm
    if not user:
        return False
    return user.is_active
    ```

------------------------------------------------------------------------

## 8. Breaking Down Giant Expressions

-   Chia nhỏ biểu thức phức tạp.\

-   Dùng biến trung gian để dễ hiểu hơn.\

-   Áp dụng luật De Morgan khi cần.\

-   Ví dụ:

    ``` python
    # Khó đọc
    if not (file_exists and not file_is_empty):

    # Rõ ràng hơn
    missing_or_empty = (not file_exists) or file_is_empty
    if missing_or_empty:
        ...
    ```

------------------------------------------------------------------------

## 9. Variables and Readability

-   Ít biến hơn → code dễ đọc hơn.\

-   Thu hẹp phạm vi biến.\

-   Ưu tiên biến chỉ gán 1 lần.\

-   Ví dụ:

    ``` python
    # Không tốt: tái sử dụng biến
    result = query_db()
    result = format(result)

    # Tốt hơn
    raw_result = query_db()
    formatted = format(raw_result)
    ```

------------------------------------------------------------------------

## 10. Extracting Unrelated Subproblems

-   Tách logic không liên quan thành hàm riêng.\

-   Giúp code tái sử dụng và dễ hiểu hơn.\

-   Ví dụ:

    ``` python
    # Trước
    def find_closest_location(user, locations):
        best_dist = float("inf")
        for loc in locations:
            dist = compute_distance(user, loc)
            if dist < best_dist:
                best_dist = dist
                best_loc = loc
        return best_loc
    ```

    ``` python
    # Sau
    def distance_between(a, b): ...
    def find_closest_location(user, locations):
        return min(locations, key=lambda loc: distance_between(user, loc))
    ```

------------------------------------------------------------------------

## 11. One Task at a Time

-   Mỗi hàm chỉ nên làm **1 việc**.\

-   Công việc nhỏ dễ test và dễ maintain.\

-   Ví dụ:

    ``` python
    # Trước: parse + validate chung
    def get_user_id(data):
        id = int(data.split(",")[0])
        if id < 0:
            raise ValueError("Invalid id")
        return id

    # Sau: tách riêng
    def parse_id(data): ...
    def validate_id(id): ...
    ```

------------------------------------------------------------------------

## 12. Turning Thoughts into Code

-   Viết code giống cách mình nghĩ.\

-   Dùng ngôn ngữ diễn đạt rõ ràng, tận dụng thư viện.\

-   Ví dụ:

    ``` python
    # Ý nghĩ: "lấy email user active"
    emails = [user.email for user in users if user.is_active]
    ```

------------------------------------------------------------------------

## 13. Writing Less Code

-   Ít code hơn → ít bug hơn.\

-   Không viết tính năng thừa.\

-   Tận dụng thư viện và công cụ có sẵn.\

-   Ví dụ:

    ``` bash
    # Thay vì viết code tìm file
    grep "keyword" *.txt
    ```

------------------------------------------------------------------------

## 14. Testing and Readability

-   Test cũng cần dễ đọc và dễ sửa.\

-   Dùng input có ý nghĩa.\

-   Đặt tên test mô tả rõ ràng.\

-   Message lỗi phải rõ ràng.\

-   Ví dụ:

    ``` python
    # Không tốt
    def test_1():
        assert f(123, 5) == 345

    # Tốt hơn
    def test_add_offset_to_id():
        assert f(user_id=123, offset=5) == 345
    ```

------------------------------------------------------------------------

## 15. Designing and Implementing a "Minute/Hour Counter"

-   Bài toán ví dụ: đếm sự kiện theo phút/giờ.\

-   3 cách tiếp cận:

    1.  **Naive** -- đơn giản nhưng không hiệu quả.\
    2.  **Conveyor belt design** -- dịch sự kiện theo thời gian.\
    3.  **Time-bucketed design** -- chia thành bucket cố định.\

-   Bài học: thiết kế rõ ràng và dễ bảo trì tốt hơn hack nhanh.\

-   Ví dụ (giản lược):

    ``` python
    class MinuteHourCounter:
        def __init__(self):
            self.minute_buckets = [0] * 60
            self.hour_buckets = [0] * 24

        def record_event(self, timestamp):
            self.minute_buckets[timestamp.minute] += 1
            self.hour_buckets[timestamp.hour] += 1
    ```
