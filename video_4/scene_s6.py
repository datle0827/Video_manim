"""
scene_s6.py – S6: Plot twist: IQR chưa đủ
"""

from manim import *
from config import FONT, C_PRIMARY, C_SUCCESS, C_WARNING, C_GRAY, C_WHITE, C_DANGER
from helpers import skill_pop_in

class SceneS6Mixin:
    def scene_s6(self):
        ttl = self.create_title("Quy tắc 1.5 IQR")

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

        # Clustered normal blue data points scattered around y = 0.5x + 1.5
        normal_data = [
            [1.5, 2.05], [2.0, 2.75], [2.5, 2.50], [3.0, 3.25], [3.5, 3.05],
            [4.0, 3.75], [4.5, 3.50], [5.0, 4.25], [5.5, 4.05], [6.0, 4.75],
            [6.5, 4.50], [7.0, 5.25], [7.5, 5.05], [8.0, 5.75], [8.5, 5.50],
            [9.0, 6.25]
        ]
        dots = VGroup(*[
            Dot(ax.c2p(x, y), color=C_PRIMARY, radius=0.08)
            for x, y in normal_data
        ])

        # Original regression line (y = 0.5x + 1.5)
        line_before = ax.plot(lambda x: 0.5 * x + 1.5, color=C_SUCCESS, stroke_width=4, x_range=[1.0, 9.0])
        lbl_before = Text("Hồi quy ban đầu", font=FONT, font_size=14, color=C_SUCCESS).move_to([-2.0, -2.6, 0])

        # Vertical Outlier at the center of x (x = 5.0, y = 8.5) -> Low Leverage, High Outlierness
        outlier = Dot(ax.c2p(5.0, 8.5), color=C_DANGER, radius=0.12)
        outlier_lbl = Text("IQR Outlier (X trung tâm)", font=FONT, font_size=14, color=C_DANGER).next_to(outlier, UP, buff=0.2)

        # New regression line after adding this outlier (y = 0.5x + 2.0) -> slightly shifted up, same slope!
        line_after = ax.plot(lambda x: 0.5 * x + 2.0, color=C_WARNING, stroke_width=4, x_range=[1.0, 9.0])
        lbl_after = Text("Độ dốc hầu như không đổi", font=FONT, font_size=14, color=C_WARNING).move_to([2.0, -2.6, 0])

        part1_script = "Nhưng một điểm bất thường chưa chắc đã ảnh hưởng mạnh đến mô hình hồi quy."
        with self.voiceover(text=part1_script) as tracker:
            self.update_subtitle("Nhưng một điểm bất thường chưa chắc\nđã ảnh hưởng mạnh đến mô hình hồi quy.", style="default")
            
            # Show original plot
            self.sp(Write(ttl, run_time=0.5))
            self.sp(Create(grid_lines), Create(ax), FadeIn(x_nums), FadeIn(y_nums), run_time=0.5)
            self.sp(LaggedStart(*[FadeIn(d, scale=0.5) for d in dots], lag_ratio=0.1), run_time=0.8)
            self.sp(Create(line_before), FadeIn(lbl_before), run_time=0.8)
            self.wait(0.5)

            # Pop in vertical outlier
            self.sp(skill_pop_in(outlier, sound=True), FadeIn(outlier_lbl), run_time=0.6)
            self.wait(0.5)

            # Show line shift
            self.sp(
                ReplacementTransform(line_before, line_after),
                ReplacementTransform(lbl_before, lbl_after),
                run_time=1.0
            )
            self.sp(Wiggle(lbl_after), run_time=0.8)
            self.wait(max(0.1, tracker.duration - 4.5))

        self._lift()
        self.clear_content()
