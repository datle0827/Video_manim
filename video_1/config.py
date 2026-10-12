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
        "Làm thế nào để tự động xác định được một khoản vay "
        "có được phê duyệt hay không một cách thông minh?"
    ),
    "s2_problem": (
        "Để xác định một hồ sơ có đủ điều kiện vay vốn hay không, "
        "cần có rất nhiều yếu tố như tuổi, thu nhập, điểm tín dụng, mục đích vay, vân vân. "
        "Nhưng để đơn giản, ta giả sử quy trình thẩm định rút gọn của ngân hàng gồm hai bước. "
        "Bước một: xác định mức thu nhập. "
        "Bước hai: kiểm tra lịch sử tín dụng. "
        "Sau đó ngân hàng mới quyết định có duyệt khoản vay hay không."
    ),
    "s3_tree": (
        "Thay vì mô tả bằng văn bản dài dòng, ta sẽ mô hình hóa quá trình này bằng cây quyết định. "
        "Dựa trên những dữ liệu thu thập được trong quá khứ, "
        "khoảng sáu mươi phần trăm khách hàng có mức thu nhập cao, "
        "bốn mươi phần trăm còn lại có mức thu nhập trung bình hoặc thấp. "
        "Nếu khách hàng có thu nhập cao, khả năng có tín dụng tốt là tám mươi phần trăm. "
        "Nếu khách hàng có thu nhập trung bình, khả năng có tín dụng tốt là năm mươi phần trăm. "
        "Nếu tín dụng tốt, khoản vay sẽ được hoàn trả với tỷ lệ là chín mươi phần trăm. "
        "Nếu có tín dụng trung bình nhưng thu nhập cao, khả năng này là bảy mươi phần trăm, "
        "còn thu nhập trung bình sẽ là năm mươi phần trăm."
    ),
    "s4_path": (
        "Đây chính là một chuỗi xác suất có điều kiện. "
        "Để biết xác suất xảy ra của một kịch bản cụ thể, "
        "ta chỉ cần nhân các xác suất trên cùng một nhánh của cây. "
        "Ví dụ cho trường hợp: khách có thu nhập cao, tín dụng tốt, khoản vay được hoàn trả. "
        "Xác suất của trường hợp này là P bằng không phẩy sáu nhân không phẩy tám nhân không phẩy chín bằng không phẩy bốn ba hai. "
        "Giả sử ngân hàng đặt ra một ngưỡng duyệt tại nhánh cuối là bảy mươi phần trăm. "
        "Các hồ sơ nếu có xác suất duyệt tại nhánh này lớn hơn bảy mươi phần trăm "
        "sẽ được tự động duyệt, còn không sẽ được thẩm định thêm."
    ),
    "s5_total": (
        "Để tính xác suất tổng thể được tự động duyệt vay, "
        "ta phải cộng xác suất của tất cả các nhánh dẫn đến kết quả được duyệt vay. "
        "Đây chính là sự kết hợp của quy tắc cộng và nhân xác suất. "
        "Như vậy, khoảng tám mươi phần trăm các hồ sơ đã được tự động duyệt một cách thông minh. "
        "Nhờ cây quyết định, chúng ta có thể nhìn rõ toàn bộ quy trình ra quyết định của ngân hàng."
    ),
    "s6_summary": (
        "Qua ví dụ này, ta đã thấy được cách cây quyết định được ứng dụng thế nào cho ngân hàng trong việc tự động ra quyết định một cách thông minh. "
        "giúp kiểm soát rủi ro hiệu quả.  "
        "Chúng ta không chỉ mô hình hóa được luồng suy nghĩ của ngân hàng"
        " mà còn tính toán chính xác xác suất cho từng kịch bản"
        "Phương pháp này hiện đang là xương sống trong rất nhiều hệ thống phân tích tín dụng, thẩm định đầu tư và quản trị rủi ro doanh nghiệp."
    ),
    "s7_keywords": (
        "Trong video này mình đề cập tới ba khái niệm quan trọng: "
        "Cây quyết định, xác suất có điều kiện, và quy tắc nhân cộng xác suất."
    ),
    "s8_question": (
        "Câu hỏi dành cho bạn: "
        "Nếu ngân hàng siết chặt tiêu chuẩn tín dụng và giảm xác suất duyệt vay từ không phẩy chín "
        "xuống không phẩy bảy, thì xác suất tổng thể được duyệt vay sẽ thay đổi như thế nào?"
    ),
}

# ─── Phụ đề song ngữ theo từng scene ───────────────────────────────────────
# Mỗi entry: (vi_text, en_text, wait_before, hold_duration)
SUBS = {
    "s1": [
        ("Làm thế nào để tự động xác định\nmột khoản vay có được phê duyệt hay không một cách thông minh?",
         "How can we intelligently and automatically determine\nif a loan will be approved?",
         0.8, 6.0),
    ],
    "s2_problem": [
        ("Để xác định 1 hồ sơ có đủ điều kiện vay vốn hay không\ncần có rất nhiều yếu tố như: tuổi, điểm tín dụng, mục đích vay,",
         "Determining whether a loan application is eligible\nrequires many factors such as age, credit score, loan purpose,",
         0.5, 4.5),
        ("Nhưng để đơn giản, ta giả sử quy trình thẩm định rút gọn của ngân hàng\n còn 2 bước chính.",
         "But to simplify, we assume the bank's appraisal process\nis simplified into 2 key steps.",
         0.5, 4.5),
        ("Bước 1: Xác định mức thu nhập.\nBước 2: Kiểm tra lịch sử tín dụng.",
         "Step 1: Assess income level.\nStep 2: Review credit history.",
         0.2, 4.5),
        ("Sau đó ngân hàng mới quyết định\ncó duyệt khoản vay hay không.",
         "Then the bank decides\nwhether to approve the loan.",
         0.2, 4.0),
    ],
    "s3_tree_intro": [
        ("Ta mô hình hóa quá trình này\nbằng một cây quyết định.",
         "We model this process\nusing a decision tree.",
         0.3, 4.2),
    ],
    "s3_tree_data": [
        ("60% khách hàng có thu nhập cao.\n40% có thu nhập trung bình/thấp.",
         "60% of customers have high income.\n40% have average/low income.",
         0.2, 4.0),
        ("Thu nhập cao → 80% tín dụng tốt.\nThu nhập TB → 50% tín dụng tốt.",
         "High income → 80% good credit.\nAvg income → 50% good credit.",
         0.2, 4.0),
        ("Tín dụng tốt → 90% hoàn trả khoản vay.\nTín dụng TB + thu nhập cao → 70%.",
         "Good credit → 90% loan repayment.\nAvg credit + high income → 70%.",
         0.2, 4.5),
    ],
    "s4_path": [
        ("Đây là chuỗi xác suất có điều kiện.\nNhân xác suất trên cùng một nhánh.",
         "This is a chain of conditional probabilities.\nMultiply probabilities along a branch.",
         0.4, 5.0),
        ("Ví dụ: Thu nhập cao → Tín dụng tốt\n→ Khoản vay được hoàn trả.",
         "Example: High income → Good credit\n→ Loan repayment.",
         0.2, 4.0),
        ("P = 0.6 × 0.8 × 0.9 = 0.432",
         "P = 0.6 × 0.8 × 0.9 = 0.432",
         0.2, 3.8),
        ("Ngưỡng duyệt 70%: nhánh trên 70%\nđược tự động duyệt.",
         "70% threshold: branches above 70%\nare automatically approved.",
         0.2, 4.5),
    ],
    "s5_total": [
        ("Cộng xác suất tất cả nhánh\ndẫn đến 'Tự động duyệt vay'.",
         "Sum probabilities of all branches\nleading to 'Auto-approved'.",
         0.3, 4.5),
        ("Quy tắc cộng + nhân xác suất:\nP(Tự động duyệt vay) = 0.804 ≈ 80%",
         "Addition + Multiplication rules:\nP(Auto-approved) = 0.804 ≈ 80%",
         0.2, 5.0),
        ("Nhờ cây quyết định, ta có thể nhìn rõ\ntoàn bộ quy trình ra quyết định.",
         "The decision tree reveals\nthe entire decision-making process.",
         0.2, 4.0),
    ],
    "s6_summary": [
        ("Cây quyết định giúp mô hình hóa\nquy trình ra quyết định nhiều bước.",
         "Decision trees model\nmulti-step decision processes.",
         0.4, 5.0),
        ("Ứng dụng: Phân tích tín dụng,\nĐầu tư, Quản trị rủi ro.",
         "Applications: Credit analysis,\nInvestment, Risk management.",
         0.2, 4.5),
    ],
    "s7_keywords": [
        ("3 khái niệm: Cây quyết định,\nXác suất có điều kiện, Quy tắc nhân-cộng.",
         "3 concepts: Decision Tree,\nConditional Probability, Multiply-Add Rules.",
         0.3, 5.8),
    ],
    "s8_question": [
        ("Nếu xác suất duyệt giảm từ 0.9\nxuống 0.7, P tổng thể thay đổi thế nào?",
         "If approval probability drops from 0.9\nto 0.7, how does overall P change?",
         0.6, 6.5),
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
