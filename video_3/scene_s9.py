"""
scene_s9.py – S9: Câu hỏi tương tác & Kết thúc (Outro)
"""

from manim import *
from config import FONT, C_SUCCESS, C_PRIMARY, C_WHITE, C_WARNING, C_GRAY, C_PURPLE, C_DANGER, C_DARK_BG, SCRIPTS, SUBS
from helpers import skill_pop_in, info_card, rnode, load_icon, make_centered_markup

class SceneQuestionMixin:
    def scene_question(self):
        ttl = self.create_title("Câu hỏi tương tác")

        # Khung câu hỏi đơn giản, fit với chữ, nền xanh dương chữ trắng
        q_text = make_centered_markup(
            "Nếu thêm cổ phiếu C tương quan âm với CTG,\ndanh mục đầu tư có an toàn hơn không?",
            font=FONT, font_size=18, color=C_WHITE, line_spacing=0.15
        )
        q_bg = RoundedRectangle(
            corner_radius=0.2,
            width=q_text.width + 0.8,
            height=q_text.height + 0.6,
            fill_color=C_PRIMARY, fill_opacity=1,
            stroke_color=C_WHITE, stroke_width=2
        )
        # Định vị văn bản nằm chính giữa khung
        q_text.move_to(q_bg.get_center())
        q_card = VGroup(q_bg, q_text).move_to([0, 0.4, 0])
 
        # CTA - Comment
        icon_comment = load_icon("icon_comment_round", width=0.6, bg_color=C_WARNING)
        txt_comment = Text("Bình luận câu trả lời bên dưới nhé!", font=FONT, font_size=18, color=C_WHITE, weight=BOLD)
        comment_cta = VGroup(icon_comment, txt_comment).arrange(RIGHT, buff=0.3).move_to([0, -1.0, 0])
 
        # Like and Follow CTAs - Scaled up for better visibility
        like_icon = load_icon("icon_like", width=0.8, bg_color=C_PRIMARY)
        like_lbl = Text("Like", font=FONT, font_size=20, color=C_WHITE, weight=BOLD)
        like_cta = VGroup(like_icon, like_lbl).arrange(RIGHT, buff=0.2)
 
        follow_icon = load_icon("icon_follow", width=0.8, bg_color=C_SUCCESS)
        follow_lbl = Text("Theo dõi", font=FONT, font_size=20, color=C_WHITE, weight=BOLD)
        follow_cta = VGroup(follow_icon, follow_lbl).arrange(RIGHT, buff=0.2)
        
        cta_row = VGroup(like_cta, follow_cta).arrange(RIGHT, buff=1.0).scale(1.8).move_to([0, 0, 0])
 
        part1_script_1 = "Câu hỏi dành cho bạn: Nếu xuất hiện một cổ phiếu C có lợi nhuận tương đương nhưng có tương quan âm với C T G,"
        with self.voiceover(text=part1_script_1) as tracker:
            self.update_subtitle("Nếu xuất hiện cổ phiếu C cùng lợi nhuận\nnhưng tương quan âm với CTG,", style="default")
            self.sp(Write(ttl, run_time=0.5))
            
            # Xuất hiện khung hình chữ nhật trước
            self.sp(skill_pop_in(q_bg, sound=True), run_time=0.6)
            self.wait(0.2)
            
            # Viết dòng chữ thứ nhất từ từ theo thoại
            self.sp(Write(q_text[0]), run_time=max(1.0, tracker.duration - 1.4))
            self.wait(max(0.1, tracker.duration - (0.5 + 0.6 + 0.2 + max(1.0, tracker.duration - 1.4))))

        part1_script_2 = "liệu danh mục đầu tư có thể trở nên an toàn hơn nữa hay không?"
        with self.voiceover(text=part1_script_2) as tracker:
            self.update_subtitle("liệu danh mục đầu tư có thể\ntrở nên an toàn hơn nữa hay không?", style="default")
            
            # Viết dòng chữ thứ hai từ từ theo thoại và hơi zoom nhẹ khung câu hỏi
            self.sp(
                Write(q_text[1]),
                q_card.animate.scale(1.05),
                run_time=max(1.0, tracker.duration - 0.5)
            )
            self.wait(max(0.1, tracker.duration - max(1.0, tracker.duration - 0.5)))

        part2_script_1 = "Hãy để lại câu trả lời của bạn dưới phần bình luận nhé!"
        with self.voiceover(text=part2_script_1) as tracker:
            self.update_subtitle("Hãy để lại câu trả lời của bạn\ndưới phần bình luận nhé!", style="default")
            
            # Đẩy câu hỏi lên vị trí y=1.2 (dưới tiêu đề y=2.8) và hiện comment cta ở dưới y=-1.0
            self.sp(
                q_card.animate.scale(0.85).move_to([0, 1.2, 0]),
                skill_pop_in(comment_cta, sound=True),
                run_time=0.8
            )
            self.sp(Wiggle(comment_cta), run_time=1.0)
            self.wait(max(0.1, tracker.duration - 1.8))

        part2_script_2 = "Xin chào và hẹn gặp lại ở các video tiếp theo của FaMI."
        with self.voiceover(text=part2_script_2) as tracker:
            self.update_subtitle("Xin chào và hẹn gặp lại\nở các video tiếp theo của FaMI.", style="default")
            
            # Biến đổi comment_cta thành cta_row to giữa màn hình (ẩn q_card và tiêu đề đi)
            self.sp(
                FadeOut(q_card),
                FadeOut(ttl),
                ReplacementTransform(comment_cta, cta_row),
                run_time=0.8
            )
            # 3D Flip/Rotate cho Like và Theo dõi
            self.sp(
                Rotate(like_cta, angle=2*PI, axis=UP),
                Rotate(follow_cta, angle=2*PI, axis=UP),
                run_time=0.8
            )
            self.wait(1.0)
            
            # Xuất hiện logo FaMI ở cuối
            fami_logo = ImageMobject(os.path.join(os.path.dirname(__file__), "fami_logo_transparent.png")).scale_to_fit_height(3.0).move_to([0, 0, 0])
            self.sp(
                FadeOut(cta_row),
                FadeIn(fami_logo, scale=0.8),
                run_time=0.8
            )
            self.wait(max(0.1, tracker.duration - 3.4))

        self._lift()
        self.clear_content()
