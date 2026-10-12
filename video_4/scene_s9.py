"""
scene_s9.py – S9: Tác động đến hồi quy
"""

from manim import *
from config import FONT, C_PRIMARY, C_SUCCESS, C_WARNING, C_GRAY, C_WHITE, C_DANGER
from helpers import skill_pop_in

class SceneS9Mixin:
    def scene_s9(self):
        ttl = self.create_title("Tác động đến Hồi quy")

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

        # Clustered normal blue data points in lower-left/mid range (x = 1 to 6)
        normal_data = [
            [1.5, 2.4], [2.0, 2.7], [3.0, 3.3], [4.0, 3.9], [4.5, 4.2],
            [5.5, 4.8], [6.0, 5.1]
        ]
        dots = VGroup(*[
            Dot(ax.c2p(x, y), color=C_PRIMARY, radius=0.08)
            for x, y in normal_data
        ])

        # Old regression line (Dashed / Gray)
        line_old = DashedVMobject(ax.plot(lambda x: 0.6 * x + 1.5, color=C_GRAY, stroke_width=3, x_range=[1.0, 9.0]))
        lbl_old = Text("Mô hình cũ (Không Outlier)", font=FONT, font_size=14, color=C_GRAY).move_to([-2.0, -2.6, 0])

        # High Leverage + High Outlierness point (x = 9.0, y = 1.0)
        bad_outlier = Dot(ax.c2p(9.0, 1.0), color=C_DANGER, radius=0.12)
        bad_lbl = Text("Outlier + Leverage lớn", font=FONT, font_size=14, color=C_DANGER).next_to(bad_outlier, UP, buff=0.2)

        # New regression line (Solid / Red) showing strong tilt/rotation
        line_new = ax.plot(lambda x: 0.25 * x + 2.4, color=C_DANGER, stroke_width=4, x_range=[1.0, 9.0])
        lbl_new = Text("Mô hình mới (Bị kéo lệch)", font=FONT, font_size=14, color=C_DANGER).move_to([2.0, -2.6, 0])

        # Curved arrow showing rotation direction
        # Pointing from old line position to new line position near x=9
        rot_arrow = CurvedArrow(
            start_point=ax.c2p(8.5, 6.6),
            end_point=ax.c2p(8.5, 4.52),
            color=C_WARNING,
            angle=-TAU/8
        )
        rot_lbl = Text("Xoay lệch!", font=FONT, font_size=14, color=C_WARNING).next_to(rot_arrow, RIGHT, buff=0.1)

        # --- ANIMATION FLOW ---

        part1_script = "Khi một điểm vừa bất thường vừa có Leverage cao xuất hiện, đường hồi quy có thể bị kéo lệch đáng kể."
        with self.voiceover(text=part1_script) as tracker:
            self.update_subtitle("Khi một điểm vừa bất thường \n vừa có Leverage cao xuất hiện", style="default")
            
            # Show original plot
            self.sp(Write(ttl, run_time=0.5))
            self.sp(Create(grid_lines), Create(ax), FadeIn(x_nums), FadeIn(y_nums), run_time=0.5)
            self.sp(LaggedStart(*[FadeIn(d, scale=0.5) for d in dots], lag_ratio=0.1), run_time=0.8)
            self.sp(Create(line_old), FadeIn(lbl_old), run_time=0.8)
            self.wait(1)

            # Add the dangerous outlier
            self.update_subtitle("đường hồi quy có thể bị kéo lệch đáng kể.", style="default")
            self.sp(skill_pop_in(bad_outlier, sound=True), FadeIn(bad_lbl), run_time=0.6)
            self.wait(1)

            # Rotate line and show new model
            self.sp(
                Create(line_new),
                FadeIn(lbl_new),
                Create(rot_arrow),
                FadeIn(rot_lbl),
                run_time=1.0
            )
            self.sp(Wiggle(lbl_new), Flash(bad_outlier, color=C_DANGER), run_time=0.8)
            self.wait(max(0.1, tracker.duration - 4.5))

        self._lift()
        self.clear_content()
