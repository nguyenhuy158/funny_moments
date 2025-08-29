+++
date = "2025-08-29T17:16:07+07:00"
draft = false
title = 'The Art of Readable Code'
description = ""
slug = ""
authors = [ ]
tags = [ "books", "code", "cleancode", "java", "js", "python" ]
categories = [ ]
externalLink = ""
series = [ ]
images = [ ]
+++


# 📖 Summary of *The Art of Readable Code*

## 1. Code Should Be Easy to Understand

* **Key Idea:** Minimize *time-till-understanding*.
* Readable code is better than short code.
* Example:

  ```cpp
  // Less clear
  return exponent >= 0 ? mantissa * (1 << exponent) : mantissa / (1 << -exponent);

  // Clearer
  if (exponent >= 0) {
      return mantissa * (1 << exponent);
  } else {
      return mantissa / (1 << -exponent);
  }
  ```

---

## 2. Packing Information into Names

* **Names are mini-comments.**
* Use specific words, not vague ones.
* Add units/attributes if important.
* Example:

  ```python
  # Bad
  def GetPage(url): ...

  # Better
  def FetchPage(url): ...
  ```
* Example with units:

  ```js
  var elapsed_ms = (new Date()).getTime() - start_ms;
  ```

---

## 3. Names That Can’t Be Misconstrued

* **Avoid ambiguity.**
* Replace vague words (`filter`, `clip`) with precise ones.
* Use `min_/max_` for limits, `first/last` for inclusive ranges, `begin/end` for exclusive ranges.
* Boolean names: use `is_`, `has_`, `can_`.
* Example:

  ```python
  # Bad
  bool read_password = True   # unclear

  # Better
  bool need_password = True
  ```

---

## 4. Aesthetics

* **Readable code looks clean.**
* Principles: consistent layout, similar code looks similar, group related lines.
* Use helper methods to simplify long/ugly test cases.
* Example before:

  ```cpp
  assert(ExpandFullName("Doug Adams") == "Mr. Douglas Adams");
  assert(ExpandFullName("No Such Guy") == "");
  ```
* Example after (cleaner):

  ```cpp
  CheckFullName("Doug Adams", "Mr. Douglas Adams", "");
  CheckFullName("No Such Guy", "", "no match found");
  ```

---

## 5. Knowing What to Comment

* **Comment = giải thích ý định, không phải lặp lại code.**
* Đừng viết comment “obvious” (rõ ràng).
* Viết những điều giúp người đọc hiểu nhanh hơn.
* Example:

  ```cpp
  // Good: explains *why*, not *what*
  // Fast version of "hash = (65599 * hash) + c"
  hash = (hash << 6) + (hash << 16) - hash + c;
  ```

---

## 6. Making Comments Precise and Compact

* Ngắn gọn, không mơ hồ.
* Tránh đại từ (it, this), viết rõ ràng.
* Dùng ví dụ input/output, nhất là corner case.
* Example:

  ```python
  # Cuts off at max chars, adds "..."
  def Truncate(text, max_chars): ...
  ```

---

## 7. Making Control Flow Easy to Read

* Quy tắc cho `if/else`: điều kiện rõ ràng, đơn giản.
* Trả về sớm (return early) để giảm nesting.
* Tránh `goto`, `do/while`.
* Example:

  ```python
  # Bad: nested
  if user:
      if user.is_active:
          return True
      else:
          return False

  # Better: return early
  if not user:
      return False
  return user.is_active
  ```

---

## 8. Breaking Down Giant Expressions

* Chia nhỏ biểu thức phức tạp.
* Dùng biến phụ để giải thích.
* Áp dụng luật De Morgan khi cần.
* Example:

  ```python
  # Hard to read
  if not (file_exists and not file_is_empty):

  # Better
  missing_or_empty = (not file_exists) or file_is_empty
  if missing_or_empty:
      ...
  ```

---

## 9. Variables and Readability

* Biến càng ít càng dễ đọc.
* Thu hẹp scope của biến.
* Ưu tiên biến chỉ gán 1 lần (write-once).
* Example:

  ```python
  # Bad: variable reused
  result = query_db()
  result = format(result)

  # Better: new variable
  raw_result = query_db()
  formatted = format(raw_result)
  ```

---

## 10. Extracting Unrelated Subproblems

* **Tách logic không liên quan** ra thành hàm/tiện ích.
* Tạo code tái sử dụng (utility function).
* Đơn giản hóa interface bằng cách tách riêng subproblem.
* Example:

  ```python
  # Before: all logic in one function
  def find_closest_location(user, locations):
      best_dist = 999999
      for loc in locations:
          dist = compute_distance(user, loc)   # subproblem
          if dist < best_dist:
              best_dist = dist
              best_loc = loc
      return best_loc
  ```

  ```python
  # After: extracted subproblem
  def distance_between(a, b): ...
  def find_closest_location(user, locations):
      return min(locations, key=lambda loc: distance_between(user, loc))
  ```

---

## 11. One Task at a Time

* **Mỗi hàm làm 1 việc.**
* Nhiệm vụ có thể rất nhỏ.
* Giúp code dễ test, dễ hiểu.
* Example:

  ```python
  # Before: mixes parsing + validation
  def get_user_id(data):
      id = int(data.split(",")[0])
      if id < 0:
          raise ValueError("Invalid id")
      return id

  # After: one task per function
  def parse_id(data): ...
  def validate_id(id): ...
  ```

---

## 12. Turning Thoughts into Code

* Viết code như “diễn giải suy nghĩ”.
* Mô tả logic bằng ngôn ngữ gần gũi.
* Dùng library có sẵn thay vì tự viết lại.
* Example:

  ```python
  # Thought: "pick emails from list of users"
  emails = [user.email for user in users if user.is_active]
  ```

---

## 13. Writing Less Code

* **Ít code hơn = ít bug hơn.**
* Không viết tính năng “chưa chắc cần”.
* Hãy đặt câu hỏi về yêu cầu, tận dụng thư viện.
* Example:

  ```bash
  # Instead of coding file search...
  grep "keyword" *.txt
  ```

---

Ok, mình làm nốt **Phần 4 – Selected Topics (chương 14 → 15)** để hoàn tất cuốn sách.

---

## 14. Testing and Readability

* Test cũng phải **dễ đọc, dễ maintain**.
* Tránh test dài dòng, khó hiểu.
* Đặt tên test rõ ràng, dễ đoán behavior.
* Dùng input “có ý nghĩa” thay vì random.
* Error message phải dễ debug.
* Example:

  ```python
  # Bad
  def test_1():
      assert f(123, 5) == 345

  # Better
  def test_add_offset_to_id():
      assert f(user_id=123, offset=5) == 345
  ```

---

## 15. Designing and Implementing a “Minute/Hour Counter”

* Một bài tập lớn để minh họa cách thiết kế code dễ đọc.
* 3 hướng giải quyết:

  1. **Naive** → đơn giản nhưng khó scale.
  2. **Conveyor Belt Design** → lưu sự kiện theo timeline.
  3. **Time-Bucketed Design** → chia sự kiện thành bucket (phút/giờ).
* Bài học: giải pháp rõ ràng, dễ maintain thường tốt hơn “hack nhanh”.
* Example (Python pseudo):

  ```python
  class MinuteHourCounter:
      def __init__(self):
          self.minute_buckets = [0] * 60
          self.hour_buckets = [0] * 24

      def record_event(self, timestamp):
          self.minute_buckets[timestamp.minute] += 1
          self.hour_buckets[timestamp.hour] += 1
  ```

---
