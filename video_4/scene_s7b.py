"""
scene_s7b.py – S7b: Tính chất của Leverage
"""

from manim import *
from config import FONT, C_PRIMARY, C_SUCCESS, C_WARNING, C_GRAY, C_WHITE, C_DANGER, FAMI_BLUE, FAMI_CYAN
from helpers import skill_pop_in

def get_math_design(tex, fallback_markup, font_size=24, color=WHITE):
    try:
        return MathTex(tex, font_size=font_size, color=color)
    except Exception:
        return MarkupText(fallback_markup, font=FONT, font_size=font_size - 4, color=color)

def get_range_formula(font_size=28, color=WHITE):
    try:
        return MathTex(r"\frac{1}{n} \le h_i \le 1", font_size=font_size, color=color)
    except Exception:
        num = MarkupText("1", font=FONT, font_size=font_size - 8, color=color)
        den = MarkupText("n", font=FONT, font_size=font_size - 8, color=color)
        line = Line(start=[-0.15, 0, 0], end=[0.15, 0, 0], stroke_width=2, color=color)
        num.next_to(line, UP, buff=0.08)
        den.next_to(line, DOWN, buff=0.08)
        frac = VGroup(num, line, den)
        suffix = MarkupText(" ≤ h<sub>i</sub> ≤ 1", font=FONT, font_size=font_size - 4, color=color)
        return VGroup(frac, suffix).arrange(RIGHT, buff=0.1)

class SceneS7bMixin:
    def scene_s7b(self):
        ttl = self.create_title("Tính chất của Leverage")

        # Left Card: Khoảng giá trị
        range_box = RoundedRectangle(
            width=3.6, height=2.2, corner_radius=0.12,
            color=FAMI_CYAN, fill_color="#0f172a", fill_opacity=0.9, stroke_width=2.5
        ).move_to([-2.0, 0.6, 0])
        range_title = Text("Khoảng giá trị", font=FONT, font_size=20, color=FAMI_CYAN, weight=BOLD).move_to([-2.0, 1.3, 0])
        range_formula = get_range_formula(font_size=28, color=C_WHITE).move_to([-2.0, 0.6, 0])
        range_desc = Text("Càng gần 1, điểm càng xa trung tâm.", font=FONT, font_size=12        , color=C_GRAY).move_to([-2.0, 0.0, 0])
        range_grp = VGroup(range_box, range_title, range_formula, range_desc)

        # Right Card: Tổng Leverage
        sum_box = RoundedRectangle(
            width=3.6, height=2.2, corner_radius=0.12,
            color=C_WARNING, fill_color="#0f172a", fill_opacity=0.9, stroke_width=2.5
        ).move_to([2.0, 0.6, 0])
        sum_title = Text("Tổng Leverage", font=FONT, font_size=20, color=C_WARNING, weight=BOLD).move_to([2.0, 1.3, 0])
        sum_formula = get_math_design(
            r"\sum h_i = k + 1",
            r"Σ h<sub>i</sub> = k + 1",
            font_size=28, color=C_WHITE
        ).move_to([2.0, 0.6, 0])
        sum_desc = Text("Trung bình = (k + 1)/n", font=FONT, font_size=18, color=C_GRAY).move_to([2.0, 0.0, 0])
        sum_grp = VGroup(sum_box, sum_title, sum_formula, sum_desc)
 
        # Bottom Card: Độc lập với Y
        prop_box = RoundedRectangle(
            width=7.6, height=1.4, corner_radius=0.12,
            color=C_SUCCESS, fill_color="#0f172a", fill_opacity=0.9, stroke_width=2.5
        ).move_to([0, -1.6, 0])
        # prop_title = Text("Đặc điểm Quan trọng", font=FONT, font_size=14, color=C_SUCCESS, weight=BOLD).move_to([0, -1.2, 0])
        prop_desc = Text("Càng có nhiều điểm dữ liệu nằm gần nhau,\nsức ảnh hưởng của điểm high leverage càng giảm.", font=FONT, font_size=14, color=C_WHITE).move_to([0, -1.6, 0])
        prop_grp = VGroup(prop_box, prop_desc)

        # --- ANIMATION FLOW ---

        part1_1 = "Leverage có một số tính chất như sau:"
        with self.voiceover(text=part1_1) as tracker:
            self.update_subtitle("Leverage có một số tính chất", style="default")
            self.sp(Write(ttl, run_time=0.5))
            self.wait(max(0.1, tracker.duration - 0.5))

        part1_2 = "Giá trị của nó luôn nằm trong khoảng từ một phần n đến một."
        with self.voiceover(text=part1_2) as tracker:
            self.update_subtitle("Giá trị của nó luôn nằm trong \n khoảng từ 1/n đến 1.", style="default")
            self.sp(skill_pop_in(range_grp, sound=True), run_time=0.8)
            self.wait(max(0.1, tracker.duration - 0.8))

        part1_3 = "Tổng tất cả các giá trị leverage của toàn bộ mẫu dữ liệu luôn bằng k cộng một, với k là số biến độc lập."
        with self.voiceover(text=part1_3) as tracker:
            self.update_subtitle("Tổng leverage toàn mẫu luôn bằng k + 1.", style="default")
            self.sp(skill_pop_in(sum_grp, sound=True), run_time=0.8)
            self.wait(max(0.1, tracker.duration - 0.8))

        part2_1 = "Và càng có nhiều điểm dữ liệu nằm gần nhau thì sức ảnh hưởng của điểm high leverage càng giảm."
        with self.voiceover(text=part2_1) as tracker:
            self.update_subtitle("Càng có nhiều điểm dữ liệu, ảnh \n hưởng của điểm high leverage càng giảm.", style="default")
            # self.sp(skill_pop_in(prop_grp, sound=True), run_time=0.8)
            # self.sp(Flash(prop_box, color=C_SUCCESS), run_time=0.5)
            # self.update_subtitle("hoàn toàn độc lập với biến phụ thuộc Y.", style="default")
            self.wait(max(0.1, tracker.duration - 1.5))

        # part2_2 = "Điều này có nghĩa là ta có thể phát hiện các điểm leverage cao ngay cả trước khi quan sát biến mục tiêu."
        # with self.voiceover(text=part2_2) as tracker:
        #     self.update_subtitle("Có thể phát hiện điểm Leverage cao trước khi biết Y.", style="default")
        #     self.wait(max(0.1, tracker.duration))

        self._lift()
        self.clear_content()
