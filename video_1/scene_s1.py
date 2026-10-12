"""
scene_s1.py – S1: Tình huống dẫn nhập
Thu thập audio khi gọi screen_intro() và đồng bộ với voiceover.
"""

from manim import *
from config import C_PRIMARY, C_SUCCESS, C_DANGER, C_WARNING, FONT, SCRIPTS
from helpers import skill_pop_in, rnode, load_icon
from config import audio_path


class SceneIntroMixin:
    def scene_intro(self):
        # Không dùng add_sound() vì đã dùng with self.voiceover() ở dưới
        
        # Thay khung textbox bằng title FaMI
        q = self.create_title("Làm thế nào để ra quyết định", "phê duyệt khoản vay?")

        person = Text("👤", font_size=80).move_to([0, 1.3, 0])  # Kéo lên
        dot    = Dot(radius=0.18, color=C_WARNING).move_to([0, 0.0, 0])  # Kéo lên

        ok_box = rnode("Duyệt vay", C_SUCCESS, w=3.4, h=1.0, fs=20)
        no_box = rnode("Từ chối",   C_DANGER,  w=3.4, h=1.0, fs=20)
        ok_box.move_to([-2.2, -1.8, 0])  # Kéo lên
        no_box.move_to([ 2.2, -1.8, 0])  # Kéo lên

        arr_ok = Arrow(dot.get_center(), ok_box.get_top(), color=C_SUCCESS,
                       buff=0.08, stroke_width=3)
        arr_no = Arrow(dot.get_center(), no_box.get_top(), color=C_DANGER,
                       buff=0.08, stroke_width=3)
        
        # VOICEOVER BLOCK - Tuân thủ quy tắc
        with self.voiceover(text=SCRIPTS["s1"]) as tracker:
            # Bắt buộc gọi subtitle ở dòng 1
            self.update_subtitle(
                "Làm thế nào để tự động xác định\nmột khoản vay có được phê duyệt?",
                style="default"
            )
            
            # Chia animation thành chunks, tuân thủ 80% rule
            # run_time tổng ≤ 0.8 * tracker.duration
            part1_time = min(1.2, tracker.duration * 0.2)
            part2_time = min(1.2, tracker.duration * 0.15)
            part3_time = min(1.2, tracker.duration * 0.2)
            part4_time = min(1.2, tracker.duration * 0.25)
            # Tổng ≈ 75% - hợp lệ!
            
            self.sp(Write(q, run_time=part1_time))
            self.sp(skill_pop_in(person, run_time=part2_time))
            self.sp(skill_pop_in(dot, run_time=0.3))
            self.sp(GrowArrow(arr_ok), GrowArrow(arr_no), run_time=part3_time)
            self.sp(
                skill_pop_in(ok_box, scale=0.85), 
                skill_pop_in(no_box, scale=0.85), 
                run_time=part4_time
            )
            
        # Manim tự chờ đến hết audio
        self._lift()
        self.clear_content()
