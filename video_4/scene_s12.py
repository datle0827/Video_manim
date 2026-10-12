"""
scene_s12.py – S12: Tổng kết
"""

from manim import *
from config import FONT, C_PRIMARY, C_SUCCESS, C_WARNING, C_GRAY, C_WHITE, C_DANGER, FAMI_BLUE, FAMI_CYAN
from helpers import skill_pop_in

class SceneS12Mixin:
    def scene_s12(self):
        ttl = self.create_title("Tổng kết Bài học")

        # 1. Outlier Title & Underline Group
        outlier_txt = Text("Outlier", font=FONT, font_size=52, color=C_DANGER, weight=BOLD).move_to([0, 0.5, 0])
        underline = Underline(outlier_txt, color=C_DANGER, stroke_width=3)
        outlier_grp = VGroup(outlier_txt, underline)

        # 2. Scatter Plot Layout (S2 style but compact)
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            x_length=5.2,
            y_length=3.6,
            axis_config={"color": C_GRAY},
        ).move_to([0, 0.2, 0])

        # Dense noisy data points scattered realistically around the green line (y = 0.6 * x + 1.4)
        normal_data = [
            [1.5, 2.1], [2.0, 2.9], [2.5, 2.6], [3.0, 3.5], [3.5, 3.2],
            [4.0, 4.1], [4.5, 3.8], [5.0, 4.7], [5.5, 4.4], [6.0, 5.3],
            [6.5, 5.0], [7.0, 5.9], [7.5, 5.6], [8.0, 6.5]
        ]
        dots = VGroup(*[
            Dot(ax.c2p(x, y), color=C_PRIMARY, radius=0.08)
            for x, y in normal_data
        ])

        # Outlier red dot (extreme leverage)
        outlier_dot = Dot(ax.c2p(8.0, 2.0), color=C_DANGER, radius=0.12)

        # Regression lines: Base (green) and Skewed (red)
        line_old = Line(ax.c2p(1, 2.0), ax.c2p(8, 6.2), color=C_SUCCESS, stroke_width=3)
        line_new = Line(ax.c2p(1, 2.3), ax.c2p(8, 3.0), color=C_DANGER, stroke_width=3)

        plot_grp = VGroup(ax, dots, line_old, line_new)

        # 3. Cook's Distance Screen elements - Title is boxed, description is unboxed
        cook_title = Text("Cook's Distance", font=FONT, font_size=40, color=FAMI_BLUE, weight=BOLD)
        cook_box = RoundedRectangle(
            width=cook_title.width + 0.6, height=cook_title.height + 0.4, corner_radius=0.12,
            color=FAMI_BLUE, fill_color="#0f172a", fill_opacity=0.9, stroke_width=3
        )
        cook_title_grp = VGroup(cook_box, cook_title).move_to([0, 0.8, 0])
        cook_title.move_to(cook_box.get_center())

        desc_l1 = Text("Đo lường mức độ ảnh hưởng thực tế", font=FONT, font_size=20, color=C_WHITE)
        desc_l2 = Text("của từng điểm dữ liệu lên các hệ số của mô hình.", font=FONT, font_size=20, color=C_WHITE)
        desc_card = VGroup(desc_l1, desc_l2).arrange(DOWN, buff=0.15).next_to(cook_title_grp, DOWN, buff=0.6)

        # --- ANIMATION FLOW ---

        part1 = "Qua đó, ta thấy được Outlier không chỉ là những điểm khác biệt."
        with self.voiceover(text=part1) as tracker:
            self.update_subtitle("Ta thấy Outlier không chỉ là những điểm khác biệt.", style="default")
            self.sp(Write(ttl, run_time=0.5))
            
            # Show Outlier text & underline
            self.sp(Write(outlier_txt), Create(underline), run_time=0.8)
            self.wait(max(0.1, tracker.duration - 1.3))
 
        part2 = "Điều quan trọng là hiểu liệu chúng có đủ sức làm ảnh hưởng đến kết quả của mô hình hay không."
        with self.voiceover(text=part2) as tracker:
            self.update_subtitle("Quan trọng là liệu chúng có đủ sức\nlàm ảnh hưởng đến mô hình hay không.", style="default")
            
            # 1. First show the plot with the normal scattered points and the original green regression line
            # while the "Outlier" text morphs into the red dot.
            self.sp(
                ReplacementTransform(outlier_grp, outlier_dot),
                Create(ax), FadeIn(dots),
                Create(line_old),
                run_time=1.2
            )
            self.wait(0.4)
            
            # 2. Then, the green line gets skewed/pulled down to the red line position due to the outlier's influence
            self.sp(
                Transform(line_old, line_new),
                run_time=1.2
            )
            self.wait(max(0.1, tracker.duration - 2.8))
 
        part3 = "Ngoài phương pháp IQR và độ đo Leverage, các nhà phân tích còn sử dụng một thước đo khác gọi là Cook's Distance"
        with self.voiceover(text=part3) as tracker:
            self.update_subtitle("Ngoài IQR và Leverage,\ncòn một thước đo gọi là Cook's Distance", style="default")
            
            # Fade out graph and show Cook's Distance title group
            self.sp(
                FadeOut(ax), FadeOut(dots), FadeOut(line_old),
                FadeOut(outlier_dot),
                run_time=0.6
            )
            self.sp(skill_pop_in(cook_title_grp, sound=True), run_time=0.8)
            self.sp(Flash(cook_box, color=FAMI_BLUE), run_time=0.6)
            self.wait(max(0.1, tracker.duration - 2.0))
 
        part4 = "để đo lường mức độ ảnh hưởng thực tế của từng điểm dữ liệu lên hệ số của mô hình. mà chúng ta sẽ tìm hiểu ở video sau."
        with self.voiceover(text=part4) as tracker:
            self.update_subtitle("để đo lường mức độ ảnh hưởng của từng điểm\nlên hệ số của mô hình.", style="default")
            
            # Show description card with fade in
            self.sp(FadeIn(desc_card), run_time=0.8)
            self.wait(max(0.1, tracker.duration - 0.8))

        # Fade out all elements
        all_mobs = VGroup(cook_title_grp, desc_card, ttl)
        self.sp(FadeOut(all_mobs), run_time=0.8)
        self.clear_content()
