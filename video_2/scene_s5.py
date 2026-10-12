"""
scene_s5.py – S5: Kỳ vọng
"""

from manim import *
from config import FONT, C_SUCCESS, C_PRIMARY, C_WHITE, C_WARNING, C_GRAY, SCRIPTS, SUBS
from helpers import skill_pop_in

class SceneTotalProbMixin:
    def scene_total_prob(self):
        ttl = self.create_title("Giá trị Kỳ vọng E(X)")

        part1_script = "Từ đó, ta có thể tính được giá trị kỳ vọng của X,"
        with self.voiceover(text=part1_script) as tracker:
            self.update_subtitle("Từ đó, ta có thể tính được Kỳ vọng của X,", style="default")
            self.sp(Write(ttl, run_time=min(0.5, tracker.duration * 0.5)))
            self.wait(tracker.duration)

        part2_script = "tức là số lỗi trung bình mỗi ngày."
        with self.voiceover(text=part2_script) as tracker:
            self.update_subtitle("tức là số lỗi trung bình mỗi ngày.", style="default")
            self.wait(tracker.duration)

        part3_script = "Cụ thể: E của X bằng không nhân không phẩy ba, cộng một nhân không phẩy bốn, cộng hai nhân không phẩy hai, cộng ba nhân không phẩy một, bằng một phẩy một."
        eq1 = MathTex("E(X)", "=", "0(0.3) + 1(0.4) + 2(0.2) + 3(0.1)", font_size=36, color=C_WHITE).move_to([0, 1.2, 0])
        eq2 = MathTex("=", "1.1", font_size=48, color=C_WARNING).next_to(eq1, DOWN, buff=0.5)

        with self.voiceover(text=part3_script) as tracker:
            self.update_subtitle("Cụ thể: E(X) = 0×0.3 + 1×0.4\n+ 2×0.2 + 3×0.1 = 1.1", style="default")
            self.sp(skill_pop_in(eq1, run_time=1.0))
            self.sp(skill_pop_in(eq2, run_time=1.0))
            self.wait(max(0.1, tracker.duration - 2.0))

        # Graphics for E(X)
        nl = NumberLine(x_range=[-1, 4, 1], length=6, color=C_WHITE, include_numbers=True).move_to([0, -1.0, 0])
        pivot = Arrow(start=nl.n2p(1.1) + DOWN*1.5, end=nl.n2p(1.1) + DOWN*0.6, color=C_SUCCESS, stroke_width=6, max_tip_length_to_length_ratio=0.3)
        dot = Dot(nl.n2p(1.1), color=C_SUCCESS, radius=0.1)

        part4_script = "Điều này có nghĩa là, trung bình mỗi ngày có khoảng một phẩy một sản phẩm lỗi."
        with self.voiceover(text=part4_script) as tracker:
            self.update_subtitle("Nghĩa là: Trung bình mỗi ngày có khoảng\n1.1 sản phẩm lỗi.", style="default")
            self.sp(Create(nl), run_time=0.8)
            self.sp(skill_pop_in(pivot), skill_pop_in(dot), run_time=0.8)
            lbl = Text("1.1 (Trọng tâm)", font=FONT, font_size=18, color=C_SUCCESS).next_to(pivot, DOWN, buff=0.2)
            self.sp(skill_pop_in(lbl, run_time=0.5))
            self.wait(tracker.duration)

        self._lift()
        self.clear_content()

