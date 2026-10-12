"""
scene_s6.py – S6: Tổng kết kiến thức
Tuân thủ voiceover-first: Chia thành 2 voiceover blocks.
"""

from manim import *
from config import (
    FONT, CONTENT_TOP, CONTENT_BOT,
    C_WHITE, C_GRAY, C_DARK_BG,
    C_PRIMARY, C_SUCCESS, C_DANGER, C_PURPLE,
)
from helpers import skill_pop_in, sec_title, rnode, load_icon
from config import audio_path


class SceneSummaryMixin:
    def scene_summary(self):
        # Không dùng add_sound() vì đã dùng with self.voiceover() ở dưới
        
        ttl = self.create_title("Tổng kết kiến thức")
        self.sp(Write(ttl, run_time=1.0))

        items = [
            ("Mô hình hóa quy trình", C_PRIMARY),
            ("Tính toán xác suất",    C_PURPLE),
            ("Hỗ trợ ra quyết định",  C_SUCCESS),
        ]
        cards = VGroup()
        for desc, col in items:
            txt = Text(desc, font=FONT, font_size=18, color=C_WHITE, weight=BOLD)
            
            actual_w = min(txt.width + 0.8, 7.5)
            if txt.width > actual_w - 0.4:
                txt.scale_to_fit_width(actual_w - 0.4)
                
            bg  = RoundedRectangle(corner_radius=0.2, width=actual_w, height=0.75,
                                    fill_color=C_DARK_BG, fill_opacity=1,
                                    stroke_color=col, stroke_width=2)
            txt.move_to(bg.get_center())
            cards.add(VGroup(bg, txt))

        cards.arrange(DOWN, buff=0.25).next_to(ttl, DOWN, buff=0.45)

        # Ứng dụng
        app_lbl = Text("Ứng dụng thực tế:", font=FONT, font_size=19,
                        color=C_GRAY, weight=BOLD)
        app_lbl.next_to(cards, DOWN, buff=0.42)

        # Tạo các icon ứng dụng thay vì rnode chữ nhật
        app_btns = VGroup()
        for idx, (t, col) in enumerate([("Tín dụng", C_PRIMARY), ("Đầu tư", C_SUCCESS), ("Rủi ro", C_DANGER)]):
            circle = Circle(radius=0.45, fill_color=col, fill_opacity=0.15, stroke_color=col, stroke_width=2)
            if idx == 0:
                sym = Text("$", font_size=32, color=col, weight=BOLD)
            elif idx == 1:
                # Mũi tên đi lên cho Đầu tư
                sym = Arrow(DOWN*0.15+LEFT*0.15, UP*0.2+RIGHT*0.2, stroke_width=4, color=col, buff=0, max_tip_length_to_length_ratio=0.3)
            else:
                sym = Text("!", font_size=32, color=col, weight=BOLD)
            
            sym.move_to(circle.get_center())
            icon_obj = VGroup(circle, sym)
            
            lbl = Text(t, font=FONT, font_size=16, color=C_WHITE)
            item = VGroup(icon_obj, lbl).arrange(DOWN, buff=0.15)
            app_btns.add(item)
            
        app_btns.arrange(RIGHT, buff=0.6).next_to(app_lbl, DOWN, buff=0.3)

        if app_btns.get_bottom()[1] < CONTENT_BOT:
            sh = CONTENT_BOT - app_btns.get_bottom()[1] + 0.5
            cards.shift(UP * sh); app_lbl.shift(UP * sh); app_btns.shift(UP * sh)

        # ── CHUNK 1: Tiêu đề + Cards ───────────────────────────────────────
        part1_script = ("Qua ví dụ này, ta đã thấy được cách cây quyết định được ứng dụng thế nào cho ngân hàng trong việc tự động ra quyết định một cách thông minh. "
                        "giúp kiểm soát rủi ro hiệu quả. "
                        "Chúng ta không chỉ mô hình hóa được luồng suy nghĩ của ngân hàng")
        with self.voiceover(text=part1_script) as tracker:
            self.update_subtitle(
                "Cây quyết định giúp mô hình hóa\nquy trình ra quyết định.",
                style="default"
            )
            self.sp(Write(ttl, run_time=min(1.0, tracker.duration * 0.15)))
            
            for c in cards:
                anim_time = min(0.8, tracker.duration * 0.18)
                self.sp(skill_pop_in(c, shift=RIGHT * 0.3, run_time=anim_time))
                self.wait(0.1)
        
        # ── CHUNK 2: Ứng dụng ──────────────────────────────────────────────
        part2_script = (" mà còn tính toán chính xác xác suất cho từng kịch bản. "
                        "Phương pháp này hiện đang là xương sống trong rất nhiều hệ thống phân tích tín dụng, thẩm định đầu tư và quản trị rủi ro doanh nghiệp.")
        with self.voiceover(text=part2_script) as tracker:
            self.update_subtitle(
                "Ứng dụng: Tín dụng, Đầu tư,\nQuản trị rủi ro.",
                style="default"
            )
            self.sp(skill_pop_in(app_lbl, run_time=min(0.8, tracker.duration * 0.15)))
            self.sp(*[skill_pop_in(a, scale=0.85) for a in app_btns], 
                    lag_ratio=0.2, run_time=min(0.8, tracker.duration * 0.35))

        self._lift()
        self.clear_content()
