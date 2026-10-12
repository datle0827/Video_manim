"""
scene_s6.py – S6: Phương sai
"""

from manim import *
from config import FONT, C_SUCCESS, C_PRIMARY, C_WHITE, C_WARNING, C_GRAY, C_DANGER, SCRIPTS, SUBS
from helpers import skill_pop_in

class SceneSummaryMixin:
    def scene_summary(self):
        ttl = self.create_title("Phương sai Var(X)")
        
        # We start by displaying the numberline again from previous scene
        nl = NumberLine(x_range=[-1, 4, 1], length=6, color=C_WHITE, include_numbers=True).move_to([0, 1.5, 0])
        dot = Dot(nl.n2p(1.1), color=C_SUCCESS, radius=0.1)

        part1_script = "Tuy nhiên, chỉ biết trung bình là chưa đủ."
        with self.voiceover(text=part1_script) as tracker:
            self.update_subtitle("Tuy nhiên, chỉ biết trung bình là chưa đủ.", style="default")
            self.sp(Write(ttl, run_time=min(0.5, tracker.duration * 0.5)))
            self.sp(Create(nl), FadeIn(dot), run_time=0.5)
            self.wait(tracker.duration)

        part2_script = "Trong thực tế, số lỗi có thể dao động giữa các ngày,"
        with self.voiceover(text=part2_script) as tracker:
            self.update_subtitle("Trong thực tế số lỗi có thể\ndao động giữa các ngày,", style="default")
            
            # Animate dot bouncing randomly
            dot.time = 0
            dot.base_pos = nl.n2p(1.1)
            def shake(m, dt):
                m.time += dt
                # move dot between 0 and 3
                new_x = 1.1 + np.sin(m.time * 8) * 1.5
                m.move_to(nl.n2p(new_x))
            dot.add_updater(shake)
            self.wait(tracker.duration)

        part3_script = "có hôm không có lỗi, nhưng cũng có hôm lên tới 3 lỗi."
        with self.voiceover(text=part3_script) as tracker:
            self.update_subtitle("có hôm không có lỗi,\nnhưng có hôm lên tới 3 lỗi.", style="default")
            self.wait(tracker.duration)

        dot.clear_updaters()
        self.play(dot.animate.move_to(nl.n2p(1.1)))

        part4_script = "Để đo mức độ biến động này, ta sử dụng phương sai."
        with self.voiceover(text=part4_script) as tracker:
            self.update_subtitle("Để đo mức độ biến động này,\nta sử dụng Phương sai.", style="default")
            var_band = Rectangle(width=2.5, height=0.4, color=C_DANGER, fill_opacity=0.3, stroke_width=0).move_to(nl.n2p(1.1))
            self.sp(FadeIn(var_band, run_time=1.0))
            self.wait(tracker.duration)

        part5_script = "Ta tính được kỳ vọng của X bình phương bằng 2 phẩy 1,"
        with self.voiceover(text=part5_script) as tracker:
            self.update_subtitle("Ta tính được E(X²) = 2.1.", style="default")
            eq1 = MathTex("E(X^2)", "=", "2.1", font_size=40, color=C_WHITE).move_to([0, -0.2, 0])
            self.sp(skill_pop_in(eq1, run_time=1.0))
            self.wait(tracker.duration)

        part6_script = "từ đó phương sai của X bằng 2 phẩy 1 trừ đi 1 phẩy 1 bình phương, bằng 0 phẩy 89."
        with self.voiceover(text=part6_script) as tracker:
            self.update_subtitle("Suy ra Var(X) = 2.1 - (1.1)² = 0.89", style="default")
            eq2 = MathTex("Var(X)", "=", "2.1 - 1.1^2 = 0.89", font_size=44, color=C_DANGER).next_to(eq1, DOWN, buff=0.8)
            self.sp(skill_pop_in(eq2, run_time=1.0))
            self.wait(tracker.duration)
            
        part7_script = "Phương sai đo lường sự dao động nhất định quanh giá trị trung bình."
        with self.voiceover(text=part7_script) as tracker:
            self.update_subtitle("Phương sai đo lường sự dao động\nnhất định quanh giá trị trung bình.", style="default")
            # emphasize the band
            self.sp(Circumscribe(var_band, color=C_WARNING, run_time=1.0))
            self.wait(tracker.duration)

        self._lift()
        self.clear_content()

