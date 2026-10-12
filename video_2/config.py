#!/usr/bin/env python3
"""
config.py – Hằng số, màu sắc, nội dung audio/phụ đề, và tiện ích audio.
"""

import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_DIR  = os.path.join(SCRIPT_DIR, "audio")
LOGO_PATH  = os.path.join(SCRIPT_DIR, "fami_logo_transparent.jpg")

# ─── Cấu hình video (FaMI Standard) ───────────────────────────────────────
VIDEO_W   = 1080
VIDEO_H   = 1920
FRAME_W   = 9.0
FRAME_H   = 16.0
BG_COLOR  = "#0A0F1E"
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

# Legacy safe zone (compatibility)
LOGO_Y              =  6.9
SUB_VI_Y            = -6.55
SUB_EN_Y            = -8.05
CONTENT_TOP         =  6.0
CONTENT_BOT         = -5.8
SAFE_SUBTITLE_MARGIN = -3.3  # Buffer an toàn từ phụ đề (-3.8 + 0.5)

# ─── Audio scripts (TTS tiếng Việt) ────────────────────────────────────────
SCRIPTS = {
    "s1": (
        "Làm thế nào để một nhà máy có thể kiểm soát chất lượng sản phẩm một cách hiệu quả, "
        "khi số lượng sản phẩm lỗi mỗi ngày luôn thay đổi?"
    ),
    "s2": (
        "Trong một dây chuyền sản xuất, không phải sản phẩm nào cũng đạt chất lượng hoàn hảo. "
        "Mỗi ngày, số lượng sản phẩm lỗi có thể thay đổi. "
        "Để trả lời câu hỏi đó, chúng ta sử dụng một công cụ trong xác suất, đó là biến ngẫu nhiên rời rạc."
    ),
    "s3": (
        "Gọi X là số sản phẩm lỗi trong một ngày. "
        "X là một biến ngẫu nhiên rời rạc, vì nó nhận các giá trị nguyên đếm được như 0, 1, 2 hoặc 3. "
        "Ở đây, ta giả sử đang xét các lỗi nghiêm trọng trong một dây chuyền đã được kiểm soát tốt, "
        "nên số lỗi mỗi ngày thường nhỏ và nằm trong khoảng này."
    ),
    "s4": (
        "Trong thực tế, không phải ngày nào nhà máy cũng có số lượng sản phẩm lỗi giống nhau. "
        "Dựa trên dữ liệu trong quá khứ, số sản phẩm lỗi mỗi ngày có thể rơi vào các trường hợp sau: "
        "xác suất không có lỗi là không phẩy ba, có 1 lỗi là không phẩy bốn, 2 lỗi là không phẩy hai, và 3 lỗi là không phẩy một. "
        "Bảng này chính là bảng phân phối xác suất của X, cho biết khả năng xảy ra của từng số lượng lỗi."
    ),
    "s5": (
        "Từ đó, ta có thể tính được giá trị kỳ vọng của X, tức là số lỗi trung bình mỗi ngày. "
        "Cụ thể: E của X bằng không nhân không phẩy ba, cộng một nhân không phẩy bốn, "
        "cộng hai nhân không phẩy hai, cộng ba nhân không phẩy một, bằng một phẩy một. "
        "Điều này có nghĩa là, trung bình mỗi ngày có khoảng một phẩy một sản phẩm lỗi."
    ),
    "s6": (
        "Tuy nhiên, chỉ biết trung bình là chưa đủ. Trong thực tế, số lỗi có thể dao động giữa các ngày, "
        "có hôm không có lỗi, nhưng cũng có hôm lên tới 3 lỗi. Để đo mức độ biến động này, ta sử dụng phương sai. "
        "Ta tính được kỳ vọng của X bình phương bằng 2 phẩy 1, "
        "từ đó phương sai của X bằng 2 phẩy 1 trừ đi 1 phẩy 1 bình phương, bằng 0 phẩy 89. "
        "Phương sai cho thấy rằng số lỗi không cố định, mà có sự dao động nhất định quanh giá trị trung bình."
    ),
    "s7": (
        "Những kết quả này không chỉ mang ý nghĩa lý thuyết, mà còn có giá trị thực tiễn rất lớn. "
        "Giả sử mỗi sản phẩm lỗi gây thiệt hại năm trăm nghìn đồng. Khi đó, chi phí lỗi trung bình mỗi ngày sẽ là "
        "một phẩy một nhân năm trăm bằng năm trăm năm mươi nghìn đồng. Bây giờ, nhà máy có thể cân nhắc một phương án khác: "
        "đầu tư hệ thống kiểm tra chất lượng với chi phí hai trăm nghìn mỗi ngày, giúp giảm số lỗi trung bình xuống còn không phẩy lăm lỗi. "
        "Khi đó, tổng chi phí sẽ là không phẩy lăm nhân năm trăm cộng hai trăm bằng bốn trăm năm mươi nghìn đồng. "
        "Như vậy, phương án hai có chi phí thấp hơn rõ rệt. Do đó, nhà máy nên ưu tiên đầu tư hệ thống kiểm tra chất lượng."
    ),
    "s8": (
        "Qua ví dụ này, ta thấy rằng biến ngẫu nhiên rời rạc là một công cụ rất hữu ích. "
        "Trong video này mình đề cập tới các khái niệm quan trọng: Biến ngẫu nhiên rời rạc, hàm phân phối xác suất, kỳ vọng, và phương sai."
    ),
    "s9": (
        "Câu hỏi dành cho bạn: Vậy trong trường hợp phần trăm rủi ro ngày càng lớn, "
        "doanh nghiệp nên quyết định trực tiếp chịu rủi ro hay nâng cấp trang thiết bị để giảm thiểu?"
    ),
}

# ─── Phụ đề song ngữ theo từng scene ───────────────────────────────────────
# Mỗi entry: (vi_text, en_text, wait_before, hold_duration)
SUBS = {
    "s1": [
        ("Làm thế nào để một nhà máy\nkiểm soát chất lượng một cách hiệu quả,",
         "How can a factory effectively\ncontrol product quality,",
         0.4, 3.5),
        ("khi số lượng sản phẩm lỗi\nmỗi ngày luôn thay đổi?",
         "when daily defect count\nconstantly varies?",
         0.1, 3.5),
    ],
    "s2": [
        ("Trong một dây chuyền sản xuất,",
         "In a production line,",
         0.2, 2.0),
        ("không phải sản phẩm nào\ncũng đạt chất lượng hoàn hảo.",
         "not every product\nachieves perfect quality.",
         0.1, 2.5),
        ("Mỗi ngày, số lượng sản phẩm lỗi\ncó thể thay đổi.",
         "Every day, the number of\ndefective products varies.",
         0.2, 2.5),
        ("Để trả lời câu hỏi đó,",
         "To answer this question,",
         0.2, 1.5),
        ("chúng ta sử dụng 1 công cụ xác suất,\nđó là: Biến ngẫu nhiên rời rạc.",
         "we use a probability tool:\nDiscrete random variables.",
         0.1, 3.0),
    ],
    "s3": [
        ("Gọi X là số sản phẩm lỗi trong 1 ngày.",
         "Let X be the number of defective products per day.",
         0.3, 2.5),
        ("X là một biến ngẫu nhiên rời rạc,",
         "X is a discrete random variable,",
         0.1, 2.0),
        ("vì nó nhận các giá trị đếm được\nnhư 0, 1, 2, hoặc 3.",
         "since it takes countable values\nlike 0, 1, 2, or 3.",
         0.1, 3.5),
        ("Giả sử đây là dây chuyền\nđã được kiểm soát tốt,",
         "Assuming a well-controlled line,",
         0.2, 2.5),
        ("nên số lỗi thường rất nhỏ\nvà nằm trong khoảng này.",
         "defects are usually minimal\nand fall within this range.",
         0.1, 3.0),
    ],
    "s4": [
        ("Trong thực tế, không phải ngày nào\ncũng có số lượng lỗi giống nhau.",
         "In reality, the defect count\nis not the same every day.",
         0.4, 3.5),
        ("Dựa trên dữ liệu trong quá khứ,\nsự phân bố lỗi thường xuất hiện như sau:",
         "Based on past data,\nthe defect distribution appears as follows:",
         0.2, 4.0),
        ("0 lỗi (0.3), 1 lỗi (0.4),\n2 lỗi (0.2), 3 lỗi (0.1).",
         "0 defect (0.3), 1 (0.4),\n2 (0.2), 3 (0.1).",
         0.1, 4.0),
        ("Bảng này chính là\nbảng phân phối xác suất của X,",
         "This table is the\nprobability distribution table of X,",
         0.2, 3.0),
        ("cho biết khả năng xảy ra\ncủa từng mức độ lỗi.",
         "showing the likelihood\nof each defect count.",
         0.1, 3.0),
    ],
    "s5": [
        ("Từ đó, ta có thể tính được Kỳ vọng của X,",
         "From this, we calculate the\nExpected Value of X,",
         0.4, 2.5),
        ("tức là số lỗi trung bình mỗi ngày.",
         "i.e., average daily defects.",
         0.1, 2.5),
        ("Cụ thể: E(X) = 0×0.3 + 1×0.4\n+ 2×0.2 + 3×0.1 = 1.1",
         "Specifically: E(X) = 0×0.3 + 1×0.4\n+ 2×0.2 + 3×0.1 = 1.1",
         0.2, 5.0),
        ("Nghĩa là: Trung bình mỗi ngày có khoảng\n1.1 sản phẩm lỗi.",
         "Meaning: There are about\n1.1 defective products daily on average.",
         0.2, 4.0),
    ],
    "s6": [
        ("Tuy nhiên, chỉ biết trung bình là chưa đủ.",
         "However, knowing the average isn't enough.",
         0.4, 2.5),
        ("Trong thực tế số lỗi có thể\ndao động giữa các ngày,",
         "In reality, defects fluctuate\nbetween days,",
         0.1, 2.5),
        ("có hôm không có lỗi,\nnhưng có hôm lên tới 3 lỗi.",
         "some days no defects,\nbut some days up to 3.",
         0.1, 3.0),
        ("Để đo mức độ biến động này,\nta sử dụng Phương sai.",
         "To measure this variance,\nwe use the Variance.",
         0.2, 3.0),
        ("Ta tính được E(X²) = 2.1.",
         "We compute E(X²) = 2.1.",
         0.2, 2.0),
        ("Suy ra Var(X) = 2.1 - (1.1)² = 0.89",
         "Thus Var(X) = 2.1 - (1.1)² = 0.89",
         0.1, 3.5),
        ("Phương sai đo lường sự dao động\nnhất định quanh giá trị trung bình.",
         "Variance measures the constant fluctuation\naround the average value.",
         0.2, 4.0),
    ],
    "s7": [
        ("Những kết quả này còn có giá trị\nthực tiễn rất lớn. Giả sử mỗi sản phẩm lỗi",
         "These results also have great practical\nvalue. Assume each defect",
         0.4, 3.5),
        ("gây thiệt hại 500 nghìn đồng.\nKhi đó, chi phí lỗi trung bình sẽ là",
         "causes 500k loss.\nThen, the average defect cost will be",
         0.1, 3.5),
        ("1.1 × 500 = 550 nghìn đồng/ngày.",
         "1.1 × 500 = 550k VND/day.",
         0.2, 3.5),
        ("Bây giờ, nhà máy có thể cân nhắc phương án 2:\nĐầu tư hệ thống kiểm tra 200 nghìn/ngày,",
         "Now, consider Option 2: Invest\n200k/day in a QA system,",
         0.2, 4.5),
        ("giúp giảm số lỗi xuống còn 0.5 lỗi.",
         "reducing defects to 0.5.",
         0.1, 2.5),
        ("Khi đó, tổng chi phí sẽ là:\n0.5 × 500 + 200 = 450 nghìn đồng.",
         "Then, total cost will be:\n0.5 × 500 + 200 = 450k VND.",
         0.2, 4.5),
        ("Như vậy, phương án 2 điểm chi phí tối ưu hơn.\nNhà máy nên đầu tư QA.",
         "Thus, option 2 has lower cost.\nThe factory should invest in QA.",
         0.1, 4.0),
    ],
    "s8": [
        ("Qua ví dụ này, ta thấy biến ngẫu nhiên rời rạc\nlà một công cụ rất hữu ích.",
         "Through this example, the discrete random\nvariable is a very useful tool.",
         0.4, 4.0),
        ("Trong video này mình đề cập tới 4 khái niệm:\nBiến rời rạc, Hàm phân phối, Kỳ vọng & Phương sai.",
         "In this video we covered 4 concepts:\nVariable, Distribution, Expected Value & Variance.",
         0.1, 6.0),
    ],
    "s9": [
        ("Câu hỏi dành cho bạn:\nTrong trường hợp phần trăm rủi ro ngày càng lớn,",
         "A question for you:\nAs the statistical market risk rises,",
         0.2, 4.0),
        ("doanh nghiệp nên thiếp tục trực tiếp chịu rủi ro\nhay nâng cấp trang thiết bị để giảm thiểu?",
         "should the firm continue to take the risk\nor invest to minimize future errors?",
         0.1, 5.0),
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
