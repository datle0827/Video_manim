"""
scene_s4.py – S4: Quyết định đầu tư & Rủi ro
"""

from manim import *
from config import FONT, C_SUCCESS, C_PRIMARY, C_WHITE, C_WARNING, C_GRAY, C_DANGER, C_PURPLE, SCRIPTS, SUBS
from helpers import skill_pop_in, rnode, load_icon

class SceneSinglePathMixin:
    def scene_single_path(self):
        ttl = self.create_title("Phân bổ vốn tối ưu")

        # Initial large capital badge at center
        mb_icon = load_icon("icon_process", width=0.6, bg_color=C_WARNING)
        capital_txt = Text("Vốn: 100 Triệu VNĐ", font=FONT, font_size=18, color=C_WHITE, weight=BOLD)
        capital = VGroup(mb_icon, capital_txt).arrange(RIGHT, buff=0.3).scale(1.5).move_to([0, 0, 0])
        
        # Target small capital position
        small_capital_pos = [0, 1.8, 0]

        # 100% cho CTG option card (centered below capital initially)
        opt_a = rnode("100%  cho CTG", C_PRIMARY, w=3.2, h=0.8, fs=18, bold=True).move_to([0, -0.4, 0])
        arrow_to_a = Arrow(start=small_capital_pos + DOWN*0.2, end=opt_a.get_top(), color=C_WHITE, stroke_width=4)
        
        # Risk label
        risk_icon = load_icon("icon_shield_warning", width=0.6, bg_color=C_DANGER)
        risk_txt = Text("RỦI RO?", font=FONT, font_size=18, color=C_WHITE, weight=BOLD)
        risk_label = VGroup(risk_icon, risk_txt).arrange(RIGHT, buff=0.2).move_to([2.2, 0.2, 0])
        arrow_to_risk = Arrow(start=[-2.2, 0.2, 0] + RIGHT*1.6, end=risk_label.get_left(), color=C_DANGER, stroke_width=4)

        # Allocation circle (circle divided in 2 parts)
        circle_bg = Circle(radius=1.2, color=C_WHITE, stroke_width=4)
        sector_a = AnnularSector(inner_radius=0, outer_radius=1.2, start_angle=PI/3, angle=PI, color=C_PRIMARY, fill_opacity=0.8)
        sector_b = AnnularSector(inner_radius=0, outer_radius=1.2, start_angle=4*PI/3, angle=PI, color=C_SUCCESS, fill_opacity=0.8)
        dividing_line = Line(start=circle_bg.point_at_angle(PI/3), end=circle_bg.point_at_angle(4*PI/3), color=C_WHITE, stroke_width=4)
        allocation_circle = VGroup(sector_a, sector_b, circle_bg, dividing_line).move_to([-1.8, -0.6, 0])

        # Question mark and pointing arrow
        q_mark = Text("?", font_size=90, color=C_WARNING).move_to([1.8, -0.6, 0])
        arrow_to_q = Arrow(start=[-0.4, -0.6, 0], end=[1.2, -0.6, 0], color=C_WARNING, stroke_width=4)

        part1_script_1 = "Thoạt nhìn, nhiều người sẽ nghĩ rằng"
        with self.voiceover(text=part1_script_1) as tracker:
            self.update_subtitle("Thoạt nhìn, nhiều người sẽ nghĩ rằng", style="default")
            self.sp(Write(ttl, run_time=min(0.5, tracker.duration * 0.3)))
            self.sp(skill_pop_in(capital, sound=True, run_time=0.5))
            self.wait(0.2)
            
            # Shrink capital badge and move to top-center
            self.sp(capital.animate.scale(1/1.5).move_to(small_capital_pos), run_time=0.6)
            self.wait(max(0.1, tracker.duration - 1.3))

        part1_script_2 = "nên đầu tư toàn bộ vào cổ phiếu C T G vì lợi nhuận cao hơn."
        with self.voiceover(text=part1_script_2) as tracker:
            self.update_subtitle("nên đầu tư toàn bộ vào cổ phiếu CTG\nvì lợi nhuận cao hơn.", style="default")
            
            # Show the 100% cho CTG card and point arrow straight down to it
            self.sp(Create(arrow_to_a), run_time=0.4)
            self.sp(skill_pop_in(opt_a, sound=True, run_time=0.5))
            self.wait(max(0.1, tracker.duration - 0.9))

        part2_script = "Nhưng trong đầu tư, chúng ta còn phải quan tâm đến rủi ro."
        with self.voiceover(text=part2_script) as tracker:
            self.update_subtitle("Nhưng trong đầu tư, chúng ta còn phải quan tâm\nđến rủi ro.", style="default")
            
            # Move the investment card to the left and point updated arrow to it
            self.sp(
                opt_a.animate.move_to([-2.2, 0.2, 0]),
                arrow_to_a.animate.put_start_and_end_on(capital.get_bottom() + LEFT*0.3, [-2.2, 0.7, 0]),
                run_time=0.8
            )
            
            # Then reveal risk_label and create arrow pointing to it
            self.sp(Create(arrow_to_risk), run_time=0.4)
            self.sp(skill_pop_in(risk_label, sound=True, run_time=0.5))
            self.sp(Wiggle(risk_label, run_time=0.8))
            self.wait(max(0.1, tracker.duration - 2.0))

        part3_script = "Vậy nên phân bổ số tiền này như thế nào để danh mục ít rủi ro nhất?"
        with self.voiceover(text=part3_script) as tracker:
            self.update_subtitle("Vậy nên phân bổ số tiền này thế nào\nđể danh mục ít rủi ro nhất?", style="default")
            
            # Fade out risk elements and investment card
            self.sp(FadeOut(risk_label), FadeOut(arrow_to_risk), FadeOut(opt_a), FadeOut(arrow_to_a), run_time=0.4)
            
            # Draw the divided circle and arrow pointing to "?"
            self.sp(Create(allocation_circle), run_time=0.8)
            self.sp(Create(arrow_to_q), Write(q_mark), run_time=0.6)
            self.sp(Wiggle(q_mark, run_time=0.8))
            self.wait(max(0.1, tracker.duration - 2.6))

        self._lift()
        self.clear_content()
