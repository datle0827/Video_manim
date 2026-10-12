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

import re

def escape_ampersand(text):
    if not isinstance(text, str):
        return text
    return re.sub(r"&(?!(?:amp|lt|gt|quot|apos);)", "&amp;", text)

def skill_pop_in(mobject, sound=False, **kwargs):
    """Hiệu ứng xuất hiện Nhanh (Scale & Ease Out) thay thế cho FadeIn."""
    kwargs.setdefault("rate_func", rate_functions.ease_out_back)
    kwargs.setdefault("run_time", 0.6)
    if "scale" not in kwargs:
        kwargs["scale"] = 0.5 # Default pop-in scale
    anim = FadeIn(mobject, **kwargs)
    if sound:
        anim.is_pop_in = True
    return anim


def make_centered_markup(text, font=FONT, font_size=18, color=WHITE, weight=NORMAL, line_spacing=0.15):
    lines = text.split('\n')
    mobs = [MarkupText(escape_ampersand(line), font=font, font_size=font_size, color=color, weight=weight) for line in lines]
    return VGroup(*mobs).arrange(DOWN, buff=line_spacing)


def rnode(text, fill, text_color=WHITE, w=3.8, h=0.88, fs=18, bold=False):
    """Nút bo góc có nhãn văn bản ở giữa."""
    rect = RoundedRectangle(
        corner_radius=0.2, width=w, height=h,
        fill_color=fill, fill_opacity=1,
        stroke_color=fill, stroke_width=0,
    )
    wrapped = auto_wrap(text, 25)
    lbl = make_centered_markup(wrapped, font=FONT, font_size=fs, color=text_color, weight=BOLD if bold else NORMAL, line_spacing=0.1)
    lbl.move_to(rect.get_center())
    if lbl.width > 0 and lbl.width > rect.width - 0.22:
        lbl.scale_to_fit_width(rect.width - 0.22)
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
    t = MarkupText(auto_wrap(escape_ampersand(title_txt), 30), font=FONT, font_size=19, color=accent, weight=BOLD)
    b = MarkupText(auto_wrap(escape_ampersand(body_txt), 35),  font=FONT, font_size=17, color=C_WHITE, line_spacing=1.3)
    
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
    return MarkupText(escape_ampersand(txt), font=FONT, font_size=fs, color=color, weight=BOLD)


def load_icon(icon_name, width=0.8, bg_color=None):
    """Tạo hoặc tải icon từ file SVG (nếu có trong /asset) bọc trong circle background."""
    import os
    
    if bg_color is None:
        bg_color = GRAY
    
    # Tạo circle background
    circle = Circle(radius=width/2, fill_color=bg_color, fill_opacity=0.9, stroke_width=0)
    
    # Mapping to SVG assets if they exist
    svg_mappings = {
        "icon_customer":      "businessman-svgrepo-com.svg",
        "icon_income_high":   "currency-revenue-svgrepo-com.svg",
        "icon_income_avg":    "cash-svgrepo-com.svg",
        "icon_credit_good":   "investor-invest-money-manager-growth-mindset-svgrepo-com.svg",
        "icon_credit_avg":    "list-svgrepo-com.svg",
        "icon_list":          "list-svgrepo-com.svg",
        "icon_approve":       "stock-up-svgrepo-com.svg",
        "icon_reject":        "danger-zone-svgrepo-com.svg",
        "icon_process":       "money-bag-svgrepo-com.svg",
        "icon_probability":   "profit-bar-chart-finance-svgrepo-com.svg",
        "icon_risk":          "danger-zone-svgrepo-com.svg",
        "icon_decision_tree": "stock-svgrepo-com.svg",
        "icon_portfolio":     "portfolio-svgrepo-com.svg",
        "icon_database":      "database-svgrepo-com.svg",
        "icon_percentage":    "percentage-svgrepo-com.svg",
        "icon_shield_warning":"shield-warning-svgrepo-com.svg",
        "icon_books":         "books-svgrepo-com.svg",
        "icon_money":         "money-1182-svgrepo-com.svg",
        "icon_covariate":     "covariate-svgrepo-com.svg",
        "icon_scales":        "scale-weight-weights-scales-balance-svgrepo-com.svg",
        "icon_comment_round": "chat-round-svgrepo-com.svg",
        "icon_like":          "like-svgrepo-com.svg",
        "icon_follow":        "user-follow-svgrepo-com.svg",
        "icon_stockprice":    "undraw_stock-prices_8nuz.svg",
        "icon_medical":       "medical-svgrepo-com.svg",
        "icon_manufacture":   "manufacture-svgrepo-com.svg",
    }
    
    if icon_name in svg_mappings:
        file_name = svg_mappings[icon_name]
        svg_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "asset", file_name)
        if os.path.exists(svg_path):
            svg_mob = SVGMobject(svg_path)
            svg_mob.scale_to_fit_width(width * 0.55)
            # Do not force set color to white to keep original vector asset colors
            # svg_mob.set_color(C_WHITE)
            svg_mob.move_to(circle.get_center())
            return VGroup(circle, svg_mob)

    if icon_name == "icon_comment":
        bubble = RoundedRectangle(corner_radius=0.1, width=width*0.55, height=width*0.4, fill_color=C_WHITE, fill_opacity=1, stroke_width=0)
        tri = Polygon([0,0,0], [width*0.1,0,0], [0,-width*0.15,0], fill_color=C_WHITE, fill_opacity=1, stroke_width=0)
        tri.move_to(bubble.get_bottom() + DOWN*0.04 + LEFT*0.08)
        icon_grp = VGroup(bubble, tri).move_to(circle.get_center())
        return VGroup(circle, icon_grp)

    # Fallback to Text symbol if no SVG matches or found
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
    
    if symbol in ["$", "M", "C", "T", "Σ"]:
        fs = int(width * 50)
    else:
        fs = int(width * 48)
    
    icon_text = MarkupText(symbol, font_size=fs, color=C_WHITE, weight=BOLD)
    icon_text.move_to(circle.get_center())
    
    return VGroup(circle, icon_text)


def flow_block(label_top, label_bot, color, w=None, h=0.85):
    """Khối bước trong sơ đồ luồng. Width tự động bó theo text."""
    dot = Dot(radius=0.12, color=color)
    t1  = MarkupText(auto_wrap(escape_ampersand(label_top), 30), font=FONT, font_size=16, color=color, weight=BOLD)
    t2  = MarkupText(auto_wrap(escape_ampersand(label_bot), 30), font=FONT, font_size=18, color=C_WHITE)
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


def math_tex(tex_str, fallback_str=None, font=FONT, font_size=24, color=WHITE, **kwargs):
    """
    Renders LaTeX math formula if LaTeX is installed, otherwise falls back
    to a beautiful MarkupText mobject (which supports <sub>, <sup>, etc.).
    """
    # Filter kwargs for MathTex (MathTex does not support font, weight, slant, etc.)
    math_kwargs = {}
    for k in ['stroke_width', 'fill_opacity', 'stroke_opacity']:
        if k in kwargs:
            math_kwargs[k] = kwargs[k]
            
    try:
        m = MathTex(tex_str, color=color, **math_kwargs)
        m.scale(font_size / 24)
        return m
    except Exception:
        text_to_render = fallback_str if fallback_str is not None else tex_str
        escaped_text = escape_ampersand(text_to_render)
        
        # Filter kwargs for MarkupText
        markup_kwargs = {}
        for k in ['weight', 'slant', 'stroke_width']:
            if k in kwargs:
                markup_kwargs[k] = kwargs[k]
                
        return MarkupText(escaped_text, font=font, font_size=font_size, color=color, **markup_kwargs)
