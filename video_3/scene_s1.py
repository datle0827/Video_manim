"""
scene_s1.py – S1: Tình huống dẫn nhập
"""

from manim import *
import os
from config import C_PRIMARY, C_SUCCESS, C_DANGER, C_WARNING, C_PURPLE, C_GRAY, C_WHITE, FONT, SCRIPTS, SUBS
from helpers import skill_pop_in, rnode, load_icon

class SceneIntroMixin:
    def scene_intro(self):
        q = self.create_title("Tối ưu danh mục đầu tư")

        # Vector stock-prices illustration in center representing the stock market
        stock_img = SVGMobject(os.path.join(os.path.dirname(__file__), "asset", "undraw_stock-prices_8nuz.svg")).scale_to_fit_width(4.2).move_to([0, 0.4, 0])

        # Left: Profit (Lợi nhuận)
        profit_icon = load_icon("icon_income_high", width=1.1, bg_color=C_SUCCESS).move_to([-1.6, -1.3, 0])
        profit_lbl = Text("Lợi nhuận", font=FONT, font_size=18, color=C_SUCCESS, weight=BOLD).next_to(profit_icon, DOWN, buff=0.15)
        profit_grp = VGroup(profit_icon, profit_lbl)
        arrow_profit = Arrow(start=[0, 2.0, 0] + LEFT*0.3, end=profit_icon.get_top(), color=C_SUCCESS, stroke_width=4)

        # Right: Risk (Rủi ro)
        risk_icon = load_icon("icon_shield_warning", width=1.1, bg_color=C_DANGER).move_to([1.6, -1.3, 0])
        risk_lbl = Text("Rủi ro", font=FONT, font_size=18, color=C_DANGER, weight=BOLD).next_to(risk_icon, DOWN, buff=0.15)
        risk_grp = VGroup(risk_icon, risk_lbl)
        arrow_risk = Arrow(start=[0, 2.0, 0] + RIGHT*0.3, end=risk_icon.get_top(), color=C_DANGER, stroke_width=4)

        part1_script_1 = "Làm thế nào để có thể xây dựng một danh mục đầu tư"
        with self.voiceover(text=part1_script_1) as tracker:
            self.update_subtitle("Làm thế nào để có thể xây dựng\nmột danh mục đầu tư", style="default")
            self.sp(Write(q, run_time=min(1.0, tracker.duration * 0.5)))
            
            # Show stock illustration
            self.sp(FadeIn(stock_img, shift=UP*0.3), run_time=0.8)
            self.wait(max(0.1, tracker.duration - 1.8))

        part1_script_2 = "vừa có lợi nhuận, vừa giảm thiểu rủi ro?"
        with self.voiceover(text=part1_script_2) as tracker:
            self.update_subtitle("vừa có lợi nhuận, vừa giảm thiểu rủi ro?", style="default")
            
            # 1. Thu nhỏ hình minh họa chứng khoán và đẩy lên trên
            self.sp(stock_img.animate.scale(0.5).move_to([0, 2.6, 0]), run_time=0.6)
            self.wait(0.2)
            
            # 2. Nói đến "lợi nhuận" -> chỉ sang nhánh Lợi nhuận
            self.sp(skill_pop_in(profit_grp, sound=True), Create(arrow_profit), run_time=0.6)
            self.wait(0.6)
            
            # 3. Nói đến "rủi ro" -> chỉ sang nhánh Rủi ro
            self.sp(skill_pop_in(risk_grp, sound=True), Create(arrow_risk), run_time=0.6)
            self.wait(max(0.1, tracker.duration - 2.6))
            
        self._lift()
        self.clear_content()
