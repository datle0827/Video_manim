"""
scene_s7.py – S7: Từ khóa quan trọng
Tuân thủ voiceover-first.
"""

from manim import *
from config import (
    FONT, CONTENT_TOP, CONTENT_BOT,
    C_GRAY, C_DARK_BG, C_WARNING,
    C_PRIMARY, C_PURPLE,
)
from helpers import skill_pop_in, sec_title, load_icon
from config import audio_path


class SceneKeywordsMixin:
    def scene_keywords(self):
        # Không dùng add_sound() vì đã dùng with self.voiceover() ở dưới
        
        ttl = self.create_title("Từ khóa quan trọng", apply_gradient=False)
        ttl.set_color(C_WARNING)
        self.sp(Write(ttl, run_time=0.9))

        kws = [
            ("Cây quyết định",        "Decision Tree",               C_PRIMARY),
            ("Xác suất có điều kiện", "Conditional Probability",     C_PURPLE),
            ("Quy tắc nhân & cộng",   "Multiplication & Addition Rule", C_WARNING),
        ]
        kw_cards = VGroup()
        for vi, en, col in kws:
            vi_t = Text(vi, font=FONT, font_size=19, color=col, weight=BOLD)
            en_t = Text(en, font=FONT, font_size=15, color=C_GRAY)
            txt_g = VGroup(vi_t, en_t).arrange(DOWN, buff=0.1)
            
            actual_w = min(txt_g.width + 1.2, 7.5)
            if txt_g.width > actual_w - 0.4:
                txt_g.scale_to_fit_width(actual_w - 0.4)
                
            bg   = RoundedRectangle(corner_radius=0.22, width=actual_w, height=1.65,
                                     fill_color=C_DARK_BG, fill_opacity=1,
                                     stroke_color=col, stroke_width=2)
            txt_g.move_to(bg.get_center())
            kw_cards.add(VGroup(bg, txt_g))

        kw_cards.arrange(DOWN, buff=0.35).next_to(ttl, DOWN, buff=0.52)

        if kw_cards.get_bottom()[1] < CONTENT_BOT:
            kw_cards.shift(UP * (CONTENT_BOT - kw_cards.get_bottom()[1] + 0.1))

        # ── CHUNK 1: Tiêu đề + Keywords ────────────────────────────────────
        part1_script = ("Trong video này mình đề cập tới ba khái niệm quan trọng: "
                       "Cây quyết định, xác suất có điều kiện, và quy tắc nhân cộng xác suất.")
        with self.voiceover(text=part1_script) as tracker:
            self.update_subtitle(
                "3 khái niệm: Cây quyết định,\nXác suất, Quy tắc nhân-cộng.",
                style="default"
            )
            self.sp(Write(ttl, run_time=min(0.9, tracker.duration * 0.15)))
            
            for c in kw_cards:
                anim_time = min(0.8, tracker.duration * 0.2)
                self.sp(skill_pop_in(c, shift=UP * 0.2, run_time=anim_time))
                self.wait(0.15)

        self._lift()
        self.clear_content()
