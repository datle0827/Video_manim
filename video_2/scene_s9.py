"""
scene_s9.py – S9: Câu hỏi mở
"""

from manim import *
from config import FONT, C_SUCCESS, C_PRIMARY, C_WHITE, C_WARNING, C_GRAY, C_PURPLE, SCRIPTS, SUBS
from helpers import skill_pop_in, flow_block, load_icon, rnode

class SceneQuestionMixin:
    def scene_question(self):
        ttl = self.create_title("Góc kỹ năng")

        # Frame for full question
        q_text = "Trong trường hợp rủi ro ngày càng lớn,\ndoanh nghiệp nên trực tiếp chịu rủi ro\nhay đầu tư giảm thiểu?"
        q_box = rnode(q_text, C_PURPLE, w=6.5, h=2.5, fs=24, bold=False).move_to([0, 0, 0])
        lbl = rnode("Câu Hỏi Dành Cho Bạn", C_WARNING, w=4.5, h=0.7, fs=26, bold=True).move_to([0, 1.25, 0])
        box_grp = VGroup(q_box, lbl)

        part1_script = "Câu hỏi dành cho bạn: Vậy trong trường hợp phần trăm rủi ro ngày càng lớn,"
        with self.voiceover(text=part1_script) as tracker:
            self.update_subtitle("Câu hỏi dành cho bạn:\nTrong trường hợp phần trăm rủi ro ngày càng lớn,", style="default")
            self.sp(Write(ttl, run_time=min(0.5, tracker.duration * 0.3)))
            self.sp(skill_pop_in(box_grp, run_time=0.8))
            self.wait(max(0.1, tracker.duration - 1.3))

        part2_script = "doanh nghiệp nên quyết định trực tiếp chịu rủi ro hay nâng cấp trang thiết bị để giảm thiểu?"
        with self.voiceover(text=part2_script) as tracker:
            self.update_subtitle("doanh nghiệp nên thiếp tục trực tiếp chịu rủi ro\nhay nâng cấp trang thiết bị để giảm thiểu?", style="default")
            self.sp(Flash(box_grp, color=C_WARNING, line_length=0.4, num_lines=12, flash_radius=3, run_time=1.5))
            
            # Subtle bounce
            box_grp.time = 0
            def bounce_scale(m, dt):
                m.time += dt
                m.shift(UP * np.sin(m.time * 8) * 0.02)
                
            box_grp.add_updater(bounce_scale)
            
            self.wait(tracker.duration)

        part3_script = "Hãy để lại câu trả lời của bạn dưới phần bình luận nhé! Xin chào và hẹn gặp lại ở các video tiếp theo của FaMI."
        with self.voiceover(text=part3_script) as tracker:
            self.update_subtitle("Hãy comment câu trả lời của bạn\nxuống dưới nhé!", style="default")
            
            # Make the question disappear
            self.sp(FadeOut(box_grp), FadeOut(ttl), run_time=0.5)
            
            # Show comment with icon
            comment_icon = load_icon("icon_comment", width=1.0, bg_color=C_SUCCESS)
            cta = rnode("Để lại bình luận nhé!", C_SUCCESS, w=5, h=1.0, fs=32, bold=True)
            cta_grp = VGroup(comment_icon, cta).arrange(DOWN, buff=0.5).move_to([0, 0, 0])
            
            self.sp(skill_pop_in(cta_grp, sound=True, run_time=0.5))
            self.wait(max(0.1, tracker.duration * 0.5 - 1.0))
            
            self.update_subtitle("Tạm biệt và hẹn gặp lại\ntrong các video tiếp theo!", style="default")
            self.wait(tracker.duration * 0.5)

        self._lift()
        self.clear_content()

