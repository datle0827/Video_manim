"""
scene_s8.py – S8: Câu hỏi gợi ý
Tuân thủ voiceover-first.
"""

from manim import *
from config import (
    FONT, CONTENT_TOP, CONTENT_BOT,
    C_WHITE, C_WARNING,
)
from helpers import skill_pop_in, load_icon
from config import audio_path


class SceneQuestionMixin:
    def scene_question(self):
        # Không dùng add_sound() vì đã dùng with self.voiceover() ở dưới
        
        q_top = Text("❓ Câu hỏi cho bạn",
                     font=FONT, font_size=23, color=C_WARNING, weight=BOLD)

        q_body = Text(
            "Nếu ngân hàng siết chặt tiêu chuẩn\n"
            "tín dụng và giảm xác suất duyệt vay\n"
            "từ  0.9  xuống  0.7,\n\n"
            "thì xác suất tổng thể được duyệt vay\n"
            "sẽ thay đổi như thế nào?",
            font=FONT, font_size=24, color=C_WHITE, line_spacing=1.4,
        )
        
        q_group = VGroup(q_top, q_body).arrange(DOWN, buff=0.42)
        
        actual_width = min(q_group.width + 0.8, 7.5)
        if q_group.width > actual_width - 0.6:
            q_group.scale_to_fit_width(actual_width - 0.6)
            
        q_bg = RoundedRectangle(corner_radius=0.3, width=actual_width, height=q_group.height + 0.8,
                                 fill_color="#0F172A", fill_opacity=1,
                                 stroke_color=C_WARNING, stroke_width=2.5)
                                 
        safe_mid = (CONTENT_TOP + CONTENT_BOT) / 2
        q_bg.move_to([0, safe_mid + 1.6, 0])
        q_group.move_to(q_bg.get_center())
        
        if q_bg.get_bottom()[1] < CONTENT_BOT:
            shift_dist = CONTENT_BOT - q_bg.get_bottom()[1] + 0.2
            q_bg.shift(UP * shift_dist)
            q_group.shift(UP * shift_dist)

        # ── CHUNK 1: Hiển thị câu hỏi ───────────────────────────────────────
        part1_script = ("Câu hỏi dành cho bạn: "
                       "Nếu ngân hàng siết chặt tiêu chuẩn tín dụng và giảm xác suất duyệt vay từ không phẩy chín "
                       "xuống không phẩy bảy, thì xác suất tổng thể được duyệt vay sẽ thay đổi như thế nào?")
        with self.voiceover(text=part1_script) as tracker:
            self.update_subtitle(
                "Nếu xác suất giảm từ 0.9\nxuống 0.7, tổng thể thay đổi?",
                style="default"
            )
            self.sp(skill_pop_in(q_bg, run_time=min(0.8, tracker.duration * 0.12)))
            self.sp(Write(q_top, run_time=min(1.0, tracker.duration * 0.18)))
            self.sp(Write(q_body, run_time=min(1.5, tracker.duration * 0.35)))
            self.wait(min(1.0, tracker.duration * 0.25))
        
        self._lift()
        
        # Fade out toàn bộ
        fade = Rectangle(width=config.frame_width, height=config.frame_height,
                         fill_color=BLACK, fill_opacity=0, stroke_width=0)
        self.add(fade)
        self.play(fade.animate.set_fill(BLACK, opacity=1), run_time=2.5)
        self.wait(0.5)
