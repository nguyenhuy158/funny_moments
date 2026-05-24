+++
date = '2026-05-24T10:34:07+07:00'
draft = false
title = '2 Tool Dọn Rác Cho Node.js Và Python'
author = []
description = "Hai CLI gọn nhẹ để dọn node_modules cũ, virtual environment Python và các thư mục cache chiếm dung lượng."
slug = "npkill-killpy"
summary = "Hai CLI nhỏ nhưng hữu ích: `npx npkill` để dọn `node_modules`, và `uvx killpy` để tìm rồi xóa virtual environment, cache Python đang ngốn ổ đĩa."
tags = ["nodejs", "python", "cli", "tool", "tip", "disk"]
+++

Nếu máy dev của bạn dùng cả **Node.js** lẫn **Python**, kiểu gì một ngày nào đó ổ đĩa cũng sẽ đầy bởi:

- `node_modules`
- `.venv`
- `__pycache__`
- cache của `poetry`, `pipx`, `uv`, `tox`...

Đây là 2 tool mình thấy rất đáng giữ trong đầu.

## 1. `npx npkill`

Khi bạn muốn tìm và xóa các thư mục `node_modules` cũ, `npkill` là lựa chọn cực nhanh:

```bash
npx npkill
```

Tool sẽ scan từ thư mục hiện tại, liệt kê các `node_modules`, kèm dung lượng để bạn chọn xóa ngay trong terminal.

Mình thích nó ở chỗ:

- không cần cài global
- nhìn được folder nào đang chiếm nhiều GB
- xóa tương tác, đỡ phải `find ... -exec rm -rf`

Nếu muốn quét một thư mục cụ thể:

```bash
npx npkill -d ~/Projects
```

## 2. `uvx killpy`

Nếu `npkill` là bản dọn rác cho Node.js, thì `killpy` là bản tương tự cho hệ sinh thái Python:

```bash
uvx killpy --path ~
```

`killpy` có thể tìm:

- `.venv`
- env của `poetry`
- env của `conda`
- env của `pipenv`, `pipx`, `pyenv`, `uv`
- cache như `__pycache__`, `.pytest_cache`, `.mypy_cache`

Điểm hay là nó gom mọi thứ vào một chỗ, thay vì bạn phải nhớ từng path lẻ tẻ trong home directory.

Nếu chỉ muốn scan thư mục hiện tại:

```bash
uvx killpy
```

## Khi nào nên dùng?

Mình thường chạy:

- `npx npkill` khi thấy repo Node.js cũ ngốn quá nhiều dung lượng
- `uvx killpy --path ~` mỗi khi muốn tổng vệ sinh môi trường Python trên máy

Đây đều là kiểu tool:

- chạy một lần là đủ
- không cần cài permanent
- rất hợp cho mấy lần "ổ cứng đầy mà không biết vì sao"

Nếu bạn code đa ngôn ngữ, nhớ 2 lệnh này là đủ cứu được kha khá GB:

```bash
npx npkill
uvx killpy --path ~
```
