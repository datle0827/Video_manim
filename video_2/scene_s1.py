"""
scene_s1.py – S1: Tình huống dẫn nhập
"""

from manim import *
import os
from config import C_PRIMARY, C_SUCCESS, C_DANGER, C_WARNING, C_GRAY, C_WHITE, FONT, SCRIPTS, SUBS
from helpers import skill_pop_in, rnode, load_icon

class SceneIntroMixin:
    def scene_intro(self):
        q = self.create_title("Làm thế nào để nhà máy", "kiểm soát lỗi hiệu quả?")

        factory_base = Rectangle(width=2.5, height=1.5, fill_color=C_PRIMARY, fill_opacity=1, stroke_width=0)
        roof1 = Polygon([-1.25, 0.75, 0], [-0.4, 1.5, 0], [-0.4, 0.75, 0], fill_color=C_PRIMARY, fill_opacity=1, stroke_width=0)
        roof2 = Polygon([-0.4, 0.75, 0], [0.45, 1.5, 0], [0.45, 0.75, 0], fill_color=C_PRIMARY, fill_opacity=1, stroke_width=0)
        roof3 = Polygon([0.45, 0.75, 0], [1.25, 1.5, 0], [1.25, 0.75, 0], fill_color=C_PRIMARY, fill_opacity=1, stroke_width=0)
        chimney = Rectangle(width=0.3, height=0.8, fill_color=C_GRAY, fill_opacity=1, stroke_width=0).move_to([0.9, 1.5, 0])
        door = Rectangle(width=0.6, height=0.8, fill_color="#0A0F1E", fill_opacity=1, stroke_width=0).move_to([0, -0.35, 0])
        factory_icon = VGroup(chimney, factory_base, roof1, roof2, roof3, door).scale(1.2).move_to([0, -0.5, 0])

        svg_path = os.path.join(os.path.dirname(__file__), "person.svg")
        person_icon = SVGMobject(svg_path, fill_color=C_WHITE).scale_to_fit_width(2.0).move_to([-0.5, -1.0, 0])
        
        q_mark = Text("?", font_size=120, color=C_WARNING).next_to(person_icon.get_top(), UR, buff=0.1)
        q_mark.t = 0
        q_mark.base_pos = q_mark.get_center()

        def bounce(mob, dt):
            mob.t += dt
            mob.move_to(mob.base_pos + UP * np.sin(mob.t * 6) * 0.2)

        part1_script = "Làm thế nào để một nhà máy có thể kiểm soát chất lượng sản phẩm một cách hiệu quả, "
        with self.voiceover(text=part1_script) as tracker:
            self.update_subtitle("Làm thế nào để một nhà máy\nkiểm soát chất lượng một cách hiệu quả,", style="default")
            self.sp(Write(q, run_time=min(1.0, tracker.duration * 0.3)))
            
            # Show factory first
            self.sp(skill_pop_in(factory_icon, sound=True, run_time=0.6))
            self.wait(max(0.1, tracker.duration - 0.6))
            
        part2_script = "khi số lượng sản phẩm lỗi mỗi ngày luôn thay đổi?"
        with self.voiceover(text=part2_script) as tracker:
            self.update_subtitle("khi số lượng sản phẩm lỗi\nmỗi ngày luôn thay đổi?", style="default")
            
            # Fade out factory, show person with question mark
            self.sp(FadeOut(factory_icon, run_time=0.4))
            q_mark.add_updater(bounce)
            
            self.sp(skill_pop_in(person_icon, sound=True, run_time=0.5), skill_pop_in(q_mark, scale=0.5, sound=True, run_time=0.5))
            
            self.wait(tracker.duration)
            
        q_mark.clear_updaters()
        self._lift()
        self.clear_content()

