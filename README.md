# ✍️ Trình Giả Lập Chép Tay Tiếng Trung Phồn Thể Trên Quyển Vở

Ứng dụng web chạy trực tiếp trên Windows, giúp tạo ảnh chữ viết tay tiếng Trung phồn thể siêu thực tế (bút bi gel đen, chữ hơi ngoáy tự nhiên, imperfect) được viết thẳng lên quyển vở kẻ ngang thực tế của bạn.

---

## 🌟 Các Tính Năng Nổi Bật

1. **Khớp Chuẩn Trang Vở Của Bạn**:
   - Sử dụng chính bức ảnh trang vở kẻ ngang Thành Nam của bạn làm phôi nền.
   - Tự động căn chỉnh 32 dòng kẻ ngang, căn mép vạch chỉ đỏ lề trái.
   - Chữ nằm tự nhiên trên dòng kẻ, có độ chạm nhẹ hoặc trôi dòng như người viết thật.

2. **Mô Phỏng Bút Bi Gel Đen Siêu Chân Thực ("Chữ ngoáy, hơi xấu")**:
   - **Độ ngoáy & run tay ngẫu nhiên**: Có thanh trượt từ Nắn nót (0%) đến Tự nhiên (50%) đến Rất ngoáy/ẩu (100%).
   - **Biến thiên từng ký tự**: Mỗi chữ Hán có góc nghiêng ngẫu nhiên (-4° đến +4°), độ trồi sụt dòng (jitter), độ to nhỏ và khoảng cách chữ không đều.
   - **Võng dòng tự nhiên**: Khi viết nhanh không có thước kẻ, dòng chữ hơi võng/lượn nhẹ theo bàn tay.
   - **Hòa trộn mực thực tế (Multiply Blend)**: Mực bút gel thấm vào thớ giấy, đè lên đường kẻ xanh và bóng mờ tự nhiên của trang giấy.

3. **Kho Phông Chữ Viết Tay Đa Dạng**:
   - `JasonHandwriting 3`: Bút gel viết nhanh, hơi ngoáy (Khuyên dùng).
   - `JasonHandwriting 5`: Ngoáy nhiều, phóng khoáng, hơi ẩu một chút.
   - `JasonHandwriting 1`: Bút bi học sinh nắn nót.
   - `Thần Vũ Lạc Nhạn (ChenYuluoyan)`: Nét thanh mảnh, sinh viên.
   - `Lưu Kiến Mao Thảo`, `Long Thương`, `Mã Sơn Chính`: Phong cách thảo thư, bút lông tự do.

4. **Đầu Vào Đa Năng**:
   - **Gõ / Dán văn bản phồn thể**: Hỗ trợ bài dài, tự động phân trang (Trang 1, Trang 2, Trang 3...).
   - **Nhận diện chữ từ ảnh (OCR)**: Kéo thả ảnh chụp tài liệu/bài tập hoặc bấm `Ctrl + V` để dán ảnh chụp màn hình trực tiếp. AI tự động đọc chữ phồn thể và điền vào vở.
   - **Chuyển Giản thể ➔ Phồn thể**: Tích hợp công cụ OpenCC chuyển đổi 1-click nhanh chóng.

5. **Xuất Ảnh Độ Nét Cao**:
   - Tải nhanh trang hiện tại (JPG sắc nét).
   - Đóng gói toàn bộ các trang thành file `ZIP` chỉ bằng 1 cú nhấp chuột.
   - Nút kết xuất ảnh siêu nét qua Python Pillow.

---

## 🚀 Hướng Dẫn Sử Dụng

### Cách 1: Khởi động nhanh
- Vào thư mục `chinese-handwriting-app`.
- Nhấp đúp chuột vào file **`start.bat`**.
- Trình duyệt sẽ tự động mở trang ứng dụng tại địa chỉ: `http://localhost:8088`.

### Cách 2: Chạy bằng dòng lệnh (PowerShell / Command Prompt)
```powershell
cd C:\Users\phucv\.gemini\antigravity\scratch\chinese-handwriting-app
python server.py
```

---

## ⌨️ Phím Tắt Tiện Lợi
- **Ctrl + V**: Dán ảnh chụp màn hình vào bất cứ lúc nào để quét chữ (OCR).
- **🎲 Đổi dáng chữ**: Bấm nút ở thanh trên cùng để đổi góc nghiêng và xô lệch ngẫu nhiên mới nếu chưa ưng ý dáng chữ hiện tại.
