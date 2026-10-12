# Hướng Dẫn Chi Tiết Dự Án Hoạt Họa Manim - Tối Ưu Danh Mục Đầu Tư (FaMI)

Dự án này sử dụng thư viện **Manim (Mathematical Animation Engine)** kết hợp với hệ thống **Voiceover (lồng tiếng bằng gTTS)** để tạo ra một video hoạt họa giáo dục ngắn (dạng dọc - Vertical Video 1080x1920) nhằm giải thích các khái niệm trong **Lý thuyết Danh mục Đầu tư Hiện đại (Modern Portfolio Theory)** của nhà kinh tế học **Harry Markowitz**.

Video tập trung giải thích cách đa dạng hóa đầu tư giữa hai cổ phiếu **CTG** (VietinBank) và **FPT** (Tập đoàn FPT) để giảm thiểu rủi ro bằng cách sử dụng các công cụ thống kê như **Tỷ suất sinh lợi trung bình (Mean Return)**, **Độ lệch chuẩn (Standard Deviation)** và **Hiệp phương sai (Covariance)**.

---

## 1. Cấu Trúc Toàn Bộ Dự Án

Dưới đây là sơ đồ tóm tắt cấu trúc các file trong dự án:

```
videoxstk3/
│
├── video_3_main.py         # Điểm khởi chạy chính (Entrypoint)
├── config.py               # Cấu hình hằng số, màu sắc, lời thoại và phụ đề
├── base_scene.py           # Class nền tảng quản lý logo, âm thanh và phụ đề tự động dịch
├── helpers.py              # Các hàm tiện ích dựng giao diện (UI Helpers)
│
├── scene_s1.py -> s9.py    # Các phân đoạn cảnh (Scenes) cấu thành nên video
│
├── asset/                  # Thư mục chứa các file vector SVG trang trí
├── audio/                  # Thư mục lưu trữ các file âm thanh TTS được tự động tạo (.mp3)
├── stock/                  # Thư mục chứa logo của các cổ phiếu phụ (MSN, SSI, HPG, v.v.)
│
├── CTG_FPT_2025.csv        # Dữ liệu giá cổ phiếu lịch sử đầu vào
├── ctg.png, fpt.png        # Logo của hai cổ phiếu chính
├── fami_logo_transparent.png # Logo kênh giáo dục FaMI
│
├── test_layout.py          # Script chạy thử để kiểm tra bố cục hiển thị
└── fix.py, revert.py       # Các script hỗ trợ refactor code nhanh
```

---

## 2. Giải Thế Chi Tiết Ý Nghĩa Của Từng Code File

### 2.1. `video_3_main.py` (File Khởi Chạy Chính)
* **Ý nghĩa:** Đây là file tập hợp tất cả các phân đoạn (scenes) để dựng nên video hoàn chỉnh.
* **Cách hoạt động:**
  * Kế thừa từ `LoanDecisionTreeBase` (class nền trong `base_scene.py`) và nạp các **Mixin class** đại diện cho từng cảnh từ `scene_s1` đến `scene_s9`.
  * Hàm `construct()` sẽ gọi tuần tự các hàm cảnh: `self.scene_intro()`, `self.scene_problem()`, ..., `self.scene_question()`.
  * Gọi hàm `generate_audio()` từ `config.py` trước khi render để đảm bảo tất cả lời thoại đã được chuyển thành file âm thanh.
* **Câu lệnh render video chất lượng cao:**
  ```bash
  manim -qh video_3_main.py LoanDecisionTree
  ```
  *(Lưu ý: Tên class là `LoanDecisionTree` do kế thừa cấu trúc từ bài học trước, nhưng nội dung đã được cập nhật thành tối ưu danh mục đầu tư).*

### 2.2. `config.py` (Cấu Hình Hệ Thống)
* **Ý nghĩa:** Chứa toàn bộ hằng số cấu hình của video để đảm bảo tính nhất quán (Brand Identity).
* **Các thành phần quan trọng:**
  * **Kích thước khung hình:** Thiết lập tỉ lệ dọc `1080x1920` phù hợp cho điện thoại (Shorts/TikTok/Reels).
  * **Hệ màu sắc thương hiệu FaMI:** Khai báo các mã màu chính như xanh lam (`FAMI_BLUE`), xanh ngọc (`FAMI_CYAN`), vàng phụ đề (`FAMI_SUB`), đỏ cảnh báo (`C_DANGER`), xanh lá thành công (`C_SUCCESS`).
  * **Hệ tọa độ khóa cứng (FaMI Layout System):** Định vị cố định vị trí các phần tử trên màn hình dọc để tránh đè chữ (Tiêu đề `POS_TITLE`, Nội dung chính `POS_CENTER`, Phụ đề `POS_SUBTITLE`).
  * **Từ điển `SCRIPTS`:** Chứa kịch bản lời thoại tiếng Việt bằng chữ để công cụ Text-to-Speech (TTS) đọc.
  * **Từ điển `SUBS`:** Định nghĩa phụ đề song ngữ Anh - Việt sẽ xuất hiện khớp với lời thoại và thời lượng hiển thị cụ thể.
  * **Hàm `generate_audio()`:** Tự động gọi thư viện `gtts` để chuyển đổi toàn bộ văn bản trong `SCRIPTS` thành file âm thanh giọng đọc tiếng Việt lưu vào thư mục `/audio`.

### 2.3. `base_scene.py` (Class Nền Tảng)
* **Ý nghĩa:** Định nghĩa class base `LoanDecisionTreeBase` kế thừa từ `VoiceoverScene` để điều khiển phụ đề, logo và luồng chạy chung.
* **Các tính năng nổi bật:**
  * **Tự động dịch:** Khi có phụ đề tiếng Việt, class sử dụng thư viện `googletrans` để tự động dịch sang tiếng Anh nếu không khai báo thủ công.
  * **Đa dạng kiểu dáng phụ đề (Styles):** Cung cấp các giao diện phụ đề như `neon` (chữ phát sáng), `banner` (dải xanh chạy ngang màn hình), `minimal` (chữ đổ bóng), `cinema` (khung xám bo góc tròn).
  * **Hàm `create_title()`:** Tạo tiêu đề tự động áp dụng dải màu gradient từ Xanh ngọc sang Xanh lam đặc trưng của thương hiệu.
  * **Hàm `clear_content()`:** Làm mờ dần và ẩn toàn bộ các đối tượng hình vẽ trên màn hình để chuyển cảnh, nhưng giữ lại Logo cố định ở trên và thanh phụ đề ở dưới.
  * **Hàm `sp()` (Super Play):** Thay thế cho `self.play()` của Manim. Hàm này tự động phát âm thanh "pop" khi xuất hiện đối tượng mới và tự động đưa các lớp giao diện quan trọng (Logo, phụ đề) lên trên cùng để tránh bị hình vẽ khác đè mất.

### 2.4. `helpers.py` (Hàm Hỗ Trợ Giao Diện UI)
* **Ý nghĩa:** Đóng vai trò là bộ công cụ vẽ nhanh các đối tượng đồ họa lặp đi lặp lại trong video để code chính ở các scene ngắn gọn và dễ bảo trì hơn.
* **Các hàm quan trọng:**
  * `skill_pop_in()`: Tạo hiệu ứng zoom và nảy nhẹ (Ease Out Back) khi xuất hiện đối tượng giúp video sinh động hơn.
  * `rnode()`: Tạo một thẻ hình chữ nhật bo góc với nhãn chữ được căn giữa tự động.
  * `info_card()`: Vẽ một hộp chứa thông tin có tiêu đề, nội dung và thanh màu chủ đề phía trên.
  * `load_icon()`: Tìm và tải một biểu tượng SVG tương ứng trong thư mục `asset/` (Ví dụ: icon túi tiền, icon khiên bảo vệ, biểu đồ...). Nếu không tìm thấy file SVG trên hệ thống, hàm sẽ tự động tạo một vòng tròn chứa ký tự chữ tương ứng để làm phương án dự phòng (fallback).
  * `flow_block()`: Tạo các khối biểu diễn quy trình xử lý thông tin.

### 2.5. Các Phân Cảnh Nội Dung (`scene_s1.py` đến `scene_s9.py`)

Mỗi file mixin đảm nhận hiển thị một cảnh quay kéo dài từ 5 - 15 giây phù hợp với nhịp điệu giọng đọc:

* **`scene_s1.py` (Cảnh 1 - Dẫn nhập):**
  * Minh họa bài toán cốt lõi: Làm sao phân bổ danh mục đầu tư để vừa đạt **Lợi nhuận** (Profit - nhánh màu xanh lá bên trái) vừa kiểm soát **Rủi ro** (Risk - nhánh màu đỏ bên phải).
  * Nhúng hình ảnh đồ thị giá cổ phiếu bằng file SVG.
* **`scene_s2.py` (Cảnh 2 - Giả thuyết bài toán):**
  * Mô tả bạn là nhà đầu tư có số vốn **100 triệu VNĐ** và đang cân nhắc hai mã cổ phiếu tiềm năng là **CTG** và **FPT**.
  * Vẽ đồ thị xu hướng giá đi lên và hiển thị logo 2 công ty.
* **`scene_s3.py` (Cảnh 3 - Dữ liệu lịch sử):**
  * Tạo một bảng dữ liệu (`Table`) biểu diễn giá đóng cửa và tỷ suất sinh lợi thực tế trong 5 tháng gần nhất của CTG và FPT.
  * Hiển thị công thức và cách tính **tỷ suất sinh lợi trung bình** dưới dạng phân số. Kết quả: CTG đạt **5.39%** (cao hơn) còn FPT đạt **0.89%**.
* **`scene_s4.py` (Cảnh 4 - Tâm lý đám đông & Rủi ro):**
  * Giải thích tâm lý thông thường sẽ dồn 100% vốn vào CTG vì lợi nhuận cao hơn.
  * Xuất hiện cảnh báo màu đỏ chói cảnh báo về mặt Rủi ro nếu không đa dạng hóa vốn.
* **`scene_s5.py` (Cảnh 5 - Lý thuyết Markowitz & Hiệp phương sai):**
  * Giới thiệu Lý thuyết Danh mục Đầu tư Hiện đại của Harry Markowitz.
  * Trình bày công thức tính **Độ lệch chuẩn ($\sigma$)** đại diện cho biến động rủi ro của từng cổ phiếu (CTG là 6.73%, FPT là 7.37%).
  * Giới thiệu khái niệm **Hiệp phương sai (Covariance)** để xem hai cổ phiếu này biến động cùng nhau ra sao. Hiển thị bảng ý nghĩa ($>0$ cùng chiều, $<0$ ngược chiều). Kết quả tính ra số âm: **-10.48** (biến động lệch pha nhau, có lợi cho việc đa dạng hóa).
* **`scene_s6.py` (Cảnh 6 - Phương sai danh mục đầu tư):**
  * Đưa ra công thức tính phương sai danh mục đầu tư 2 tài sản:
    $$Var(P) = w_{CTG}^2 \cdot \sigma_{CTG}^2 + w_{FPT}^2 \cdot \sigma_{FPT}^2 + 2 \cdot w_{CTG} \cdot w_{FPT} \cdot Cov(CTG, FPT)$$
  * Chứng minh toán học: Nếu chia tỷ trọng **60% CTG và 40% FPT**, rủi ro danh mục (độ lệch chuẩn $\sigma_p$) giảm xuống chỉ còn **4.47%** (nhỏ hơn hẳn mức rủi ro riêng lẻ là 6.73% và 7.37%).
* **`scene_s7.py` (Cảnh 7 - Đa dạng hóa & Mở rộng):**
  * So sánh trực quan Phương án 1 (100% CTG) và Phương án 2 (60% CTG - 40% FPT) bằng hiệu ứng lật thẻ 3D.
  * Vẽ biểu đồ **Đường biên hiệu quả (Efficient Frontier)** - đường cong biểu diễn các tập hợp danh mục tối ưu.
  * Đưa ra công thức mở rộng dạng ma trận cho $n$ tài sản: $\sigma_p^2 = w^T \Sigma w$, trong đó minh họa chi tiết Vector trọng số $w$ và Ma trận hiệp phương sai $\Sigma$ với các dấu ba chấm được dựng thủ công bằng các đối tượng điểm tròn (`Dot`) của Manim.
* **`scene_s8.py` (Cảnh 8 - Tổng kết):**
  * Tóm tắt lại 3 khái niệm cốt lõi đã học: Hiệp phương sai, Phương sai danh mục đầu tư, Đa dạng hóa đầu tư theo mô hình Markowitz.
* **`scene_s9.py` (Cảnh 9 - Tương tác & Kết thúc):**
  * Đặt câu hỏi kích thích thảo luận dưới phần bình luận của người xem: *"Nếu thêm cổ phiếu C tương quan âm với CTG, danh mục đầu tư có an toàn hơn không?"*
  * Hiển thị lời kêu gọi Like, Đăng ký (Theo dõi) kèm hiệu ứng xoay và hiện logo thương hiệu FaMI ở cuối cùng.

---

## 3. Các Công Cụ Dùng Để Tinh Chỉnh & Sửa Lỗi

* **`test_layout.py`:**
  * Đây là một script phụ rút gọn. Thay vì phải render toàn bộ video 9 cảnh rất mất thời gian, lập trình viên sử dụng file này để render nhanh một cảnh tĩnh duy nhất của bảng số liệu Cảnh 3. Mục đích là để căn chỉnh khoảng cách các hàng, cỡ chữ, và căn chỉnh phân số sao cho đẹp mắt nhất.
* **`fix.py` / `revert.py`:**
  * Các file script tự động hóa dùng để thực hiện nhanh thao tác tìm kiếm và thay thế (Search & Replace) hàng loạt chuỗi ký tự trong mã nguồn khi cần cập nhật một thay đổi lớn về thư viện (ví dụ như thay đổi cách render chữ viết xuống dòng từ `Paragraph` sang `MarkupText`).

---

## 4. Ý Nghĩa Kinh Tế / Giáo Dục Của Kịch Bản

Video truyền tải một thông điệp vô cùng quan trọng trong đầu tư: **"Không nên bỏ tất cả trứng vào một giỏ"**.
Bằng cách chứng minh trực quan bằng các con số thực tế:
* CTG có lợi nhuận $5.39\%$ (Rủi ro $6.73\%$).
* FPT có lợi nhuận $0.89\%$ (Rủi ro $7.37\%$).
* Khi kết hợp chúng với tỷ lệ $60/40$, vì hai cổ phiếu này có mối tương quan âm (hiệp phương sai là $-10.48$), chúng sẽ triệt tiêu biến động cho nhau.
* Kết quả là danh mục đầu tư chung có rủi ro chỉ còn **$4.47\%$** (thấp hơn nhiều so với việc đầu tư riêng lẻ vào bất kỳ cổ phiếu nào), trong khi vẫn giữ được mức lợi nhuận trung bình khá tốt ($3.59\%$).

---

## 5. Giải Thích Chi Tiết Các Đoạn Code Trong Các File Cảnh (Scene_s1 -> Scene_s9)

Các file cảnh từ `scene_s1.py` đến `scene_s9.py` được thiết kế dưới dạng các **Mixin Class** (ví dụ: `SceneIntroMixin`, `SceneProblemMixin`). Cách thiết kế này cho phép tách mã nguồn thành các module nhỏ, giúp dễ quản lý và bảo trì.

Dưới đây là phân tích chi tiết cấu trúc code và các dòng lệnh tiêu biểu được sử dụng trong các file cảnh:

### 5.1. Khởi tạo đối tượng đồ họa (Mobjects)
Trước khi bắt đầu các hiệu ứng hoạt họa, mỗi cảnh sẽ khởi tạo tiêu đề và các thành phần giao diện cần thiết:
* **Tiêu đề cảnh:** `ttl = self.create_title("Tiêu đề")` (tự động căn vị trí `POS_TITLE` và áp dụng màu dải chuyển sắc Cyan -> Blue).
* **Hình ảnh & SVG:**
  * `SVGMobject("asset/...")`: Tải các file hình ảnh vector để vẽ các minh họa không bị vỡ nét (ví dụ: hình người đầu tư, đồ thị giá cổ phiếu).
  * `ImageMobject("ctg.png").scale_to_fit_width(0.8)`: Nhúng và thu nhỏ hình ảnh bitmap (như logo CTG, FPT) để làm biểu tượng trực quan.

### 5.2. Khối lệnh đồng bộ giọng nói và phụ đề (`with self.voiceover`)
Đây là trái tim của việc tạo video có thuyết minh đồng bộ:
```python
part1_script = "Làm thế nào để có thể xây dựng một danh mục đầu tư"
with self.voiceover(text=part1_script) as tracker:
    self.update_subtitle("Làm thế nào để có thể xây dựng\nmột danh mục đầu tư", style="default")
    self.sp(Write(q, run_time=min(1.0, tracker.duration * 0.5)))
    self.wait(max(0.1, tracker.duration - 1.8))
```
* **`self.voiceover(text=...)`**: Đọc lời thoại dựa trên công cụ TTS tiếng Việt.
* **`tracker.duration`**: Đo thời gian thực tế của giọng nói phát ra. Nhờ giá trị này, các hiệu ứng hình ảnh (`run_time=...`) và thời gian chờ (`self.wait(...)`) được tính toán động để khớp hoàn toàn với lời thoại, tránh trường hợp hình chạy trước tiếng hoặc tiếng nói xong rồi hình mới bắt đầu chạy.
* **`self.update_subtitle(...)`**: Hiển thị phụ đề tương ứng dưới chân màn hình (`POS_SUBTITLE`).

### 5.3. Các lệnh hoạt họa tiêu biểu và ý nghĩa
Trong các file scene, bạn sẽ thấy rất nhiều hiệu ứng hoạt họa của Manim:

* **`skill_pop_in(mobject, sound=True)`**:
  * *Ý nghĩa:* Xuất hiện vật thể kèm hiệu ứng nảy nhẹ (Ease Out Back) và phát âm thanh "pop" vui tai.
  * *Ứng dụng:* Dùng khi hiển thị các logo cổ phiếu, các thẻ kết quả tính toán hoặc biểu tượng cảnh báo rủi ro để tăng sự chú ý của người xem.
* **`ReplacementTransform(A, B)`**:
  * *Ý nghĩa:* Biến đổi vật thể A thành vật thể B một cách trơn tru tại chỗ.
  * *Ứng dụng:* 
    * Trong `scene_s3.py`, biến đổi biểu tượng cơ sở dữ liệu (`center_db_icon`) thành các đường lưới của bảng lịch sử (`grid`).
    * Trong `scene_s6.py`, biến công thức toán học chữ thành công thức chứa số, rồi từ công thức số co cụm lại thành kết quả cuối cùng (`Var(P) = 19.97`).
* **`Rotate(mobject, angle=2*PI, axis=UP)`**:
  * *Ý nghĩa:* Xoay vật thể 360 độ quanh trục thẳng đứng, tạo cảm giác giống như lật một tấm thẻ 3D.
  * *Ứng dụng:* Sử dụng trong `scene_s7.py` khi giới thiệu hai phương án đầu tư PA1 và PA2 để tạo điểm nhấn thị giác cao cấp.
* **`Indicate(mobject, color=...)` và `Wiggle(mobject)`**:
  * *Ý nghĩa:* Rung lắc nhẹ (`Wiggle`) hoặc làm đối tượng sáng bừng lên/phóng to thu nhỏ tạm thời (`Indicate`).
  * *Ứng dụng:* Nhấn mạnh khi giọng đọc nhắc tới một con số cụ thể (như lợi nhuận, rủi ro) hoặc các trục tọa độ khi phân tích đồ thị.
* **`ParametricFunction`**:
  * *Ý nghĩa:* Vẽ đồ thị dựa trên phương trình toán học tham số thực tế.
  * *Ứng dụng:* Trong `scene_s7.py`, dùng để vẽ chính xác **Đường biên hiệu quả (Efficient Frontier)** - một đường cong C-shape phản ánh các tổ hợp đầu tư tối ưu Markowitz:
    ```python
    curve_func = lambda u: ax.c2p(2.0 + 0.15 * (u - 3.0)**2, u, 0)
    ```
    Hàm này ánh xạ giá trị toán học $(x, y)$ vào hệ tọa độ của màn hình Manim để vẽ nhánh hiệu quả màu xanh (`efficient_curve`) và nhánh kém hiệu quả màu xám (`inefficient_curve`).
* **`clear_content(t=0.8)`**:
  * *Ý nghĩa:* Thực hiện Fade Out (biến mất dần) toàn bộ các phần tử nội dung đang có trên màn hình, di chuyển nhẹ xuống dưới.
  * *Ứng dụng:* Luôn nằm ở cuối mỗi file scene để dọn dẹp màn hình, chuẩn bị không gian trống cho phân cảnh tiếp theo, ngoại trừ Logo thương hiệu ở trên cùng và Phụ đề ở dưới cùng được giữ lại để tạo sự liên tục.

