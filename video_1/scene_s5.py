"""
scene_s5.py – S5: Tổng xác suất được duyệt vay
Tuân thủ voiceover-first: Chia thành 2 voiceover blocks.
"""

from manim import *
from config import (
    FONT, CONTENT_TOP, CONTENT_BOT,
    C_WHITE, C_GRAY, C_SUCCESS, C_DARK_BG,
    C_INCOME_H, C_INCOME_L,
    SCRIPTS,
)
from helpers import skill_pop_in, sec_title, load_icon
from config import audio_path


class SceneTotalProbMixin:
    def scene_total_prob(self):
        # Không dùng add_sound() vì đã dùng with self.voiceover() ở dưới
        
        ttl = self.create_title("P(Tự động duyệt vay) = ?")

        rule = Text('Cộng xác suất tất cả nhánh dẫn đến "Tự động duyệt vay"',
                     font=FONT, font_size=18, color=C_GRAY)
        rule.next_to(ttl, DOWN, buff=0.38)

        rows_data = [
            ("Thu nhập cao + Tín dụng tốt", "0.6 × 0.8", "0.480", C_INCOME_H),
            ("Thu nhập cao + Tín dụng TB",  "0.6 × 0.2", "0.120", C_INCOME_H),
            ("Thu nhập TB  + Tín dụng tốt", "0.4 × 0.5", "0.200", C_INCOME_L),
        ]

        row_mobs = VGroup()
        for desc, formula, result, col in rows_data:
            d = Text(desc,           font=FONT, font_size=16, color=C_WHITE)
            f = Text(formula,        font=FONT, font_size=16, color=col, weight=BOLD)
            r = Text("= " + result,  font=FONT, font_size=19, color=C_SUCCESS, weight=BOLD)
            fr = VGroup(f, r).arrange(RIGHT, buff=0.22)
            grp = VGroup(d, fr).arrange(DOWN, buff=0.12)
            
            actual_w = min(grp.width + 0.8, 7.5)
            if grp.width > actual_w - 0.4:
                grp.scale_to_fit_width(actual_w - 0.4)
                
            bg = RoundedRectangle(corner_radius=0.18, width=actual_w, height=1.15,
                                   fill_color=C_DARK_BG, fill_opacity=1,
                                   stroke_color=col, stroke_width=1.5)
            grp.move_to(bg.get_center())
            row_mobs.add(VGroup(bg, grp))

        row_mobs.arrange(DOWN, buff=0.25).next_to(rule, DOWN, buff=0.42)

        # Clamp - Tránh vướng phụ đề với buffer lớn
        if row_mobs.get_bottom()[1] < CONTENT_BOT + 1.8:
            row_mobs.shift(UP * (CONTENT_BOT + 1.8 - row_mobs.get_bottom()[1] + 0.8))

        # Đường phân cách + tổng
        div = Line(LEFT * 3.75, RIGHT * 3.75, color=C_GRAY, stroke_width=1.2)
        div.next_to(row_mobs, DOWN, buff=0.28)

        t1 = Text("0.480 + 0.120 + 0.200",
                  font=FONT, font_size=17, color=C_WHITE)
        t2 = Text("P(Tự động duyệt vay)  =  0.800  =  80%",
                  font=FONT, font_size=22, color=C_SUCCESS, weight=BOLD)
        grp_t = VGroup(t1, t2).arrange(DOWN, buff=0.12)
        
        tw = min(grp_t.width + 0.8, 7.5)
        if grp_t.width > tw - 0.4:
            grp_t.scale_to_fit_width(tw - 0.4)
            
        total_bg = RoundedRectangle(
            corner_radius=0.22, width=tw, height=1.35,
            fill_color="#052e16", fill_opacity=1,
            stroke_color=C_SUCCESS, stroke_width=2.5)
        total_bg.next_to(div, DOWN, buff=0.28)
        grp_t.move_to(total_bg.get_center())

        if total_bg.get_bottom()[1] < CONTENT_BOT:
            sh = CONTENT_BOT - total_bg.get_bottom()[1] + 0.8
            div.shift(UP * sh); total_bg.shift(UP * sh)
            grp_t.shift(UP * sh)

        # ── CHUNK 1: Tiêu đề + Rule ─────────────────────
        part1_script = ("Để tính xác suất tổng thể được tự động duyệt vay, "
                        "ta phải cộng xác suất của tất cả các nhánh dẫn đến kết quả được duyệt vay. "
                        "Đây chính là sự kết hợp của quy tắc cộng và nhân xác suất. ")
        with self.voiceover(text=part1_script) as tracker:
            self.update_subtitle(
                "Cộng xác suất tất cả nhánh\ndẫn đến 'Tự động duyệt vay'.",
                style="default"
            )
            self.sp(Write(ttl, run_time=min(1.0, tracker.duration * 0.15)))
            self.sp(skill_pop_in(rule, run_time=min(1.0, tracker.duration * 0.15)))
            
            # Ô xuất hiện sớm ở ngay chunk tổng quan
            for rw in row_mobs:
                anim_time = min(0.6, tracker.duration * 0.15)
                self.sp(skill_pop_in(rw, shift=RIGHT * 0.25, run_time=anim_time))
        
        # ── CHUNK 2: Rows + Total ──────────────────────────
        part2_script = ("Như vậy, khoảng tám mươi phần trăm các hồ sơ đã được tự động duyệt một cách thông minh. "
                        "Nhờ cây quyết định, chúng ta có thể nhìn rõ toàn bộ quy trình ra quyết định của ngân hàng.")
        with self.voiceover(text=part2_script) as tracker:
            self.update_subtitle(
                "Quy tắc cộng + nhân xác suất:\nP(Tự động duyệt vay) = 0.800 = 80%",
                style="default"
            )
            
            self.sp(Create(div, run_time=min(0.6, tracker.duration * 0.15)))
            self.sp(skill_pop_in(total_bg, run_time=min(0.6, tracker.duration * 0.15)))
            self.sp(Write(t1, run_time=min(1.0, tracker.duration * 0.25)))
            self.sp(Write(t2, run_time=min(1.0, tracker.duration * 0.25)))
            
            self.wait(min(1.0, tracker.duration * 0.2))
        
        self._lift()
        self.clear_content()
