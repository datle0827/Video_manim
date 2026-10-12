# FaMI - Video Series Xác Suất Thống Kê (Manim)

Repository tổng hợp mã nguồn render video diễn giải toán học & ứng dụng kinh tế/tài chính thuộc dự án **FaMI 1956**, sử dụng thư viện **Manim Community Edition** và **gTTS** (Google Text-to-Speech).

---

## 📂 Danh Sách Các Video Trong Series

| Thư mục | Chủ đề | Kịch bản / Nội dung chính |
| :--- | :--- | :--- |
| **`video_1/`** | **Xác suất phê duyệt khoản vay** | Mô hình Cây quyết định (Decision Tree), xác suất có điều kiện |
| **`video_2/`** | **Kiểm soát chất lượng sản phẩm** | Biến ngẫu nhiên rời rạc, kỳ vọng $E(X)$, phương sai $Var(X)$, bài toán chi phí QA |
| **`video_3/`** | **Tối ưu danh mục đầu tư** | Hiệp phương sai (Covariance), độ lệch chuẩn $\sigma$, đa dạng hóa danh mục Markowitz |
| **`video_4/`** | **Phát hiện điểm dữ liệu bất thường** | Điểm ngoại lai (Outliers), chỉ số đòn bẩy (Leverage $h_i$), ảnh hưởng mô hình hồi quy |

---

## 🚀 Cài Đặt Môi Trường

Khuyến nghị sử dụng **Python 3.10 - 3.12**:

```bash
# 1. Clone repository
git clone https://github.com/<your-username>/fami-videoxstk.git
cd fami-videoxstk

# 2. Tạo và kích hoạt môi trường ảo (khuyên dùng)
python -m venv .venv
# Trên Windows PowerShell:
.venv\Scripts\Activate.ps1

# 3. Cài đặt các thư viện phụ thuộc
pip install -r requirements.txt
```

> **Lưu ý về FFmpeg:** Manim yêu cầu hệ thống đã cài đặt FFmpeg. Hãy đảm bảo lệnh `ffmpeg -version` hoạt động trên máy của bạn.

---

## 🎬 Hướng Dẫn Render Video

Bạn có thể chạy video theo 2 cách cực kỳ linh hoạt:

### Cách 1: Sử dụng Runner tổng hợp từ thư mục gốc (Tiện lợi nhất)

```bash
# Xem danh sách video
python run.py --list

# Render Video 1 chất lượng cao (1080p)
python run.py 1

# Render Video 3 thử nghiệm nhanh (chất lượng 480p15)
python run.py 3 -ql

# Render Video 4 và dọn sạch cache
python run.py 4 -ql --flush_cache

# Chỉ tự động sinh giọng đọc TTS cho Video 2
python run.py 2 --audio
```

### Cách 2: Vào từng thư mục con để chạy Manim độc lập

Mỗi thư mục video hoàn toàn độc lập, bạn có thể `cd` vào thư mục bất kỳ để thao tác:

```bash
cd video_3

# Sinh giọng đọc TTS (nếu cần cập nhật kịch bản)
python video_3_main.py

# Render video chất lượng cao
manim -qh video_3_main.py LoanDecisionTree

# Hoặc render nhanh chất lượng thấp
manim -ql video_3_main.py LoanDecisionTree
```

---

## ⚙️ Cấu Trúc Mỗi Thư Mục Video Con

```text
video_X/
├── config.py                 # Kịch bản lời thoại, phụ đề, tọa độ UI, màu sắc nhận diện FaMI
├── base_scene.py             # Lớp nền (setup logo, căn phụ đề tự động, quản lý âm thanh)
├── helpers.py                # Các hàm vẽ component, UI cards, node bo góc, load icon SVG
├── video_3_main.py           # Entry point kết hợp tất cả các scene mixin
├── scene_s1.py, s2.py...     # Mã nguồn diễn hoạt chi tiết từng phân cảnh
├── audio/                    # File âm thanh giọng đọc TTS (.mp3)
└── asset/                    # Các file icon SVG, ảnh minh họa (nếu có)
```

---

## 📦 Đẩy Lên GitHub Lần Đầu

```bash
git init
git add .
git commit -m "feat: initial commit for FaMI videoxstk series"
git branch -M main
git remote add origin https://github.com/<your-username>/fami-videoxstk.git
git push -u origin main
```
