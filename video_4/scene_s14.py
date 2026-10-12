"""
scene_s14.py – S14: Câu hỏi gợi mở & Kết thúc
"""

from manim import *
from config import FONT, C_PRIMARY, C_SUCCESS, C_WARNING, C_GRAY, C_WHITE, C_DANGER, FAMI_BLUE, FAMI_CYAN
from helpers import skill_pop_in, load_icon, info_card

class SceneS14Mixin:
    def scene_s14(self):
        ttl = self.create_title("Câu hỏi dành cho bạn")

        # Question Card in the center (centered, aligned, snug fit)
        # q_title = Text("Lựa chọn phương án nào?", font=FONT, font_size=16, color=C_WARNING, weight=BOLD)
        q_l1 = Text("Loại bỏ điểm Outlier đó hay tìm kiếm", font=FONT, font_size=20, color=C_WHITE)
        q_l2 = Text("một mô hình phù hợp hơn?", font=FONT, font_size=20, color=C_WHITE, weight=BOLD, t2c={"Robust Regression": FAMI_BLUE})
        q_body = VGroup(q_l1, q_l2).arrange(DOWN, buff=0.1)
        
        card_content = VGroup(q_body).arrange(DOWN, buff=0.25).move_to([0, 1.2, 0])
        card_box = RoundedRectangle(
            width=q_body.width + 0.8, height=card_content.height + 0.6,
            corner_radius=0.15, color=C_WARNING, fill_color="#0f172a", fill_opacity=0.9, stroke_width=3
        ).move_to(card_content.get_center())
        
        card = VGroup(card_box, card_content)

        # Question mark highlight (positioned dynamically next to the card)
        q_mark = Text("?", font=FONT, font_size=72, color=C_DANGER, weight=BOLD).next_to(card_box, RIGHT, buff=0.3)

        # CTA social icons in the bottom half
        # Like
        icon_like = load_icon("icon_like", width=1.2, bg_color=C_SUCCESS)
        lbl_like = Text("Like", font=FONT, font_size=12, color=C_WHITE).next_to(icon_like, DOWN, buff=0.1)
        grp_like = VGroup(icon_like, lbl_like).move_to([-2.2, -1.6, 0])

        # Comment
        icon_comm = load_icon("icon_comment_round", width=1.2, bg_color=FAMI_BLUE)
        lbl_comm = Text("Bình luận", font=FONT, font_size=12, color=C_WHITE).next_to(icon_comm, DOWN, buff=0.1)
        grp_comm = VGroup(icon_comm, lbl_comm).move_to([0.0, -1.6, 0])

        # Follow/Subscribe
        icon_sub = load_icon("icon_follow", width=1.2, bg_color=C_DANGER)
        lbl_sub = Text("Đăng ký", font=FONT, font_size=12, color=C_WHITE).next_to(icon_sub, DOWN, buff=0.1)
        grp_sub = VGroup(icon_sub, lbl_sub).move_to([2.2, -1.6, 0])

        ctas_grp = VGroup(grp_like, grp_comm, grp_sub)

        # --- ANIMATION FLOW ---

        part1_1 = "Câu hỏi dành cho bạn, nếu một điểm dữ liệu vừa là Outlier vừa có Leverage cao."
        with self.voiceover(text=part1_1) as tracker:
            self.update_subtitle("Nếu điểm dữ liệu vừa là Outlier\nvừa có Leverage cao,", style="default")
            self.sp(Write(ttl, run_time=0.5))
            self.sp(skill_pop_in(card, sound=True), run_time=0.8)
            self.wait(max(0.1, tracker.duration - 1.3))

        part1_2 = "Liệu chúng ta nên loại bỏ nó hay tìm một mô hình phù hợp hơn?"
        with self.voiceover(text=part1_2) as tracker:
            self.update_subtitle("liệu chúng ta nên loại bỏ nó\nhay tìm một mô hình phù hợp hơn?", style="default")
            self.sp(skill_pop_in(q_mark, sound=True), run_time=0.6)
            self.sp(Wiggle(q_mark), run_time=0.8)
            self.wait(max(0.1, tracker.duration - 1.4))

        part2_1 = "Hãy để lại ý kiến của bạn dưới phần bình luận nhé!"
        with self.voiceover(text=part2_1) as tracker:
            self.update_subtitle("Hãy để lại ý kiến dưới phần bình luận nhé!", style="default")
            
            # 3D Flip Card Transition: pre-rotate ctas_grp and flip it in
            ctas_grp.rotate(angle=-PI/2, axis=UP)
            self.add(ctas_grp)
            self.sp(Rotate(ctas_grp, angle=PI/2, axis=UP), run_time=0.8)
            self.wait(max(0.1, tracker.duration - 0.8))
            
        part2_2 = "Xin chào và hẹn gặp lại ở các video tiếp theo của FaMI."
        with self.voiceover(text=part2_2) as tracker:
            self.update_subtitle("Xin chào và hẹn gặp lại trong các video tiếp theo!", style="default")
            # Wiggle comments to highlight
            self.sp(Wiggle(grp_comm), run_time=0.8)
            self.wait(max(0.1, tracker.duration - 0.8))

        self._lift()
        self.clear_content()
