"""
scene_s4.py – S4: Định nghĩa Outlier
"""

from manim import *
from config import FONT, C_PRIMARY, C_SUCCESS, C_WARNING, C_GRAY, C_WHITE, C_DANGER, FAMI_CYAN
from helpers import skill_pop_in
import random

class SceneS4Mixin:
    def scene_s4(self):
        ttl = self.create_title("Định nghĩa Outlier")

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
            Text(str(val), font=FONT, font_size=10, color=C_GRAY).next_to(ax.c2p(val, 0), DOWN, buff=0.22)
            for val in range(2, 10, 2)
        ])
        y_nums = VGroup(*[
            Text(str(val), font=FONT, font_size=10, color=C_GRAY).next_to(ax.c2p(0, val), LEFT, buff=0.22)
            for val in range(2, 10, 2)
        ])

        # Clustered normal data points
        normal_data = [
            [1.0, 1.5], [1.5, 2.0], [2.0, 1.8], [2.2, 2.5], [2.8, 2.2],
            [3.0, 3.0], [3.5, 2.8], [4.0, 3.5], [4.5, 3.2]
        ]
        dots = VGroup(*[
            Dot(ax.c2p(x, y), color=C_PRIMARY, radius=0.08)
            for x, y in normal_data
        ])

        # Outlier 1: High above (y-axis outlier)
        y_outlier = Dot(ax.c2p(3.0, 8.5), color=C_DANGER, radius=0.12)
        y_lbl = Text("?", font=FONT, font_size=32, color=C_DANGER, weight=BOLD).next_to(y_outlier, UP, buff=0.15)
        y_desc = Text("Bất thường Y", font=FONT, font_size=14, color=C_DANGER).next_to(y_lbl, UP, buff=0.05)
        grp_y = VGroup(y_outlier, y_lbl, y_desc)

        # Outlier 2: Far right (x-axis outlier)
        x_outlier = Dot(ax.c2p(9.0, 3.5), color=C_WARNING, radius=0.12)
        x_lbl = Text("?", font=FONT, font_size=32, color=C_WARNING, weight=BOLD).next_to(x_outlier, UP, buff=0.15)
        x_desc = Text("Bất thường X", font=FONT, font_size=14, color=C_WARNING).next_to(x_lbl, UP, buff=0.05)
        grp_x = VGroup(x_outlier, x_lbl, x_desc)

        # Distance lines
        cluster_center = ax.c2p(2.5, 2.2)
        line_to_y = DashedLine(start=cluster_center, end=ax.c2p(3.0, 8.5), color=C_GRAY, stroke_width=2)
        line_to_x = DashedLine(start=cluster_center, end=ax.c2p(9.0, 3.5), color=C_GRAY, stroke_width=2)

        # --- ANIMATION FLOW ---

        part1_script = "Outlier là những điểm dữ liệu nằm xa phần lớn các quan sát còn lại."
        with self.voiceover(text=part1_script) as tracker:
            self.update_subtitle("Outlier là những điểm dữ liệu nằm xa\nphần lớn các quan sát còn lại.", style="default")
            self.sp(Write(ttl, run_time=0.5))
            self.sp(Create(grid_lines), Create(ax), FadeIn(x_nums), FadeIn(y_nums), run_time=0.5)
            self.sp(LaggedStart(*[FadeIn(d, scale=0.5) for d in dots], lag_ratio=0.1), run_time=0.8)
            self.wait(0.3)
            self.sp(Create(line_to_y), Create(line_to_x), run_time=0.6)
            self.sp(skill_pop_in(grp_y, sound=True), skill_pop_in(grp_x, sound=True), run_time=0.8)
            self.wait(max(0.1, tracker.duration - 3.2))

        part2_script = "Tuy nhiên, với bộ dữ liệu hàng triệu điểm, chúng ta không thể chỉ nhìn bằng mắt để kết luận một điểm là Outlier."
        with self.voiceover(text=part2_script) as tracker:
            self.update_subtitle("Với bộ dữ liệu hàng triệu điểm, chúng ta không thể\nnhìn bằng mắt để kết luận một điểm là Outlier.", style="default")
            
            # Generate 150 random blue dots with shuffled locations
            random.seed(42)
            coords = []
            for _ in range(150):
                coords.append((random.uniform(0.5, 9.5), random.uniform(0.5, 9.5)))
            random.shuffle(coords)
            many_dots = VGroup(*[
                Dot(ax.c2p(x, y), color=C_PRIMARY, radius=0.06)
                for x, y in coords
            ])
            
            self.sp(
                FadeOut(line_to_y), FadeOut(line_to_x),
                FadeOut(y_lbl), FadeOut(y_desc),
                FadeOut(x_lbl), FadeOut(x_desc),
                y_outlier.animate.set_color(C_PRIMARY).scale(0.08 / 0.12),
                x_outlier.animate.set_color(C_PRIMARY).scale(0.08 / 0.12),
                run_time=1.0
            )
            self.sp(
                LaggedStart(*[FadeIn(d, scale=0.5) for d in many_dots], lag_ratio=0.015),
                run_time=2.5
            )
            self.wait(max(0.1, tracker.duration - 3.5))

        part3_script = "Hôm nay, chúng ta sẽ tìm hiểu 2 phương pháp để hỗ trợ việc này là quy tắc 1.5IQR và Độ đo Leverage."
        with self.voiceover(text=part3_script) as tracker:
            self.update_subtitle("Hôm nay, chúng ta sẽ tìm hiểu 2 phương pháp:\nquy tắc 1.5IQR và Độ đo Leverage.", style="default")
            
            all_plot_elements = VGroup(ax, grid_lines, x_nums, y_nums, dots, many_dots, y_outlier, x_outlier)
            self.sp(FadeOut(all_plot_elements), run_time=0.8)
            
            iqr_card_bg = RoundedRectangle(width=5.5, height=1, corner_radius=0.15, color=FAMI_CYAN, fill_color=FAMI_CYAN, fill_opacity=0.1, stroke_width=3).move_to([0, 0, 0])
            iqr_card_title = Text("Quy tắc 1.5IQR", font=FONT, font_size=24, color=FAMI_CYAN, weight=BOLD).move_to(iqr_card_bg.get_center())
            iqr_card = VGroup(iqr_card_bg, iqr_card_title)

            lev_card_bg = RoundedRectangle(width=5.5, height=1, corner_radius=0.15, color=C_WARNING, fill_color=C_WARNING, fill_opacity=0.1, stroke_width=3).move_to([0, -1.2, 0])
            lev_card_title = Text("Độ đo Leverage", font=FONT, font_size=24, color=C_WARNING, weight=BOLD).move_to(lev_card_bg.get_center())
            lev_card = VGroup(lev_card_bg, lev_card_title)

            self.sp(skill_pop_in(iqr_card, sound=True), run_time=0.8)
            self.wait(1.0)
            self.sp(
                iqr_card.animate.move_to([0, 1.2, 0]),
                skill_pop_in(lev_card, sound=True),
                run_time=0.8
            )
            self.wait(max(0.1, tracker.duration - 2.6))

        self._lift()
        self.clear_content()
