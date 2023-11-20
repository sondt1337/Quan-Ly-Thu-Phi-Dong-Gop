# Bài tập lớn IT3180 - Quản lý thu phí đóng góp
Phần mềm Quản lý thu phí và đóng góp cho Tổ dân phố 7 phường La Khê là một giải pháp quản lý hiện đại giúp tổ chức theo dõi thông tin cộng đồng và thu tiền một cách hiệu quả.

Với hơn 400 hộ gia đình, sinh viên thuê trọ và các khoản đóng góp đa dạng, phần mềm này giúp cán bộ kế toán lập danh sách, thu phí vệ sinh hàng năm và quản lý các đóng góp từ cộng đồng.

Nó cũng cung cấp các công cụ thống kê để nắm bắt tình hình tài chính và tăng cường tính minh bạch trong quản lý. Dự án này sẽ nâng cao quản lý tổ dân phố thông qua công nghệ thông tin và hiệu quả hóa quy trình quản lý tài chính.
## Thành viên nhóm 3
| Thành viên                                              | MSSV     | Vai trò     | Nhiệm vụ           |
| ------------------------------------------------------- | -------- | ----------- | ------------------ |
| [Đinh Thái Sơn](https://github.com/vepiot/)             | 20210750 | Trưởng nhóm | Backend, Frontend  |
| [Bùi Văn Huy](https://github.com/buiihuy)               | 20210443 | Phó nhóm    | Frontend           |
| [Phạm Quang Huy](https://github.com/Huygiauten)         | 20210448 |             | Frontend           |
| [Trần Ngọc Bảo](https://github.com/TranNgocBao12062003) | 20215529 |             | Frontend           |
| [Vũ Minh Hiển](https://github.com/Minh-Hien2904)        | 20210324 |             | Report             |
## Giới thiệu
## Cài đặt
1. Tải repository
```
git clone https://github.com/vepiot/Quan-Ly-Thu-Phi-Dong-Gop.git
```
2. Tải thư viện Django
```
pip install django
```
## Chạy phần mềm
1. Chạy phần mềm
```
python manage.py runserver
```
Ứng dụng sẽ được chạy ở [http://localhost:3000](http://localhost:3000)
## DEMO
1. Sản phẩm demo: [DEMO](https://projectnmcnpm--sondt210750.repl.co/)
2. Tài khoản thường
Người dùng có thể tự tạo tài khoản ở phần Đăng ký

![image](https://hackmd.io/_uploads/HJ8eAmYN6.png)

3. Tài khoản ADMIN (Đăng nhặp tại [ADMIN](https://projectnmcnpm--sondt210750.repl.co/admin)):
- Tên tài khoản: `admin`
- Mật khẩu: `admin123`
### Giới thiệu phần mềm
Phần mềm quản lý thu phí đóng góp cho tổ dân phố là một ứng dụng Web chạy bởi backend là [Django](https://www.djangoproject.com/start/overview/)

Trang quản trị Django: 

![image](https://hackmd.io/_uploads/ryiPimYNp.png)