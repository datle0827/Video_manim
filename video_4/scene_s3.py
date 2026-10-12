"""
scene_s3.py – S3: Đặt vấn đề
"""

from manim import *
from config import FONT, C_PRIMARY, C_SUCCESS, C_WARNING, C_GRAY, C_WHITE, C_DANGER
from helpers import skill_pop_in, rnode

class SceneS3Mixin:
    def scene_s3(self):
        ttl = self.create_title("Dữ liệu Thực tế")

        # Scatter plot axes
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            x_length=6.0,
            y_length=4.5,
            axis_config={"color": C_GRAY},
        ).move_to([0, 0.4, 0])

        # Grid lines for charts
        grid_lines = VGroup()
        for x in range(1, 10):
            grid_lines.add(DashedLine(ax.c2p(x, 0), ax.c2p(x, 10), color="#1e293b", stroke_width=1))
        for y in range(1, 10):
            grid_lines.add(DashedLine(ax.c2p(0, y), ax.c2p(10, y), color="#1e293b", stroke_width=1))

        # Axis ticks/numbers
        x_nums = VGroup(*[
            Text(str(val), font=FONT, font_size=10, color=C_GRAY).next_to(ax.c2p(val, 0), DOWN, buff=0.1)
            for val in range(2, 10, 2)
        ])
        y_nums = VGroup(*[
            Text(str(val), font=FONT, font_size=10, color=C_GRAY).next_to(ax.c2p(0, val), LEFT, buff=0.1)
            for val in range(2, 10, 2)
        ])

        # Clustered normal blue data points
        normal_data = [
            [1.2, 2.0], [1.8, 2.3], [2.2, 2.6], [2.8, 2.9], [3.2, 3.2],
            [3.8, 3.5], [4.2, 3.8], [4.8, 4.1], [5.2, 4.4], [5.8, 4.7]
        ]
        dots = VGroup(*[
            Dot(ax.c2p(x, y), color=C_PRIMARY, radius=0.08)
            for x, y in normal_data
        ])

        # Outliers of different types
        # 1. Rare outlier (near the trend but far away) - Green/Yellow
        rare_outlier = Dot(ax.c2p(8.5, 6.5), color=C_SUCCESS, radius=0.12)
        rare_lbl = Text("Hiếm gặp?", font=FONT, font_size=16, color=C_SUCCESS).next_to(rare_outlier, UP, buff=0.15)
        
        # 2. Critical outlier (far from the trend, pulling the model) - Red
        bad_outlier = Dot(ax.c2p(5.0, 8.5), color=C_DANGER, radius=0.12)
        bad_lbl = Text("Sai lệch mô hình?", font=FONT, font_size=16, color=C_DANGER).next_to(bad_outlier, DOWN, buff=0.15)

        # Question Badge "Outlier?"
        outlier_badge = rnode("Outlier?", C_WARNING, w=2.5, h=0.7, fs=18, bold=True).move_to([0, -2.0, 0])

        part1_script = "Trong thực tế, dữ liệu luôn tồn tại những quan sát khác biệt. Một số chỉ đơn giản là hiếm gặp. Nhưng một số khác lại có thể làm sai lệch toàn bộ mô hình."
        with self.voiceover(text=part1_script) as tracker:
            self.update_subtitle("Trong thực tế, dữ liệu luôn tồn tại\nnhững quan sát khác biệt.", style="default")
            
            # Show axes, grid, numbers and normal dots
            self.sp(Write(ttl, run_time=0.5))
            self.sp(Create(grid_lines), Create(ax), FadeIn(x_nums), FadeIn(y_nums), run_time=0.5)
            self.sp(LaggedStart(*[FadeIn(d, scale=0.5) for d in dots], lag_ratio=0.1), run_time=0.8)
            self.wait(0.5)

            # Speak about rare cases
            self.update_subtitle("Một số chỉ đơn giản là hiếm gặp.", style="default")
            self.sp(skill_pop_in(rare_outlier, sound=True), FadeIn(rare_lbl), run_time=0.6)
            self.wait(0.8)

            # Speak about distorting the model
            self.update_subtitle("Nhưng một số khác có thể làm sai lệch toàn bộ mô hình.", style="default")
            self.sp(skill_pop_in(bad_outlier, sound=True), FadeIn(bad_lbl), run_time=0.6)
            self.wait(0.5)

            # Pop in "Outlier?" badge at bottom
            self.sp(skill_pop_in(outlier_badge, sound=True), run_time=0.6)
            self.sp(Wiggle(outlier_badge), run_time=0.8)
            self.wait(max(0.1, tracker.duration - 4.3))

        self._lift()
        self.clear_content()
