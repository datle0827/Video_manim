"""
scene_s2.py – S2: Liên kết với video trước
"""

from manim import *
from config import FONT, C_PRIMARY, C_SUCCESS, C_WARNING, C_GRAY, C_WHITE, C_DANGER
from helpers import skill_pop_in

class SceneS2Mixin:
    def scene_s2(self):
        ttl = self.create_title("Dự báo Hồi quy")

        # Previous video thumbnail
        try:
            prev_video = ImageMobject(os.path.join(os.path.dirname(__file__), "video.png")).scale_to_fit_width(5.0).move_to([0, 0.4, 0])
        except Exception:
            # Fallback if image fails to load
            rect = RoundedRectangle(width=5.0, height=3.0, color=C_PRIMARY, fill_opacity=0.3)
            lbl = Text("Video trước: Dự đoán giá nhà", font=FONT, font_size=20, color=C_WHITE)
            prev_video = VGroup(rect, lbl).move_to([0, 0.4, 0])

        # Axes for scatter plot
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 100, 10],
            x_length=6.0,
            y_length=4.2,
            axis_config={"color": C_GRAY},
        ).move_to([0, 0.2, 0])
        
        # Grid lines for charts
        grid_lines = VGroup()
        for x in range(1, 10):
            grid_lines.add(DashedLine(ax.c2p(x, 0), ax.c2p(x, 100), color="#1e293b", stroke_width=1))
        for y in range(10, 100, 10):
            grid_lines.add(DashedLine(ax.c2p(0, y), ax.c2p(10, y), color="#1e293b", stroke_width=1))

        # Axis ticks/numbers
        x_nums = VGroup(*[
            Text(str(val), font=FONT, font_size=10, color=C_GRAY).next_to(ax.c2p(val, 0), DOWN, buff=0.22)
            for val in range(2, 10, 2)
        ])
        y_nums = VGroup(*[
            Text(str(val), font=FONT, font_size=10, color=C_GRAY).next_to(ax.c2p(0, val), LEFT, buff=0.22)
            for val in range(20, 100, 20)
        ])

        # Labels for axes (housing price theme: size vs price) - Positioned safely to prevent overlapping tick numbers
        x_lbl = Text("Diện tích (m²)", font=FONT, font_size=11, color=C_GRAY).next_to(ax.x_axis, DOWN, buff=0.5).shift(LEFT * 0.4)
        y_lbl = Text("Giá nhà (Tỷ)", font=FONT, font_size=11, color=C_GRAY).next_to(ax.y_axis, LEFT, buff=0.4).shift(UP * 0.2)

        # Scatter plot data scattered realistically around y = 9.5x + 5
        data_points = [
            [1.5, 16], [2.0, 28], [2.5, 26], [3.0, 37], [3.5, 34],
            [4.0, 47], [4.5, 44], [5.0, 57], [5.5, 53], [6.0, 66],
            [6.5, 63], [7.0, 76], [7.5, 72], [8.0, 85], [8.5, 82],
            [9.0, 95]
        ]
        dots = VGroup(*[
            Dot(ax.c2p(x, y), color=C_PRIMARY, radius=0.08)
            for x, y in data_points
        ])

        # Regression lines: old (original) and new (with outlier)
        line_old = ax.plot(lambda x: 9.5 * x + 5, color=C_SUCCESS, stroke_width=3.5, x_range=[1.0, 9.0])
        line_new = ax.plot(lambda x: 7.33 * x + 20, color=C_DANGER, stroke_width=4.0, x_range=[1.0, 9.0])

        # Outlier point matching dialogue (60m2, 10 billion)
        outlier_dot = Dot(ax.c2p(6.0, 100), color=C_DANGER, radius=0.12)
        outlier_lbl = Text("60 m² - 10 Tỷ", font=FONT, font_size=12, color=C_DANGER).next_to(outlier_dot, UP, buff=0.15)

        # --- ANIMATION FLOW ---

        part1_script = "Ở video trước, chúng ta đã sử dụng hồi quy để dự đoán giá nhà."
        with self.voiceover(text=part1_script) as tracker:
            self.update_subtitle("Ở video trước, chúng ta đã sử dụng hồi quy\nđể dự đoán giá nhà.", style="default")
            self.sp(Write(ttl, run_time=0.5))
            self.sp(FadeIn(prev_video, scale=0.8), run_time=0.8)
            self.wait(max(0.1, tracker.duration - 1.3))

        part2_1 = "Nhưng dữ liệu thực tế không phải lúc nào cũng hoàn hảo."
        with self.voiceover(text=part2_1) as tracker:
            self.update_subtitle("Nhưng dữ liệu thực tế không hoàn hảo.", style="default")
            
            # Shrink previous video to 0 and fade out (disappear completely)
            self.sp(
                prev_video.animate.scale(0.01).fade(1.0),
                run_time=0.8
            )
            self.remove(prev_video)
            
            # Reveal scatter plot gradually (Draw axes and grid lines slowly, do not pop them)
            self.sp(
                Create(ax),
                Create(grid_lines),
                FadeIn(x_nums),
                FadeIn(y_nums),
                Write(x_lbl),
                Write(y_lbl),
                run_time=1.5
            )
            # Fade in data dots
            self.sp(
                LaggedStart(*[FadeIn(d, scale=0.5) for d in dots], lag_ratio=0.1),
                run_time=1.0
            )
            # Draw the original regression line (old model)
            self.sp(
                Create(line_old),
                run_time=1.0
            )
            self.wait(max(0.1, tracker.duration - 3.5))

        part2_2 = "Giả sử có một ngôi nhà với diện tích chỉ 60 m² nhưng giá bán lên tới 10 tỷ đồng."
        with self.voiceover(text=part2_2) as tracker:
            self.update_subtitle("Ví dụ: diện tích 60 m² giá 10 tỷ đồng.", style="default")
            # Pop in the outlier dot and its label
            self.sp(
                skill_pop_in(outlier_dot, sound=True),
                FadeIn(outlier_lbl),
                run_time=0.8
            )
            # # Draw the new regression line pulled/skewed by the outlier
            # self.sp(
            #     Create(line_new),
            #     run_time=1.0
            # )
            self.wait(max(0.1, tracker.duration - 1.8))
            
        part2_3 = "Đây là một căn nhà đặc biệt,"
        with self.voiceover(text=part2_3) as tracker:
            self.update_subtitle("Đây là một căn nhà đặc biệt,", style="default")
            
            # Group all components of the graph
            graph_all = VGroup(ax, grid_lines, x_nums, y_nums, x_lbl, y_lbl, dots, line_old, line_new, outlier_lbl)
            
            # Scale down and push up the graph
            self.sp(
                graph_all.animate.scale(0.65).move_to([0, 2.0, 0]),
                outlier_dot.animate.move_to([0, -1.0, 0]),
                run_time=1.2
            )
            
            # Morph red outlier dot into green "Đặc biệt" text below the graph
            dac_biet_txt = Text("Đặc biệt", font=FONT, font_size=32, color=C_SUCCESS, weight=BOLD).move_to([0, -1.5, 0])
            self.sp(
                ReplacementTransform(outlier_dot, dac_biet_txt),
                run_time=0.8
            )
            self.wait(max(0.1, tracker.duration - 2.0))

        part2_4 = "hay chỉ đơn giản là dữ liệu bất thường?"
        with self.voiceover(text=part2_4) as tracker:
            self.update_subtitle("hay chỉ đơn giản là dữ liệu bất thường?", style="default")
            
            # Morph "Đặc biệt" into red "Bất thường?" text
            bat_thuong_txt = Text("Bất thường?", font=FONT, font_size=32, color=C_DANGER, weight=BOLD).move_to([0, -1.5, 0])
            self.sp(
                ReplacementTransform(dac_biet_txt, bat_thuong_txt),
                Flash(bat_thuong_txt, color=C_DANGER),
                run_time=1.0
            )
            self.wait(max(0.1, tracker.duration - 1.0))

        # Fade out everything gracefully
        self.sp(
            FadeOut(graph_all),
            FadeOut(bat_thuong_txt),
            FadeOut(ttl),
            run_time=0.8
        )
        self.clear_content()
