"""
helpers.py – Các hàm dựng UI dùng chung cho tất cả scene.
"""

from manim import *
from config import FONT, C_DARK_BG, C_WHITE, C_GRAY
import textwrap

def auto_wrap(text, limit=30):
    """Tính năng ngắt dòng tự động nếu văn bản quá dài và chưa cố tình ngắt."""
    if "\n" in text:
        return text
    return textwrap.fill(text, width=limit)

def skill_pop_in(mobject, **kwargs):
    """Hiệu ứng xuất hiện Nhanh (Scale & Ease Out) thay thế cho FadeIn."""
    kwargs.setdefault("rate_func", rate_functions.ease_out_back)
    kwargs.setdefault("run_time", 0.6)
    if "scale" not in kwargs:
        kwargs["scale"] = 0.5 # Default pop-in scale
    return FadeIn(mobject, **kwargs)


def rnode(text, fill, text_color=WHITE, w=3.8, h=0.88, fs=18, bold=False):
    """Nút bo góc có nhãn văn bản ở giữa."""
    rect = RoundedRectangle(
        corner_radius=0.2, width=w, height=h,
        fill_color=fill, fill_opacity=1,
        stroke_color=fill, stroke_width=0,
    )
    lbl = Text(auto_wrap(text, 25), font=FONT, font_size=fs,
               color=text_color,
               weight=BOLD if bold else NORMAL,
               line_spacing=0.9)
    lbl.move_to(rect.get_center())
    if lbl.width > 0 and lbl.width > rect.width - 0.22:
        lbl.scale((rect.width - 0.22) / lbl.width)
    return VGroup(rect, lbl)


def info_card(title_txt, body_txt, accent, w=7.4, h=2.0):
    """Card thông tin có thanh màu trên cùng."""
    bg      = RoundedRectangle(corner_radius=0.25, width=w, height=h,
                                fill_color=C_DARK_BG, fill_opacity=1,
                                stroke_color=accent, stroke_width=2)
    top_bar = RoundedRectangle(corner_radius=0.25, width=w, height=0.12,
                                fill_color=accent, fill_opacity=1,
                                stroke_width=0)
    top_bar.align_to(bg, UP)
    t = Text(auto_wrap(title_txt, 30), font=FONT, font_size=19, color=accent, weight=BOLD)
    b = Text(auto_wrap(body_txt, 35),  font=FONT, font_size=17, color=C_WHITE, line_spacing=1.3)
    
    if t.width > w - 0.4:
        t.scale_to_fit_width(w - 0.4)
    if b.width > w - 0.4:
        b.scale_to_fit_width(w - 0.4)
        
    t.next_to(bg.get_top(), DOWN, buff=0.24)
    b.next_to(t, DOWN, buff=0.16)
    if b.get_bottom()[1] < bg.get_bottom()[1] + 0.1:
        b.scale(0.9)
    return VGroup(bg, top_bar, t, b)


def sec_title(txt, color=None, fs=19):
    """Tiêu đề section in đậm."""
    from config import C_PRIMARY
    color = color or C_PRIMARY
    return Text(txt, font=FONT, font_size=fs, color=color, weight=BOLD)


def load_icon(icon_name, width=0.8, bg_color=None):
    """Tạo icon đơn giản từ shape Manim (dùng text + circle)."""
    from config import C_WHITE
    
    if bg_color is None:
        bg_color = GRAY
    
    # Tạo circle background
    circle = Circle(radius=width/2, fill_color=bg_color, fill_opacity=0.9, stroke_width=0)
    
    # Symbol text dựa trên icon_name (dùng character đơn giản, không emoji)
    icon_symbols = {
        "icon_customer":      "C",
        "icon_income_high":   "$",
        "icon_income_avg":    "M", 
        "icon_credit_good":   "✓",
        "icon_credit_avg":    "!",
        "icon_approve":       "✓",
        "icon_reject":        "✕",
        "icon_process":       "→",
        "icon_probability":   "Σ",
        "icon_risk":          "Z",
        "icon_decision_tree": "T",
    }
    
    symbol = icon_symbols.get(icon_name, "●")
    
    # Adjust font size based on symbol
    if symbol in ["$", "M", "C", "T", "Σ"]:
        fs = int(width * 50)
    else:
        fs = int(width * 48)
    
    icon_text = Text(symbol, font_size=fs, color=C_WHITE, weight=BOLD)
    icon_text.move_to(circle.get_center())
    
    return VGroup(circle, icon_text)


def flow_block(label_top, label_bot, color, w=None, h=0.85):
    """Khối bước trong sơ đồ luồng. Width tự động bó theo text."""
    dot = Dot(radius=0.12, color=color)
    t1  = Text(auto_wrap(label_top, 30), font=FONT, font_size=16, color=color, weight=BOLD)
    t2  = Text(auto_wrap(label_bot, 30), font=FONT, font_size=18, color=C_WHITE)
    inner = VGroup(dot, VGroup(t1, t2).arrange(DOWN, buff=0.05, aligned_edge=LEFT))
    inner.arrange(RIGHT, buff=0.25)
    
    # Auto-fit width limit 7.5
    actual_width = w if w is not None else min(inner.width + 0.8, 7.5)
    if inner.width > actual_width - 0.4:
        inner.scale_to_fit_width(actual_width - 0.4)
        
    bg  = RoundedRectangle(corner_radius=0.18, width=actual_width, height=h,
                            fill_color=C_DARK_BG, fill_opacity=1,
                            stroke_color=color, stroke_width=1.8)
    inner.move_to(bg.get_center())
    return VGroup(bg, inner)
