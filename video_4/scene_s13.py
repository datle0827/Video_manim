"""
scene_s13.py – S13: Từ khóa chính
"""

from manim import *
from config import FONT, C_PRIMARY, C_SUCCESS, C_WARNING, C_GRAY, C_WHITE, C_DANGER, FAMI_BLUE, FAMI_CYAN
from helpers import skill_pop_in, rnode

class SceneS13Mixin:
    def scene_s13(self):
        ttl = self.create_title("Từ khóa")

        # Faded background scatter plot axes
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            x_length=6.0,
            y_length=4.5,
            axis_config={"color": C_GRAY},
        ).move_to([0, 0.4, 0]).set_opacity(0.25)

        # Scattered noisy background dots
        normal_data = [
            [1.5, 2.1], [2.0, 2.9], [2.5, 2.6], [3.0, 3.5], [3.5, 3.2],
            [4.0, 4.1], [4.5, 3.8], [5.0, 4.7], [5.5, 4.4], [6.0, 5.3],
            [6.5, 5.0], [7.0, 5.9], [7.5, 5.6], [8.0, 6.5]
        ]
        dots = VGroup(*[
            Dot(ax.c2p(x, y), color=C_PRIMARY, radius=0.08)
            for x, y in normal_data
        ]).set_opacity(0.25)

        bg_grp = VGroup(ax, dots)

        # Keyword blocks with brand colors
        kw1 = rnode("Outlier\n(Điểm dị biệt)", C_DANGER, w=2.8, h=0.8, fs=13, bold=True).move_to([-1.8, 1.4, 0])
        kw2 = rnode("IQR\n(Khoảng tứ phân vị)", FAMI_CYAN, w=2.8, h=0.8, fs=13, bold=True).move_to([1.8, 1.4, 0])
        kw3 = rnode("Leverage\n(Độ đòn bẩy)", C_WARNING, w=2.8, h=0.8, fs=13, bold=True).move_to([-1.8, -0.6, 0])
        kw4 = rnode("Hồi quy\nTuyến tính", C_SUCCESS, w=2.8, h=0.8, fs=13, bold=True).move_to([1.8, -0.6, 0])

        # --- ANIMATION FLOW ---

        part1 = "Các khái niệm chính trong video gồm: Outlier,"
        with self.voiceover(text=part1) as tracker:
            self.update_subtitle("Các khái niệm chính trong video gồm:\nOutlier,", style="default")
            
            # Show title and faded background
            self.sp(Write(ttl, run_time=0.5))
            self.sp(FadeIn(bg_grp), run_time=0.8)
            self.sp(skill_pop_in(kw1, sound=True), run_time=0.6)
            self.wait(max(0.1, tracker.duration - 1.9))

        part2 = "khoảng tứ phân vị IQR,"
        with self.voiceover(text=part2) as tracker:
            self.update_subtitle("khoảng tứ phân vị IQR,", style="default")
            self.sp(skill_pop_in(kw2, sound=True), run_time=0.6)
            self.wait(max(0.1, tracker.duration - 0.6))

        part3 = "Leverage,"
        with self.voiceover(text=part3) as tracker:
            self.update_subtitle("Leverage,", style="default")
            self.sp(skill_pop_in(kw3, sound=True), run_time=0.6)
            self.wait(max(0.1, tracker.duration - 0.6))

        part4 = "và Hồi quy tuyến tính."
        with self.voiceover(text=part4) as tracker:
            self.update_subtitle("và Hồi quy tuyến tính.", style="default")
            self.sp(skill_pop_in(kw4, sound=True), run_time=0.6)
            
            # Float effect: slow translation
            self.sp(
                kw1.animate.shift(UP*0.08),
                kw2.animate.shift(DOWN*0.08),
                kw3.animate.shift(UP*0.08),
                kw4.animate.shift(DOWN*0.08),
                run_time=0.8
            )
            self.wait(max(0.1, tracker.duration - 1.4))

        self._lift()
        self.clear_content()
