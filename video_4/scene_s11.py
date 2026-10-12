"""
scene_s11.py – S11: Liên hệ thực tiễn
"""

from manim import *
from config import FONT, C_PRIMARY, C_SUCCESS, C_WARNING, C_GRAY, C_WHITE, C_DANGER, FAMI_BLUE, FAMI_CYAN
from helpers import skill_pop_in, load_icon

class SceneS11Mixin:
    def scene_s11(self):
        ttl = self.create_title("Ứng dụng Thực tiễn")

        # 4 Application Categories with matching SVG icons from asset folder
        # Top-Left: Tài chính (Finance) -> money bag
        icon_fin = load_icon("icon_process", width=1.5, bg_color=FAMI_BLUE)
        lbl_fin = Text("Tài chính", font=FONT, font_size=16, color=C_WHITE, weight=BOLD).next_to(icon_fin, DOWN, buff=0.15)
        grp_fin = VGroup(icon_fin, lbl_fin).move_to([-1.8, 1.2, 0])

        # Top-Right: Y tế (Healthcare) -> medical icon
        icon_med = load_icon("icon_medical", width=1.5, bg_color=C_DANGER)
        lbl_med = Text("Y tế", font=FONT, font_size=16, color=C_WHITE, weight=BOLD).next_to(icon_med, DOWN, buff=0.15)
        grp_med = VGroup(icon_med, lbl_med).move_to([1.8, 1.2, 0])

        # Bottom-Left: Sản xuất (Manufacturing) -> manufacture icon
        icon_prod = load_icon("icon_manufacture", width=1.5, bg_color=C_WARNING)
        lbl_prod = Text("Sản xuất", font=FONT, font_size=16, color=C_WHITE, weight=BOLD).next_to(icon_prod, DOWN, buff=0.15)
        grp_prod = VGroup(icon_prod, lbl_prod).move_to([-1.8, -1.2, 0])

        # Bottom-Right: Dự báo (Business Forecasting) -> bar chart
        icon_biz = load_icon("icon_probability", width=1.5, bg_color=C_SUCCESS)
        lbl_biz = Text("Dự báo kinh doanh", font=FONT, font_size=16, color=C_WHITE, weight=BOLD).next_to(icon_biz, DOWN, buff=0.15)
        grp_biz = VGroup(icon_biz, lbl_biz).move_to([1.8, -1.2, 0])

        part1_script = "Những kỹ thuật này được sử dụng rộng rãi trong tài chính, y tế, sản xuất và bất kỳ lĩnh vực nào dựa vào mô hình dự báo để ra quyết định."
        with self.voiceover(text=part1_script) as tracker:
            self.update_subtitle("Các kỹ thuật này được dùng rộng rãi\ntrong tài chính, y tế,", style="default")
            
            self.sp(Write(ttl, run_time=0.7))
            
            # Sequentially pop in each application group
            self.sp(skill_pop_in(grp_fin, sound=True), run_time=1.2)
            self.sp(skill_pop_in(grp_med, sound=True), run_time=1.2)
            
            self.update_subtitle("sản xuất và các lĩnh vực\ndựa vào dự báo để ra quyết định.", style="default")
            self.sp(skill_pop_in(grp_prod, sound=True), run_time=0.5)
            self.sp(skill_pop_in(grp_biz, sound=True), run_time=0.5)
            
            # Subtle zoom/scale-up animations to bring life to the icons
            self.sp(
                grp_fin.animate.scale(1.1),
                grp_med.animate.scale(1.1),
                grp_prod.animate.scale(1.1),
                grp_biz.animate.scale(1.1),
                run_time=1.0
            )
            self.sp(
                grp_fin.animate.scale(1/1.1),
                grp_med.animate.scale(1/1.1),
                grp_prod.animate.scale(1/1.1),
                grp_biz.animate.scale(1/1.1),
                run_time=0.8
            )
            self.wait(max(0.1, tracker.duration - 3.9))

        self._lift()
        self.clear_content()
