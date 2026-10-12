"""
scene_s7.py – S7: Ứng dụng thực tiễn
"""

from manim import *
from config import FONT, C_SUCCESS, C_PRIMARY, C_WHITE, C_WARNING, C_GRAY, C_DANGER, SCRIPTS, SUBS
from helpers import skill_pop_in, load_icon

class SceneKeywordsMixin:
    def scene_keywords(self):
        ttl = self.create_title("Ứng dụng thực tiễn")

        part1_script = "Những kết quả này không chỉ mang ý nghĩa lý thuyết, mà còn có giá trị thực tiễn rất lớn. Giả sử mỗi sản phẩm lỗi"
        with self.voiceover(text=part1_script) as tracker:
            self.update_subtitle("Những kết quả này còn có giá trị\nthực tiễn rất lớn. Giả sử mỗi sản phẩm lỗi", style="default")
            self.sp(Write(ttl, run_time=min(0.5, tracker.duration * 0.3)))
            self.wait(tracker.duration)

        # Setup Left Column
        icon1 = load_icon("icon_reject", width=0.7, bg_color=C_DANGER).move_to([-2.0, 1.4, 0])
        pa1_lbl = Text("PA 1: Trực tiếp chịu lỗi", font=FONT, font_size=18, color=C_WARNING).next_to(icon1, DOWN, buff=0.3)
        pa1_eq = MathTex("1.1 \\times 500 = 550k", font_size=28, color=C_DANGER).next_to(pa1_lbl, DOWN, buff=1.0)
        
        part2_script = "gây thiệt hại năm trăm nghìn đồng. Khi đó, chi phí lỗi trung bình mỗi ngày sẽ là "
        with self.voiceover(text=part2_script) as tracker:
            self.update_subtitle("gây thiệt hại 500 nghìn đồng.\nKhi đó, chi phí lỗi trung bình sẽ là", style="default")
            self.sp(skill_pop_in(icon1), skill_pop_in(pa1_lbl), run_time=1.0)
            self.wait(tracker.duration)

        part3_script = "một phẩy một nhân năm trăm bằng năm trăm năm mươi nghìn đồng."
        with self.voiceover(text=part3_script) as tracker:
            self.update_subtitle("1.1 × 500 = 550 nghìn đồng/ngày.", style="default")
            self.sp(skill_pop_in(pa1_eq), run_time=0.8)
            self.wait(tracker.duration)

        # Setup Right Column
        icon2 = load_icon("icon_approve", width=0.7, bg_color=C_SUCCESS).move_to([2.0, 1.4, 0])
        pa2_lbl = Text("PA 2: Gắn hệ thống QA", font=FONT, font_size=18, color=C_WARNING).next_to(icon2, DOWN, buff=0.3)
        pa2_eq1 = Text("Hệ thống: +200k, Lỗi: 0.5", font=FONT, font_size=16, color=C_GRAY).next_to(pa2_lbl, DOWN, buff=0.3)
        pa2_eq2 = MathTex("0.5 \\times 500 + 200 = 450k", font_size=28, color=C_SUCCESS).move_to([2.0, pa1_eq.get_y(), 0])

        part4_script = "Bây giờ, nhà máy có thể cân nhắc một phương án khác: đầu tư hệ thống kiểm tra chất lượng với chi phí hai trăm nghìn mỗi ngày,"
        with self.voiceover(text=part4_script) as tracker:
            self.update_subtitle("Bây giờ, nhà máy có thể cân nhắc phương án 2:\nĐầu tư hệ thống kiểm tra 200 nghìn/ngày,", style="default")
            self.sp(skill_pop_in(icon2), skill_pop_in(pa2_lbl), run_time=1.0)
            self.wait(tracker.duration)

        part5_script = "giúp giảm số lỗi trung bình xuống còn không phẩy lăm lỗi."
        with self.voiceover(text=part5_script) as tracker:
            self.update_subtitle("giúp giảm số lỗi xuống còn 0.5 lỗi.", style="default")
            self.sp(skill_pop_in(pa2_eq1), run_time=0.8)
            self.wait(tracker.duration)

        part6_script = "Khi đó, tổng chi phí sẽ là không phẩy lăm nhân năm trăm cộng hai trăm bằng bốn trăm năm mươi nghìn đồng."
        with self.voiceover(text=part6_script) as tracker:
            self.update_subtitle("Khi đó, tổng chi phí sẽ là:\n0.5 × 500 + 200 = 450 nghìn đồng.", style="default")
            self.sp(skill_pop_in(pa2_eq2), run_time=1.0)
            self.wait(tracker.duration)

        # Greater Than sign
        eq_sign = MathTex(">", font_size=50, color=C_WHITE).move_to([0, pa1_eq.get_y(), 0])
        recov = RoundedRectangle(corner_radius=0.2, width=pa2_eq2.width + 0.4, height=0.8, color=C_SUCCESS, stroke_width=4).move_to(pa2_eq2)

        part7_script = "Như vậy, phương án hai có chi phí thấp hơn rõ rệt. Do đó, nhà máy nên ưu tiên đầu tư hệ thống kiểm tra chất lượng."
        with self.voiceover(text=part7_script) as tracker:
            self.update_subtitle("Như vậy, phương án 2 điểm chi phí tối ưu hơn.\nNhà máy nên đầu tư QA.", style="default")
            self.sp(skill_pop_in(eq_sign, scale=2.0), run_time=0.5)
            self.sp(Wiggle(pa1_eq), Wiggle(pa2_eq2), run_time=1.0)
            self.sp(Create(recov), run_time=0.5)
            self.sp(Flash(recov, color=C_SUCCESS))
            self.wait(max(0.1, tracker.duration - 2.5))

        self._lift()
        self.clear_content()

