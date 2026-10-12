"""
scene_s3.py – S3: Khai báo X
"""

from manim import *
from config import FONT, C_PRIMARY, C_PURPLE, C_WARNING, C_GRAY, C_WHITE, C_SUCCESS, C_DANGER, SCRIPTS, SUBS
from helpers import skill_pop_in, rnode, load_icon

class SceneTreeMixin: 
    def scene_tree(self): 
        ttl = self.create_title("Biến ngẫu nhiên X")
        
        part1_script = "Gọi X là số sản phẩm lỗi trong một ngày."
        with self.voiceover(text=part1_script) as tracker:
            self.update_subtitle("Gọi X là số sản phẩm lỗi trong 1 ngày.", style="default")
            self.sp(Write(ttl, run_time=min(0.5, tracker.duration * 0.3)))
            
            t_X = MathTex("X", "=", font_size=40)
            t_txt = Text("Số sản phẩm lỗi trong 1 ngày", font=FONT, font_size=24)
            eq_X = VGroup(t_X, t_txt).arrange(RIGHT, buff=0.2).set_color(C_SUCCESS).move_to([0, 1.5, 0])
            self.sp(skill_pop_in(eq_X, run_time=0.5))
            self.wait(tracker.duration)

        part2_script = "X là một biến ngẫu nhiên rời rạc,"
        with self.voiceover(text=part2_script) as tracker:
            self.update_subtitle("X là một biến ngẫu nhiên rời rạc,", style="default")
            var_lbl = Text("Biến ngẫu nhiên rời rạc", font=FONT, font_size=24, color=C_PURPLE).next_to(eq_X, DOWN, buff=0.5)
            self.sp(Write(var_lbl, run_time=0.5))
            self.wait(tracker.duration)

        part3_script = "vì nó nhận các giá trị nguyên đếm được như 0, 1, 2 hoặc 3."
        with self.voiceover(text=part3_script) as tracker:
            self.update_subtitle("vì nó nhận các giá trị đếm được\nnhư 0, 1, 2, hoặc 3.", style="default")
            # Hộp mô tả 0, 1, 2, 3
            boxes = VGroup()
            for val in [0, 1, 2, 3]:
                sq = Square(side_length=0.8, color=C_WARNING)
                txt = Text(str(val), font_size=32, color=C_WHITE).move_to(sq)
                boxes.add(VGroup(sq, txt))
            boxes.arrange(RIGHT, buff=0.5).next_to(var_lbl, DOWN, buff=0.8)
            
            in_tex = MathTex(r"\in", font_size=40).next_to(boxes, LEFT, buff=0.5)
            self.sp(Write(in_tex), run_time=0.2)
            self.sp(skill_pop_in(boxes, run_time=1.0))
            self.wait(tracker.duration)

        part4_script = "Ở đây, ta giả sử đang xét các lỗi nghiêm trọng trong một dây chuyền đã được kiểm soát tốt,"
        with self.voiceover(text=part4_script) as tracker:
            self.update_subtitle("Giả sử đây là dây chuyền\nđã được kiểm soát tốt,", style="default")
            note = Text("Dây chuyền kiểm soát tốt", font=FONT, font_size=20, color=C_GRAY).next_to(boxes, DOWN, buff=0.8)
            gear = load_icon("icon_process", width=0.6).next_to(note, LEFT, buff=0.2)
            self.sp(skill_pop_in(VGroup(note, gear)), run_time=0.5)
            self.wait(tracker.duration)

        part5_script = "nên số lỗi mỗi ngày thường nhỏ và nằm trong khoảng này."
        with self.voiceover(text=part5_script) as tracker:
            self.update_subtitle("nên số lỗi thường rất nhỏ\nvà nằm trong khoảng này.", style="default")
            self.sp(Circumscribe(boxes, color=C_SUCCESS, time_width=0.5, run_time=1.0))
            self.wait(max(0.1, tracker.duration - 1.0))

        self._lift()
        self.clear_content()

