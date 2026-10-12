"""
scene_s2.py – S2: Mô tả bài toán
"""

from manim import *
from config import (
    FONT, CONTENT_BOT,
    C_WARNING, C_PURPLE, C_SUCCESS, C_GRAY, C_WHITE, C_DANGER,
    SCRIPTS, SUBS
)
from helpers import skill_pop_in, sec_title, flow_block, rnode

class SceneProblemMixin:
    def scene_problem(self):
        ttl = self.create_title("Mô tả bài toán")

        belt = Line(LEFT*3.5, RIGHT*3.5, stroke_width=12, color=C_GRAY).move_to([0, -0.2, 0])
        w1 = Circle(radius=0.4, color=C_GRAY, stroke_width=4).move_to([-3.5, -0.2, 0])
        w2 = Circle(radius=0.4, color=C_GRAY, stroke_width=4).move_to([3.5, -0.2, 0])
        
        boxes = VGroup()
        for i in range(7):
            b = Square(side_length=0.6, fill_color=C_SUCCESS, fill_opacity=1, stroke_width=0, color=C_WHITE).move_to([-5.25 + i*1.75, 0.4, 0])
            boxes.add(b)

        def move_boxes(grp, dt):
            grp.shift(RIGHT * dt * 2)
            for box in grp:
                if box.get_x() > 6.0:
                    box.set_x(box.get_x() - 7 * 1.75)
                    
        part1_script = "Trong một dây chuyền sản xuất,"
        with self.voiceover(text=part1_script) as tracker:
            self.update_subtitle("Trong một dây chuyền sản xuất,", style="default")
            self.sp(Write(ttl, run_time=min(0.5, tracker.duration * 0.3)))
            self.sp(Create(belt), Create(w1), Create(w2), run_time=0.3)
            self.sp(FadeIn(boxes), run_time=0.2)
            
            w1.add_updater(lambda m, dt: m.rotate(-dt*2))
            w2.add_updater(lambda m, dt: m.rotate(-dt*2))
            boxes.add_updater(move_boxes)
            self.wait(tracker.duration)
            
        part2_script = "không phải sản phẩm nào cũng đạt chất lượng hoàn hảo."
        with self.voiceover(text=part2_script) as tracker:
            self.update_subtitle("không phải sản phẩm nào\ncũng đạt chất lượng hoàn hảo.", style="default")
            boxes[2].set_fill(C_DANGER)
            self.wait(tracker.duration)

        part3_script = "Mỗi ngày, số lượng sản phẩm lỗi có thể thay đổi."
        with self.voiceover(text=part3_script) as tracker:
            self.update_subtitle("Mỗi ngày, số lượng sản phẩm lỗi\ncó thể thay đổi.", style="default")
            boxes[4].set_fill(C_DANGER)
            self.wait(tracker.duration)

        part4_script = "Để trả lời câu hỏi đó,"
        with self.voiceover(text=part4_script) as tracker:
            self.update_subtitle("Để trả lời câu hỏi đó,", style="default")
            self.wait(tracker.duration)

        part5_script = "chúng ta sử dụng một công cụ trong xác suất, đó là biến ngẫu nhiên rời rạc."
        with self.voiceover(text=part5_script) as tracker:
            self.update_subtitle("chúng ta sử dụng 1 công cụ xác suất,\nđó là: Biến ngẫu nhiên rời rạc.", style="default")
            # stop updaters and fade out conveyor 
            boxes.clear_updaters()
            w1.clear_updaters()
            w2.clear_updaters()
            conveyor_grp = VGroup(belt, w1, w2, boxes)
            self.sp(FadeOut(conveyor_grp, run_time=0.5))
            
            # Show big keyword
            kw = rnode("Biến ngẫu nhiên rời rạc", C_PURPLE, w=5.0, h=1.0, fs=28, bold=True).move_to([0, 0, 0])
            self.sp(skill_pop_in(kw, run_time=0.5))
            self.sp(Wiggle(kw, run_time=1.0))
            self.wait(max(0.1, tracker.duration - 2.0))
            
        self._lift()
        self.clear_content()

