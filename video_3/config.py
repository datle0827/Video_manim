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
        "Làm thế nào để có thể xây dựng một danh mục đầu tư vừa có lợi nhuận, vừa giảm thiểu rủi ro?"
    ),
    "s2": (
        "Giả sử bạn là một nhà đầu tư tham gia vào thị trường chứng khoán và đang có một trăm triệu đồng. "
        "Sau khi phân tích thị trường, bạn tìm được hai cổ phiếu tiềm năng là C T G và F P T."
    ),
    "s3": (
        "Dựa trên dữ liệu lịch sử về tỷ suất sinh lợi của hai cổ phiếu trong năm tháng gần nhất như sau, "
        "ta tính tỷ suất sinh lợi trung bình của từng cổ phiếu và thấy cổ phiếu C T G có lợi nhuận trung bình cao hơn cổ phiếu F P T."
    ),
    "s4": (
        "Thoạt nhìn, nhiều người sẽ nghĩ rằng nên đầu tư toàn bộ vào cổ phiếu C T G vì lợi nhuận cao hơn. "
        "Nhưng trong đầu tư, lợi nhuận không phải yếu tố duy nhất. Chúng ta còn phải quan tâm đến rủi ro. "
        "Vậy nên phân bổ số tiền này như thế nào để danh mục ít rủi ro nhất?"
    ),
    "s5": (
        "Để trả lời được câu hỏi này, chúng ta sẽ sử dụng Lý thuyết Danh mục Đầu tư Hiện đại do Harry Markowitz đề xuất. "
        "Từ dữ liệu trên, ta sẽ tính độ lệch chuẩn để đánh giá mức độ biến động của từng cổ phiếu. "
        "Độ lệch chuẩn càng lớn thì rủi ro càng cao. Tuy nhiên, rủi ro của danh mục không chỉ phụ thuộc vào từng cổ phiếu riêng lẻ "
        "mà còn phụ thuộc vào cách chúng biến động so với nhau. Để biết hai cổ phiếu ảnh hưởng lẫn nhau như thế nào, ta sử dụng hiệp phương sai. "
        "Hiệp phương sai đo lường mức độ biến động cùng nhau của hai tài sản. Sau khi áp dụng công thức hiệp phương sai cho dữ liệu lịch sử, "
        "ta thu được một giá trị là âm mười phẩy bốn mươi tám."
    ),
    "s6": (
        "Quay lại câu hỏi ban đầu, ta đặt w c t g là tỷ trọng vốn đầu tư vào cổ phiếu C T G và w f p t là tỷ trọng vốn đầu tư vào cổ phiếu F P T. "
        "Ta sẽ tính được phương sai của danh mục đầu tư theo công thức: Var p bằng w c t g bình phương nhân sigma c t g bình phương cộng "
        "w f p t bình phương nhân sigma f p t bình phương cộng hai lần w c t g w f p t nhân hiệp phương sai của C T G và F P T. Giả sử bạn quyết định đầu tư "
        "sáu mươi phần trăm vào C T G và bốn mươi phần trăm cho F P T, khi đó Var p sẽ bằng mười chín phẩy chín mươi bảy. "
        "Phương sai không phải là một giá trị dễ giải thích vì vậy hầu hết các nhà phân tích sử dụng độ lệch chuẩn. "
        "Vậy độ lệch chuẩn của danh mục đầu tư này sẽ là bốn phẩy bốn mươi bảy phần trăm, hay còn là thước đo cho Mức độ rủi ro trong danh mục đầu tư."
    ),
    "s7": (
        "Ta có thể thấy bằng cách kết hợp C T G và F P T theo tỷ trọng phù hợp, nhà đầu tư có thể giảm rủi ro mà vẫn duy trì mức lợi nhuận hấp dẫn. "
        "Ý tưởng này chính là nền tảng của Lý thuyết Danh mục Đầu tư Hiện đại mà hiện nay hầu hết các quỹ đầu tư chuyên nghiệp "
        "vẫn đang sử dụng để tìm kiếm sự kết hợp tối ưu giữa nhiều tài sản."
    ),
    "s8": (
        "Qua ví dụ này, chúng ta thấy rằng hiệp phương sai không chỉ là một công cụ thống kê. "
        "Nó giúp đo lường mối quan hệ giữa các tài sản và đóng vai trò quan trọng trong việc xác định tỷ trọng đầu tư tối ưu. "
        "Nhờ đó, nhà đầu tư có thể đưa ra quyết định phân bổ vốn hợp lý và giảm thiểu rủi ro cho danh mục. "
        "Trong video này mình đề cập tới ba khái niệm quan trọng: Hiệp phương sai, Phương sai danh mục đầu tư, "
        "Đa dạng hóa đầu tư và Lý thuyết Markowitz."
    ),
    "s9": (
        "Câu hỏi dành cho bạn: Nếu xuất hiện một cổ phiếu C có lợi nhuận tương đương nhưng có tương quan âm với F P T, "
        "liệu danh mục đầu tư có thể trở nên an toàn hơn nữa hay không? Hãy để lại câu trả lời của bạn dưới phần bình luận nhé! "
        "Xin chào và hẹn gặp lại ở các video tiếp theo của FaMI."
    ),
}

# ─── Phụ đề song ngữ theo từng scene ───────────────────────────────────────
# Mỗi entry: (vi_text, en_text, wait_before, hold_duration)
SUBS = {
    "s1": [
        ("Làm thế nào để có thể xây dựng một danh mục đầu tư\nvừa có lợi nhuận, vừa giảm thiểu rủi ro?",
         "How can we build a portfolio that is\nboth profitable and minimizes risk?",
         0.4, 6.0),
    ],
    "s2": [
        ("Giả sử bạn là một nhà đầu tư tham gia thị trường\nvà đang có 100 triệu đồng.",
         "Suppose you are a stock investor\nwith 100 million VND.",
         0.3, 4.5),
        ("Sau khi phân tích thị trường, bạn tìm được\nhai cổ phiếu tiềm năng là CTG và FPT.",
         "After analysis, you find two potential\nstocks, CTG and FPT.",
         0.1, 4.5),
    ],
    "s3": [
        ("Dựa trên dữ liệu tỷ suất sinh lợi 5 tháng qua,\nta tính tỷ suất lợi nhuận trung bình.",
         "Based on returns of the past 5 months,\nwe calculate average returns.",
         0.3, 5.0),
        ("Ta thấy cổ phiếu CTG có lợi nhuận trung bình\ncao hơn cổ phiếu FPT.",
         "We see that stock CTG has a higher average return\nthan stock FPT.",
         0.1, 4.0),
    ],
    "s4": [
        ("Thoạt nhìn, nhiều người sẽ nghĩ nên đầu tư\ntoàn bộ vào cổ phiếu CTG vì lợi nhuận cao hơn.",
         "At first, many think to invest fully in CTG\nbecause of its higher return.",
         0.3, 5.0),
        ("Nhưng trong đầu tư, ta phải quan tâm đến rủi ro.\nNên phân bổ số tiền này thế nào để ít rủi ro nhất?",
         "But in investing, we must care about risk.\nHow to allocate to minimize risk?",
         0.1, 5.5),
    ],
    "s5": [
        ("Để trả lời câu hỏi này, chúng ta sử dụng\nLý thuyết Danh mục Đầu tư Hiện đại.",
         "To answer this, we use Modern Portfolio Theory\nproposed by Harry Markowitz.",
         0.3, 5.0),
        ("Ta tính độ lệch chuẩn để đánh giá rủi ro.\nĐộ lệch chuẩn càng lớn thì rủi ro càng cao.",
         "We calculate standard deviation to assess risk.\nThe higher it is, the higher the risk.",
         0.1, 5.0),
        ("Để biết hai cổ phiếu ảnh hưởng lẫn nhau thế nào,\nta sử dụng Hiệp phương sai (Covariance).",
         "To see how the two stocks affect each other,\nwe use Covariance.",
         0.1, 5.0),
        ("Hiệp phương sai đo biến động cùng nhau của hai tài sản.\nGiá trị hiệp phương sai tính được là -10.48.",
         "Covariance measures co-movement of assets.\nThe calculated covariance is -10.48.",
         0.1, 5.5),
    ],
    "s6": [
        ("Đặt w_CTG, w_FPT là tỷ trọng đầu tư vào CTG và FPT.\nTa tính phương sai danh mục theo công thức:",
         "Let w_CTG, w_FPT be weights for CTG and FPT.\nWe compute portfolio variance via formula:",
         0.3, 5.5),
        ("Với tỷ trọng 60% vào CTG và 40% vào FPT,\nta tính được Var(P) = 19.97.",
         "With 60% in CTG and 40% in FPT,\nwe get Var(P) = 19.97.",
         0.1, 5.0),
        ("Độ lệch chuẩn của danh mục sẽ là 4.47%,\nthước đo cho Mức độ rủi ro trong danh mục.",
         "The portfolio standard deviation is 4.47%,\nthe measure of portfolio risk.",
         0.1, 5.5),
    ],
    "s7": [
        ("Bằng cách kết hợp CTG và FPT theo tỷ trọng phù hợp,\nta giảm rủi ro mà vẫn duy trì lợi nhuận tốt.",
         "By combining CTG and FPT in proper weights,\nwe reduce risk while keeping good returns.",
         0.3, 5.5),
        ("Ý tưởng này chính là nền tảng của\nLý thuyết Danh mục Đầu tư Hiện đại.",
         "This idea is the foundation of\nModern Portfolio Theory.",
         0.1, 5.0),
    ],
    "s8": [
        ("Hiệp phương sai giúp đo lường mối quan hệ và\nxác định tỷ trọng đầu tư tối ưu.",
         "Covariance measures relationships and\nhelps determine optimal weights.",
         0.3, 5.0),
        ("Trong video này mình đề cập tới 3 khái niệm:\nHiệp phương sai, Phương sai danh mục, và Đa dạng hóa.",
         "In this video we covered 3 concepts:\nCovariance, Portfolio Variance, and Diversification.",
         0.1, 6.0),
    ],
    "s9": [
        ("Nếu xuất hiện cổ phiếu C cùng lợi nhuận\nnhưng tương quan âm với FPT, liệu danh mục có an toàn hơn?",
         "If a stock C has same return but negative\ncorrelation with FPT, will the portfolio be safer?",
         0.3, 6.0),
        ("Hãy để lại câu trả lời dưới phần bình luận nhé!\nHẹn gặp lại các bạn trong những video sau!",
         "Please leave your answer in the comments!\nSee you in the next videos!",
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
