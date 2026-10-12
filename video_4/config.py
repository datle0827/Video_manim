#!/usr/bin/env python3
"""
config.py – Hằng số, màu sắc, nội dung audio/phụ đề, và tiện ích audio.
"""

import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_DIR  = os.path.join(SCRIPT_DIR, "audio")
LOGO_PATH  = os.path.join(SCRIPT_DIR, "fami_logo_transparent.png")

# ─── Cấu hình video (FaMI Standard) ───────────────────────────────────────
VIDEO_W   = 1080
VIDEO_H   = 1920
FRAME_W   = 9.0
FRAME_H   = 16.0
BG_COLOR  = "#000000"
FONT      = "Arial"

# ─── Màu sắc (FaMI Brand Colors) ───────────────────────────────────────────
# Core FaMI colors
FAMI_BLUE  = "#005BAA"
FAMI_CYAN  = "#45C4D9"
FAMI_SUB   = "#DFE858"
ACCENT     = "#fffa65"
DANGER     = "#ff4d4d"
SUCCESS    = "#00e676"
TEXT_COLOR = "#FFFFFF"

# Compatibility with old color names
C_WHITE    = "#FFFFFF"
C_YELLOW   = "#FFD700"
C_PRIMARY  = "#3B82F6"
C_SUCCESS  = "#22C55E"
C_DANGER   = "#EF4444"
C_WARNING  = "#F59E0B"
C_PURPLE   = "#A855F7"
C_GRAY     = "#94A3B8"
C_DARK_BG  = "#111827"
C_INCOME_H = "#60A5FA"
C_INCOME_L = "#FB923C"
C_CREDIT_G = "#34D399"
C_CREDIT_A = "#F87171"
C_APPROVE  = "#4ADE80"
C_REJECT   = "#475569"

# ─── Hệ tọa độ khóa cứng (FaMI Layout System) ──────────────────────────────
POS_TITLE        = (0, 5.2, 0)      # Vị trí tiêu đề (cao nhất, ngay dưới Logo)
POS_TOP_FOCUS    = (0, 3.2, 0)      # Vùng trên (focus)
POS_CENTER       = (0, 1.5, 0)      # Tâm điểm chính
POS_BOTTOM_FOCUS = (0, -0.5, 0)     # Vùng dưới trong nội dung chính (focus)
POS_CTA          = (0, -3.2, 0)     # Vị trí dành cho chú thích, CTA
POS_SUBTITLE     = (0, -4.5, 0)     # Vị trí phụ đề (khóa cứng Y = -4.5)

# ─── Audio scripts (TTS tiếng Việt) ────────────────────────────────────────
SCRIPTS = {
    "s1": (
        "Liệu chỉ một điểm dữ liệu bất thường có thể làm thay đổi hoàn toàn kết quả của một mô hình dự báo?"
    ),
    "s2": (
        "Ở video trước, chúng ta đã sử dụng hồi quy để dự đoán giá nhà. Nhưng dữ liệu thực tế không phải lúc nào cũng hoàn hảo. "
        "Giả sử xuất hiện một giao dịch có diện tích chỉ 60 m² nhưng giá bán lên tới 10 tỷ đồng. "
        "Đây là một căn nhà đặc biệt, hay chỉ đơn giản là dữ liệu bất thường?"
    ),
    "s3": (
        "Trong thực tế, dữ liệu luôn tồn tại những quan sát khác biệt. Một số chỉ đơn giản là hiếm gặp. Nhưng một số khác lại có thể làm sai lệch toàn bộ mô hình."
    ),
    "s4": (
        "Outlier là những điểm dữ liệu nằm xa phần lớn các quan sát còn lại. "
        "Tuy nhiên, với bộ dữ liệu hàng triệu điểm, chúng ta không thể chỉ nhìn bằng mắt để kết luận một điểm là Outlier. "
        "Hôm nay, chúng ta sẽ tìm hiểu 2 phương pháp để hỗ trợ việc này là quy tắc 1.5IQR và Độ đo Leverage."
    ),
    "s5": (
        "Đầu tiên, chúng ta có thể sử dụng khoảng tứ phân vị IQR để phát hiện những giá trị bất thường trong phân bố dữ liệu. "
        "Khoảng tứ phân vị IQR được tính bằng hiệu giữa tứ phân vị thứ ba và thứ nhất. "
        "Một điểm được xem là Outlier nếu nhỏ hơn Q 1 trừ một phẩy năm IQR hoặc lớn hơn Q 3 cộng một phẩy năm IQR. "
        "IQR giúp chúng ta trả lời câu hỏi: điểm này có bất thường so với phần lớn dữ liệu hay không?"
    ),
    "s6": (
        "Nhưng một điểm bất thường chưa chắc đã ảnh hưởng mạnh đến mô hình hồi quy."
    ),
    "s7": (
        "Để đánh giá mức độ ảnh hưởng của một điểm đến mô hình, chúng ta sử dụng Leverage – hay độ đòn bẩy. "
        "Leverage đo lường mức độ khác biệt của một quan sát so với vị trí trung tâm của dữ liệu. "
        "Điểm càng xa giá trị trung bình của biến độc lập thì Leverage càng lớn. "
        "Leverage giúp trả lời câu hỏi: điểm này có đủ sức kéo lệch mô hình hay không?"
    ),
    "s8": (
        "Khi kết hợp cả hai phương pháp, chúng ta có thể phân loại các điểm dữ liệu theo mức độ nguy hiểm. "
        "Có những điểm bất thường nhưng ít ảnh hưởng. Có những điểm không quá bất thường nhưng lại có Leverage cao. "
        "Và đáng chú ý nhất là những điểm vừa là Outlier theo khoảng tứ phân vị IQR, vừa có Leverage lớn."
    ),
    "s9": (
        "Khi một điểm vừa bất thường vừa có Leverage cao xuất hiện, đường hồi quy có thể bị kéo lệch đáng kể."
    ),
    "s10": (
        "Vì vậy, trước khi xây dựng hoặc sử dụng một mô hình dự báo, các nhà phân tích cần kiểm tra dữ liệu bằng nhiều góc nhìn khác nhau. "
        "Nếu điểm đó là lỗi nhập liệu, có thể loại bỏ hoặc chỉnh sửa. Nếu là trường hợp đặc biệt nhưng có ý nghĩa thực tế, cần cân nhắc các phương pháp hồi quy bền vững hơn."
    ),
    "s11": (
        "Những kỹ thuật này được sử dụng rộng rãi trong tài chính, y tế, sản xuất và bất kỳ lĩnh vực nào dựa vào mô hình dự báo để ra quyết định."
    ),
    "s12": (
        "Outlier không chỉ là những điểm khác biệt. Điều quan trọng là hiểu liệu chúng có đủ sức ảnh hưởng đến mô hình hay không. "
        "IQR giúp phát hiện sự bất thường, còn Leverage giúp đánh giá mức độ tác động."
    ),
    "s13": (
        "Các khái niệm chính trong video gồm: Outlier, khoảng tứ phân vị IQR, Leverage và Hồi quy tuyến tính."
    ),
    "s14": (
        "Nếu một điểm dữ liệu vừa là Outlier vừa có Leverage cao, liệu chúng ta nên loại bỏ nó hay tìm một mô hình phù hợp hơn? "
        "Hãy để lại ý kiến của bạn dưới phần bình luận nhé! Xin chào và hẹn gặp lại ở các video tiếp theo của FaMI."
    ),
}

# ─── Phụ đề song ngữ theo từng scene ───────────────────────────────────────
# Mỗi entry: (vi_text, en_text, wait_before, hold_duration)
SUBS = {
    "s1": [
        ("Liệu chỉ một điểm dữ liệu bất thường có thể làm\nthay đổi hoàn toàn kết quả của một mô hình dự báo?",
         "Can just a single abnormal data point completely\nchange the results of a forecasting model?",
         0.3, 6.0),
    ],
    "s2": [
        ("Ở video trước, chúng ta đã sử dụng hồi quy\nđể dự đoán giá nhà.",
         "In the previous video, we used regression\nto predict housing prices.",
         0.3, 4.5),
        ("Nhưng dữ liệu thực tế không phải lúc nào cũng hoàn hảo.",
         "But real-world data is not always perfect.",
         0.1, 4.0),
        ("Giả sử xuất hiện một giao dịch có diện tích chỉ 60 m²\nnhưng giá bán lên tới 10 tỷ đồng.",
         "Suppose a transaction occurs with an area of only 60 m²\nbut the selling price is up to 10 billion VND.",
         0.1, 6.0),
        ("Đây là một căn nhà đặc biệt,\nhay chỉ đơn giản là dữ liệu bất thường?",
         "Is this a special house,\nor simply abnormal data?",
         0.1, 5.0),
    ],
    "s3": [
        ("Trong thực tế, dữ liệu luôn tồn tại\nnhững quan sát khác biệt.",
         "In practice, data always contains\ndifferent observations.",
         0.3, 4.5),
        ("Một số chỉ đơn giản là hiếm gặp. Nhưng một số\nkhác lại có thể làm sai lệch toàn bộ mô hình.",
         "Some are simply rare. But others\ncan distort the entire model.",
         0.1, 5.5),
    ],
    "s4": [
        ("Outlier là những điểm dữ liệu nằm xa\nphần lớn các quan sát còn lại.",
         "Outliers are data points that lie far\nfrom the majority of other observations.",
         0.3, 5.0),
        ("Tuy nhiên, với bộ dữ liệu hàng triệu điểm,\nchúng ta không thể chỉ nhìn bằng mắt...",
         "However, with a dataset of millions of points,\nwe cannot simply rely on visual inspection...",
         0.1, 5.0),
        ("...để kết luận một điểm là Outlier.",
         "...to conclude that a point is an outlier.",
         0.1, 4.5),
        ("Hôm nay, chúng ta sẽ tìm hiểu 2 phương pháp hỗ trợ\nlà quy tắc 1.5IQR và Độ đo Leverage.",
         "Today, we will learn 2 supporting methods:\nthe 1.5IQR rule and the Leverage metric.",
         0.1, 6.5),
    ],
    "s5": [
        ("Đầu tiên, chúng ta có thể sử dụng IQR – khoảng\ntứ phân vị – để phát hiện giá trị bất thường.",
         "First, we can use IQR – Interquartile Range –\nto detect abnormal values in the distribution.",
         0.3, 5.5),
        ("IQR được tính bằng hiệu giữa\ntứ phân vị thứ ba và thứ nhất.",
         "IQR is calculated as the difference\nbetween the third and first quartiles.",
         0.1, 4.5),
        ("Một điểm được xem là Outlier nếu nhỏ hơn Q1 - 1.5IQR\nhoặc lớn hơn Q3 + 1.5IQR.",
         "A point is considered an outlier if smaller than Q1 - 1.5IQR\nor greater than Q3 + 1.5IQR.",
         0.1, 5.5),
        ("IQR giúp trả lời câu hỏi: điểm này\ncó bất thường so với dữ liệu hay không?",
         "IQR helps answer the question: is this point\nabnormal compared to most of the data?",
         0.1, 5.0),
    ],
    "s6": [
        ("Nhưng một điểm bất thường chưa chắc\nđã ảnh hưởng mạnh đến mô hình hồi quy.",
         "But an abnormal point does not necessarily\nhave a strong impact on the regression model.",
         0.3, 6.0),
    ],
    "s7": [
        ("Để đánh giá mức độ ảnh hưởng của một điểm,\nchúng ta sử dụng Leverage – hay độ đòn bẩy.",
         "To evaluate the impact of a point,\nwe use Leverage.",
         0.3, 5.0),
        ("Leverage đo lường mức độ khác biệt của\nquan sát so với vị trí trung tâm dữ liệu.",
         "Leverage measures the difference of\nan observation from the center of the data.",
         0.1, 5.0),
        ("Điểm càng xa giá trị trung bình của biến\nđộc lập thì Leverage càng lớn.",
         "The further the point is from the independent\nvariable's mean, the larger the Leverage.",
         0.1, 4.5),
        ("Leverage giúp trả lời câu hỏi: điểm này\ncó đủ sức kéo lệch mô hình hay không?",
         "Leverage helps answer: does this point\nhave enough influence to distort the model?",
         0.1, 4.5),
    ],
    "s8": [
        ("Khi kết hợp cả hai phương pháp, chúng ta\ncó thể phân loại điểm dữ liệu theo độ nguy hiểm.",
         "Combining both methods allows us to\nclassify data points by their danger level.",
         0.3, 5.5),
        ("Có những điểm bất thường nhưng ít ảnh hưởng,\ncó những điểm có Leverage cao dù không quá bất thường.",
         "Some are abnormal but have little impact;\nsome have high leverage without being too abnormal.",
         0.1, 6.0),
        ("Và đáng chú ý nhất là những điểm vừa là\nOutlier theo IQR, vừa có Leverage lớn.",
         "And most notable are points that are both\noutliers by IQR and have high leverage.",
         0.1, 5.5),
    ],
    "s9": [
        ("Khi một điểm vừa bất thường vừa có Leverage cao\nxuất hiện, đường hồi quy có thể bị kéo lệch đáng kể.",
         "When a point that is both abnormal and has high\nleverage appears, the regression line can distort significantly.",
         0.3, 6.0),
    ],
    "s10": [
        ("Vì vậy, trước khi xây dựng hoặc sử dụng mô hình,\nnhà phân tích cần kiểm tra dữ liệu qua nhiều góc nhìn.",
         "Therefore, before building or using a model,\nanalysts need to check data from multiple perspectives.",
         0.3, 5.5),
        ("Nếu là lỗi nhập liệu, có thể loại bỏ/chỉnh sửa.\nNếu là trường hợp đặc biệt, cần hồi quy bền vững.",
         "If it is an entry error, remove or edit it.\nIf it is special, consider robust regression.",
         0.1, 6.0),
    ],
    "s11": [
        ("Những kỹ thuật này được sử dụng rộng rãi trong\ntài chính, y tế, sản xuất và dự báo quyết định.",
         "These techniques are widely used in finance,\nhealthcare, manufacturing, and decision forecasting.",
         0.3, 6.0),
    ],
    "s12": [
        ("Outlier không chỉ là những điểm khác biệt. Điều\nquan trọng là nó có đủ sức ảnh hưởng mô hình hay không.",
         "Outliers are not just different. The key\nis whether they influence the model.",
         0.3, 6.0),
        ("IQR giúp phát hiện sự bất thường,\ncòn Leverage giúp đánh giá mức độ tác động.",
         "IQR detects abnormality, while Leverage\nassesses the level of impact.",
         0.1, 5.0),
    ],
    "s13": [
        ("Các khái niệm chính trong video gồm:\nOutlier, IQR, Leverage và Hồi quy tuyến tính.",
         "The main concepts in this video are:\nOutlier, IQR, Leverage, and Linear Regression.",
         0.3, 6.0),
    ],
    "s14": [
        ("Nếu một điểm dữ liệu vừa là Outlier vừa có Leverage cao,\nliệu nên loại bỏ nó hay tìm mô hình phù hợp hơn?",
         "If a data point is both an outlier and has high leverage,\nshould we remove it or find a better model?",
         0.3, 6.0),
        ("Hãy để lại ý kiến của bạn dưới bình luận nhé!\nHẹn gặp lại ở các video tiếp theo của FaMI.",
         "Please leave your thoughts in the comments!\nSee you in the next videos of FaMI.",
         0.1, 6.0),
    ],
}

# ─── Tiện ích audio ────────────────────────────────────────────────────────
def audio_path(name: str) -> str:
    """Trả về đường dẫn tới file mp3 của scene."""
    return os.path.join(AUDIO_DIR, f"{name}.mp3")


def generate_audio():
    """Sinh file TTS cho tất cả các scene (bỏ qua nếu đã có)."""
    try:
        from gtts import gTTS
    except ImportError:
        print("pip install gtts"); sys.exit(1)
    os.makedirs(AUDIO_DIR, exist_ok=True)
    missing = [k for k in SCRIPTS if not os.path.exists(audio_path(k))]
    if not missing:
        print("Audio OK\n"); return
    print("Sinh TTS...")
    for name in missing:
        gTTS(text=SCRIPTS[name], lang="vi", slow=False).save(audio_path(name))
        print(f"  {name}.mp3 OK")
    print()
