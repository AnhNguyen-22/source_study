# Student Management System

Hệ thống quản lý sinh viên sử dụng PyQt6 và MySQL.

## Yêu cầu hệ thống

- Python 3.8+
- MySQL Server
- PyQt6
- mysql-connector-python

## Cài đặt

1. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

2. Tạo database MySQL:
```sql
CREATE DATABASE studentmanagement;
USE studentmanagement;

CREATE TABLE student (
    idstudent INT AUTO_INCREMENT PRIMARY KEY,
    Code VARCHAR(10) NOT NULL,
    Name VARCHAR(100) NOT NULL,
    Age INT NOT NULL,
    Avatar VARCHAR(255),
    Intro TEXT
);
```

3. Cập nhật thông tin kết nối database trong file `StudentManagement.py`:
```python
self.server = "localhost"
self.port = 3306
self.database = "studentmanagement"
self.user = "root"
self.password = "your_password"
```

## Chạy ứng dụng

```bash
python StudentManagement.py
```

## Chức năng

- ✅ Xem danh sách sinh viên
- ✅ Thêm sinh viên mới
- ✅ Cập nhật thông tin sinh viên
- ✅ Xóa sinh viên
- ✅ Upload avatar
- ✅ Tìm kiếm và lọc dữ liệu

## Cấu trúc thư mục

```
01_10/
├── StudentManagement.py    # File chính
├── MainWindow.py          # Giao diện UI
├── Connect_SQL.py         # Kết nối database
├── requirements.txt       # Dependencies
├── README.md             # Hướng dẫn
└── images/               # Thư mục chứa ảnh
    └── ic_no_avatar.png  # Ảnh mặc định
```

## Lưu ý

- Đảm bảo MySQL server đang chạy
- Tạo thư mục `images` và thêm file `ic_no_avatar.png` nếu cần
- Kiểm tra quyền truy cập database

