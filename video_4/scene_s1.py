"""
scene_s1.py – S1: Câu hỏi mở đầu
"""

from manim import *
from config import FONT, C_PRIMARY, C_SUCCESS, C_DANGER, C_WARNING, C_GRAY, C_WHITE
from helpers import skill_pop_in

class SceneS1Mixin:
    def scene_s1(self):
        ttl = self.create_title("Ảnh hưởng của Outlier")

        # Create axes in the middle
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
        ax_grp = VGroup(grid_lines, ax, x_nums, y_nums)

        # Normal data points scattered realistically around y = 0.6x + 1.5
        normal_data = [
            [1.5, 2.2], [2.0, 3.0], [2.5, 2.7], [3.0, 3.6], [3.5, 3.3],
            [4.0, 4.2], [4.5, 3.9], [5.0, 4.8], [5.5, 4.5], [6.0, 5.4],
            [6.5, 5.1], [7.0, 6.0], [7.5, 5.7], [8.0, 6.6]
        ]
        dots = VGroup(*[
            Dot(ax.c2p(x, y), color=C_PRIMARY, radius=0.08)
            for x, y in normal_data
        ])

        # Regression line before outlier
        line_before = ax.plot(lambda x: 0.6 * x + 1.5, color=C_SUCCESS, stroke_width=4, x_range=[1.0, 9.0])
        lbl_before = Text("Mô hình ban đầu", font=FONT, font_size=16, color=C_SUCCESS).move_to([-1.8, -2.6, 0])

        # Outlier point (Leverage + Outlier)
        outlier = Dot(ax.c2p(8.5, 2.0), color=C_DANGER, radius=0.12)
        outlier_lbl = Text("Outlier", font=FONT, font_size=16, color=C_DANGER).next_to(outlier, DOWN, buff=0.2)

        # Regression line after outlier (bent/tilted downward)
        line_after = ax.plot(lambda x: 0.35 * x + 2.8, color=C_DANGER, stroke_width=4, x_range=[1.0, 9.0])
        lbl_after = Text("Bị bẻ cong", font=FONT, font_size=16, color=C_DANGER).move_to([1.8, -2.6, 0])

        part1_script = "Liệu chỉ một điểm dữ liệu bất thường có thể làm thay đổi hoàn toàn kết quả của một mô hình dự báo?"
        with self.voiceover(text=part1_script) as tracker:
            self.update_subtitle("Liệu một điểm dữ liệu bất thường", style="default")
            
            # Show title, axes and data points
            self.sp(Write(ttl, run_time=0.6))
            self.sp(Create(grid_lines), Create(ax), FadeIn(x_nums), FadeIn(y_nums), run_time=0.5)
            self.sp(LaggedStart(*[FadeIn(d, scale=0.5) for d in dots], lag_ratio=0.1), run_time=0.8)
            
            # Update subtitle for the second part of question
            self.update_subtitle("có thể làm sai lệch hoàn toàn mô hình?", style="default")
            
            # Show original regression line
            self.sp(Create(line_before), FadeIn(lbl_before), run_time=0.8)
            self.wait(1.0)

            # Pop in the outlier and show it bending the line
            self.sp(skill_pop_in(outlier, sound=True), FadeIn(outlier_lbl), run_time=0.6)
            self.wait(0.5)
            self.sp(
                ReplacementTransform(line_before, line_after),
                ReplacementTransform(lbl_before, lbl_after),
                run_time=1.0
            )
            self.wait(max(0.1, tracker.duration - 4.8))

        self._lift()
        self.clear_content()
