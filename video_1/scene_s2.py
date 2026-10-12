"""
scene_s2.py – S2: Mô tả bài toán
Tuân thủ voiceover-first: Mỗi chunk voiceover = mỗi animation sequence.
"""

from manim import *
from config import (
    FONT, CONTENT_TOP, CONTENT_BOT,
    C_PRIMARY, C_WARNING, C_INCOME_H, C_PURPLE, C_SUCCESS, C_GRAY, C_WHITE, C_DANGER,
    SCRIPTS,
)
from helpers import skill_pop_in, sec_title, flow_block, load_icon
from config import audio_path


class SceneProblemMixin:
    def scene_problem(self):
        # Không dùng add_sound() vì đã dùng with self.voiceover() ở dưới
        
        # Chuẩn bị tiêu đề (không animate chưa)
        ttl = self.create_title("Mô tả bài toán")
        
        intro_text = "Quy trình thẩm định rút gọn của ngân hàng:"
        intro = Text(
            intro_text,
            font=FONT, font_size=17, color=C_GRAY, line_spacing=1.3,
        ).next_to(ttl, DOWN, buff=0.5)

        steps = [
            ("Khách hàng vay",    "Hồ sơ cần xét duyệt",      C_WARNING),
            ("Bước 1",            "Xác định mức thu nhập",     C_INCOME_H),
            ("Bước 2",            "Kiểm tra lịch sử tín dụng", C_PURPLE),
            ("Kết quả",           "Quyết định cho vay",         C_SUCCESS),
        ]
        step_grp = VGroup(*[flow_block(a, b, c) for a, b, c in steps])
        step_grp.arrange(DOWN, buff=0.28).next_to(intro, DOWN, buff=0.45)

        # Clamp to safe bottom - Tăng buffer để tránh subtitle
        if step_grp.get_bottom()[1] < CONTENT_BOT:
            step_grp.shift(UP * (CONTENT_BOT - step_grp.get_bottom()[1] + 0.8))

        # Mũi tên giữa các bước
        arrows = VGroup()
        for i in range(len(step_grp) - 1):
            a = Arrow(step_grp[i].get_bottom(), step_grp[i + 1].get_top(),
                      buff=0.06, stroke_width=2, color=C_GRAY,
                      max_tip_length_to_length_ratio=0.18)
            arrows.add(a)

        # ── CHUNK 0a: Yếu tố ban đầu ──────────────────────────────────────
        part0a_script = "Để xác định một hồ sơ có đủ điều kiện vay vốn hay không, "
        with self.voiceover(text=part0a_script) as tracker:
            self.update_subtitle(
                "Để xác định 1 hồ sơ có đủ điều kiện\nvay vốn hay không,",
                style="default"
            )
            self.sp(Write(ttl, run_time=min(1.0, tracker.duration * 0.4)))
            self.wait(min(1.5, tracker.duration * 0.5))

        # ── CHUNK 0b: Các yếu tố cụ thể (Hiển thị Icon) ───────────────────
        part0b_script = "cần có rất nhiều yếu tố như tuổi, thu nhập, điểm tín dụng, mục đích vay, vân vân. "
        with self.voiceover(text=part0b_script) as tracker:
            self.update_subtitle(
                "cần rất nhiều yếu tố: tuổi, thu nhập,\nđiểm tín dụng, mục đích vay,...",
                style="default"
            )
            
            def make_icon(sym, lbl):
                txt = Text(lbl, font=FONT, font_size=20, color=C_WHITE)
                return VGroup(sym, txt).arrange(DOWN, buff=0.2)

            # 1. Tuổi (Vector Person)
            h = Circle(radius=0.3, fill_color=C_WARNING, fill_opacity=1, stroke_width=0)
            b = Sector(radius=0.5, angle=PI, start_angle=0, fill_color=C_WARNING, fill_opacity=1, stroke_width=0)
            p_sym = VGroup(h, b).arrange(DOWN, buff=0.08)
            i_age = make_icon(p_sym, "Tuổi")

            # 2. Thu nhập (Vector Coin)
            c = Circle(radius=0.5, fill_color=C_INCOME_H, fill_opacity=1, stroke_width=0)
            d = Text("$", font=FONT, font_size=42, color="#0A0F1E", weight=BOLD).move_to(c.get_center())
            i_inc = make_icon(VGroup(c, d), "Thu nhập")

            # 3. Tín dụng (Vector Star)
            s_sym = Star(n=5, outer_radius=0.55, inner_radius=0.25, fill_color=C_SUCCESS, fill_opacity=1, stroke_width=0)
            i_cre = make_icon(s_sym, "Tín dụng")

            # 4. Mục đích (Vector Target)
            t1 = Circle(radius=0.5, fill_color=C_DANGER, fill_opacity=1, stroke_width=0)
            t2 = Circle(radius=0.35, fill_color=C_WHITE, fill_opacity=1, stroke_width=0)
            t3 = Circle(radius=0.2, fill_color=C_DANGER, fill_opacity=1, stroke_width=0)
            t_sym = VGroup(t1, t2, t3)
            i_pur = make_icon(t_sym, "Mục đích")
            
            icons_grp = VGroup(i_age, i_inc, i_cre, i_pur).arrange(RIGHT, buff=0.5)
            # Dịch lên cao một chút so với buff cũ
            icons_grp.next_to(ttl, DOWN, buff=0.8)
            
            # Tính toán nhịp pop-in tuần tự
            delay_per_icon = (tracker.duration * 0.8) / 4
            for icon in icons_grp:
                self.sp(skill_pop_in(icon, scale=0.5, run_time=min(0.4, delay_per_icon)))
                self.wait(max(0.1, delay_per_icon - 0.4))
                
        # Thu dọn mảng icon trước khi qua bước rút gọn
        self.sp(FadeOut(icons_grp, run_time=0.5))

        # ── CHUNK 1: Tiêu đề + Intro ──────────────────────────────────────────
        part1_script = "Nhưng để đơn giản, ta giả sử quy trình thẩm định rút gọn của ngân hàng gồm hai bước. "
        with self.voiceover(text=part1_script) as tracker:
            self.update_subtitle(
                "Nhưng để đơn giản, ta giả sử quy trình thẩm định rút gọn của ngân hàng\n "
                "còn 2 bước chính.",
                style="default"
            )
            self.sp(skill_pop_in(intro, run_time=min(1.0, tracker.duration * 0.35)))
        
        # ── CHUNK 2: Flow steps ────────────────────────────────────────────────
        part2_script = "Bước một: xác định mức thu nhập. Bước hai: kiểm tra lịch sử tín dụng."
        with self.voiceover(text=part2_script) as tracker:
            self.update_subtitle(
                "Bước 1: Xác định mức thu nhập.\nBước 2: Kiểm tra lịch sử tín dụng.",
                style="default"
            )
            # Animate từng bước với animation + arrow
            for i, s in enumerate(step_grp):
                anim_time = min(0.8, tracker.duration * 0.15)
                self.sp(skill_pop_in(s, shift=RIGHT * 0.3, run_time=anim_time))
                if i < len(arrows.submobjects):
                    self.sp(GrowArrow(arrows[i], run_time=0.3))
                self.wait(0.15)
        
        # ── CHUNK 3: Kết luận ──────────────────────────────────────────────────
        part3_script = "Sau đó ngân hàng mới quyết định có duyệt khoản vay hay không."
        with self.voiceover(text=part3_script) as tracker:
            self.update_subtitle(
                "Sau đó ngân hàng mới quyết định\ncó duyệt khoản vay hay không.",
                style="default"
            )
            self.wait(min(1.5, tracker.duration * 0.7))
        
        self._lift()
        self.clear_content()
