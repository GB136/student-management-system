# Student Management System

## Thông tin cá nhân

* **Họ và tên:** Lê Gia Bảo
* **MSSV:** 23720061
* **Ngành học:** Data Science

---

## Giới thiệu dự án

Đây là một hệ thống **quản lý sinh viên** được xây dựng bằng **FastAPI (Backend)** và **ReactJS (Frontend)**.

Ứng dụng cho phép quản lý thông tin sinh viên bao gồm:

* Thêm sinh viên
* Xem danh sách sinh viên
* Cập nhật thông tin sinh viên
* Xóa sinh viên
* Tìm kiếm sinh viên theo tên
* Thống kê dữ liệu sinh viên
* Xuất dữ liệu ra file CSV

Mục tiêu của dự án là thực hành xây dựng **ứng dụng web full-stack** kết nối giữa frontend và backend thông qua API.

---

## Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* SQLite

### Frontend

* React JS
* Axios

### Database

* SQLite

---

## Tools sử dụng
* Chat GPT
* Git
* GitHub
* VS Code

---

## Kiến trúc hệ thống

Frontend (ReactJS)
↓ Gửi request API bằng Axios
Backend (FastAPI)
↓ ORM SQLAlchemy
SQLite Database

---

## Cấu trúc thư mục

```id="7rnh5d"
student-management-system
│
├── backend
│   ├── main.py
│   ├── crud.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│
├── frontend
│   ├── src
│   │   ├── pages
│   │   │   ├── StudentList.js
│   │   │   ├── AddStudent.js
│   │   │   └── Stats.js
│   │   ├── api.js
│   │   └── App.js
│
└── README.md
```

---

## Chức năng chính

### Quản lý sinh viên

* Thêm sinh viên mới
* Cập nhật thông tin sinh viên
* Xóa sinh viên
* Hiển thị danh sách sinh viên

### Tìm kiếm

* Tìm sinh viên theo tên

### Thống kê

* Tổng số sinh viên
* GPA trung bình
* Số lượng sinh viên theo ngành

### Xuất dữ liệu

* Xuất danh sách sinh viên ra file CSV

---

## Cách chạy dự án

### Chạy Backend

```id="37vtff"
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend sẽ chạy tại:

```id="r2kjdr"
http://127.0.0.1:8000
```

---

### Chạy Frontend

```id="8xd6d4"
cd frontend
npm install
npm start
```

Frontend sẽ chạy tại:

```id="rmn41e"
http://localhost:3000
```

---

## Log quá trình thực hiện

### Bước 1

* Thiết kế database cho hệ thống sinh viên và lớp học

### Bước 2

* Xây dựng API bằng FastAPI
* Thực hiện các chức năng CRUD

### Bước 3

* Xây dựng giao diện frontend bằng ReactJS
* Kết nối React với FastAPI bằng Axios

### Bước 4

* Thêm chức năng thống kê dữ liệu sinh viên

### Bước 5

* Thêm chức năng export dữ liệu ra CSV

### Bước 6

* Đưa project lên GitHub

---

## Hướng phát triển thêm

* Thêm chức năng đăng nhập (authentication)
* Cải thiện giao diện UI
* Thêm phân trang dữ liệu
* Triển khai lên cloud (Render / Vercel)

---

## Ghi chú

Dự án được thực hiện nhằm mục đích học tập và thực hành phát triển ứng dụng web full-stack.
