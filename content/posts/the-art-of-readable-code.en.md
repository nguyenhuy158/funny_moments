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

---

# 📖 Summary of *The Art of Readable Code*

## 1. Code Should Be Easy to Understand

* **Key Idea:** Minimize *time-till-understanding*.
* Readable code is more important than short code.
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
* Use specific and concrete words.
* Attach units or attributes if critical.
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

* Avoid ambiguous names.
* Use `min_`/`max_` for limits, `first/last` for inclusive ranges, `begin/end` for inclusive-exclusive ranges.
* Boolean names should use `is_`, `has_`, `can_`.
* Example:

  ```python
  # Bad
  read_password = True   # unclear meaning

  # Better
  need_password = True
  ```

---

## 4. Aesthetics

* Code should **look clean**.
* Rules: consistent layout, make similar code look similar, group related lines.
* Use helper methods to simplify long or repetitive test cases.
* Example:

  ```cpp
  // Before
  assert(ExpandFullName("Doug Adams") == "Mr. Douglas Adams");
  assert(ExpandFullName("No Such Guy") == "");

  // After
  CheckFullName("Doug Adams", "Mr. Douglas Adams", "");
  CheckFullName("No Such Guy", "", "no match found");
  ```

---

## 5. Knowing What to Comment

* Comments should explain **why**, not repeat **what**.
* Avoid obvious comments.
* Write notes that help future readers understand faster.
* Example:

  ```cpp
  // Fast version of "hash = (65599 * hash) + c"
  hash = (hash << 6) + (hash << 16) - hash + c;
  ```

---

## 6. Making Comments Precise and Compact

* Keep comments short and exact.
* Avoid vague pronouns (“it”, “this”).
* Provide input/output examples, especially edge cases.
* Example:

  ```python
  # Cuts off at max characters and appends "..."
  def Truncate(text, max_chars): ...
  ```

---

## 7. Making Control Flow Easy to Read

* Write `if/else` in a clear order.
* Return early to reduce nesting.
* Avoid `goto` and `do/while` loops.
* Example:

  ```python
  # Nested
  if user:
      if user.is_active:
          return True
      else:
          return False

  # Return early
  if not user:
      return False
  return user.is_active
  ```

---

## 8. Breaking Down Giant Expressions

* Split long expressions into smaller pieces.
* Use helper variables.
* Apply De Morgan’s laws to simplify.
* Example:

  ```python
  # Hard to read
  if not (file_exists and not file_is_empty):

  # Clearer
  missing_or_empty = (not file_exists) or file_is_empty
  if missing_or_empty:
      ...
  ```

---

## 9. Variables and Readability

* Fewer variables = easier to read.
* Minimize scope of variables.
* Prefer write-once variables.
* Example:

  ```python
  # Bad: reusing variable
  result = query_db()
  result = format(result)

  # Better
  raw_result = query_db()
  formatted = format(raw_result)
  ```

---

## 10. Extracting Unrelated Subproblems

* Separate unrelated logic into helper functions.
* Makes code reusable and simplifies main functions.
* Example:

  ```python
  # Before
  def find_closest_location(user, locations):
      best_dist = float("inf")
      for loc in locations:
          dist = compute_distance(user, loc)
          if dist < best_dist:
              best_dist = dist
              best_loc = loc
      return best_loc
  ```

  ```python
  # After
  def distance_between(a, b): ...
  def find_closest_location(user, locations):
      return min(locations, key=lambda loc: distance_between(user, loc))
  ```

---

## 11. One Task at a Time

* Each function should do **only one job**.
* Small tasks are easier to test and maintain.
* Example:

  ```python
  # Before: parsing + validation together
  def get_user_id(data):
      id = int(data.split(",")[0])
      if id < 0:
          raise ValueError("Invalid id")
      return id

  # After: separated
  def parse_id(data): ...
  def validate_id(id): ...
  ```

---

## 12. Turning Thoughts into Code

* Write code that mirrors your thought process.
* Use expressive language and libraries.
* Example:

  ```python
  # Thought: "get active users' emails"
  emails = [user.email for user in users if user.is_active]
  ```

---

## 13. Writing Less Code

* Less code = fewer bugs.
* Don’t implement unnecessary features.
* Reuse libraries and tools.
* Example:

  ```bash
  # Instead of writing custom file search
  grep "keyword" *.txt
  ```

---

## 14. Testing and Readability

* Tests must be readable and maintainable.
* Use meaningful inputs.
* Write descriptive test names.
* Error messages should be clear.
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

* Example problem: count events by minute/hour.
* Three design approaches:

  1. **Naive solution** – simple but inefficient.
  2. **Conveyor belt design** – shift events forward.
  3. **Time-bucketed design** – divide into fixed buckets.
* Lesson: clear and maintainable design beats quick hacks.
* Example (simplified):

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
