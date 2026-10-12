"""
scene_s3.py – S3: Cây quyết định
Lưu state (_N, _E, _PL) cho scene_s4 dùng.
Tuân thủ voiceover-first: Chia thành multiple voiceover blocks.
"""

import numpy as np
from manim import *
from config import (
    FONT, CONTENT_TOP,
    C_PRIMARY, C_WARNING, C_GRAY, C_WHITE,
    C_INCOME_H, C_INCOME_L,
    C_CREDIT_G, C_CREDIT_A,
    C_APPROVE, C_REJECT,
    SCRIPTS,
)
from helpers import skill_pop_in, rnode, sec_title, load_icon
from config import audio_path


class SceneTreeMixin:
    def scene_tree(self):
        # Không dùng add_sound() vì đã dùng with self.voiceover() ở dưới
        
        def text_node(text_content, percentage, bg_color):
            """Node level 1-2: text + percentage."""
            txt = rnode(text_content, bg_color, w=1.95, h=0.72, fs=13)
            pct = Text(percentage, font=FONT, font_size=11, color=C_WHITE, weight=BOLD)
            pct.next_to(txt, DOWN, buff=0.06)
            return VGroup(txt, pct)
        
        def icon_node(icon_name, percentage, bg_color, width=1.0):
            """Node level 3: icon + percentage text."""
            icon = load_icon(icon_name, width=width, bg_color=bg_color)
            pct = Text(percentage, font=FONT, font_size=12, color=C_WHITE, weight=BOLD)
            pct.next_to(icon, DOWN, buff=0.08)
            return VGroup(icon, pct)
        
        ttl = self.create_title("Cây Quyết Định")
        
        intro = Text(
            "Mô hình hóa quá trình:",
            font=FONT, font_size=15, color=C_GRAY,
        ).next_to(ttl, DOWN, buff=0.35)

        # ── Vị trí các nút ────────────────────────────────────────────────
        TREE_TOP = 4.8  # Giữ cây sát phần trên hơn để chừa chỗ phía dưới
        y0 = TREE_TOP - 0.6
        y1 = y0 - 1.8  # Thu gọn khoảng cách dọc từ 2.2 xuống 1.8
        y2 = y1 - 1.8
        y3 = y2 - 1.8

        P = {
            "root":   np.array([ 0.00, y0, 0]),
            "cao":    np.array([-2.30, y1, 0]),
            "tb":     np.array([ 2.30, y1, 0]),
            "cc_tot": np.array([-3.20, y2, 0]),
            "cc_avg": np.array([-1.20, y2, 0]),
            "tb_tot": np.array([ 1.20, y2, 0]),
            "tb_avg": np.array([ 3.20, y2, 0]),
            "d1":     np.array([-3.60, y3, 0]),
            "r1":     np.array([-2.10, y3, 0]),
            "d2":     np.array([-1.60, y3, 0]),
            "r2":     np.array([-0.10, y3, 0]),
            "d3":     np.array([ 0.65, y3, 0]),
            "r3":     np.array([ 1.80, y3, 0]),
            "d4":     np.array([ 2.75, y3, 0]),
            "r4":     np.array([ 3.90, y3, 0]),
        }

        N = {
            "root":   rnode("Khách hàng",           C_WARNING,  w=2.5,  h=0.80, fs=18, bold=True),
            "cao":    text_node("Thu nhập cao", "60%",      C_INCOME_H),
            "tb":     text_node("Thu nhập TB",  "40%",      C_INCOME_L),
            "cc_tot": text_node("Tín dụng tốt", "80%",      C_CREDIT_G),
            "cc_avg": text_node("Tín dụng TB",  "20%",      C_CREDIT_A),
            "tb_tot": text_node("Tín dụng tốt", "50%",      C_CREDIT_G),
            "tb_avg": text_node("Tín dụng TB",  "50%",      C_CREDIT_A),
            "d1":  icon_node("icon_approve",  "90%",   C_APPROVE, width=0.75),
            "r1":  icon_node("icon_reject",   "10%",   C_REJECT,  width=0.75),
            "d2":  icon_node("icon_approve",  "70%",   C_APPROVE, width=0.75),
            "r2":  icon_node("icon_reject",   "30%",   C_REJECT,  width=0.75),
            "d3":  icon_node("icon_approve",  "90%",   C_APPROVE, width=0.75),
            "r3":  icon_node("icon_reject",   "10%",   C_REJECT,  width=0.75),
            "d4":  icon_node("icon_approve",  "50%",   C_APPROVE, width=0.75),
            "r4":  icon_node("icon_reject",   "50%",   C_REJECT,  width=0.75),
        }
        for k, n in N.items():
            n.move_to(P[k])

        def mk_edge(a, b, col, sw=1.8):
            return Line(N[a].get_bottom(), N[b].get_top(), color=col, stroke_width=sw)

        E = {
            "r_c":   mk_edge("root", "cao",    C_INCOME_H, 2.4),
            "r_t":   mk_edge("root", "tb",     C_INCOME_L, 2.4),
            "c_cg":  mk_edge("cao",  "cc_tot", C_CREDIT_G, 1.8),
            "c_ca":  mk_edge("cao",  "cc_avg", C_CREDIT_A, 1.8),
            "t_tg":  mk_edge("tb",   "tb_tot", C_CREDIT_G, 1.8),
            "t_ta":  mk_edge("tb",   "tb_avg", C_CREDIT_A, 1.8),
            "cg_d1": mk_edge("cc_tot", "d1",   C_APPROVE,  1.4),
            "cg_r1": mk_edge("cc_tot", "r1",   C_REJECT,   1.4),
            "ca_d2": mk_edge("cc_avg", "d2",   C_APPROVE,  1.4),
            "ca_r2": mk_edge("cc_avg", "r2",   C_REJECT,   1.4),
            "tg_d3": mk_edge("tb_tot", "d3",   C_APPROVE,  1.4),
            "tg_r3": mk_edge("tb_tot", "r3",   C_REJECT,   1.4),
            "ta_d4": mk_edge("tb_avg", "d4",   C_APPROVE,  1.4),
            "ta_r4": mk_edge("tb_avg", "r4",   C_REJECT,   1.4),
        }

        def plbl(edge_obj, txt, col, offset=ORIGIN):
            t = Text(txt, font=FONT, font_size=11, color=col)  # Giảm từ 12 → 11
            t.move_to(edge_obj.get_center() + offset)
            return t

        PL = [
            plbl(E["r_c"],   "0.6", C_INCOME_H, LEFT * 0.28),
            plbl(E["r_t"],   "0.4", C_INCOME_L, RIGHT * 0.28),
            plbl(E["c_cg"],  "0.8", C_CREDIT_G, LEFT * 0.25),
            plbl(E["c_ca"],  "0.2", C_CREDIT_A, RIGHT * 0.22),
            plbl(E["t_tg"],  "0.5", C_CREDIT_G, LEFT * 0.25),
            plbl(E["t_ta"],  "0.5", C_CREDIT_A, RIGHT * 0.22),
            plbl(E["cg_d1"], "0.9", C_APPROVE,  LEFT * 0.18),
            plbl(E["cg_r1"], "0.1", C_REJECT,   RIGHT * 0.18),
            plbl(E["ca_d2"], "0.7", C_APPROVE,  LEFT * 0.18),
            plbl(E["ca_r2"], "0.3", C_REJECT,   RIGHT * 0.18),
            plbl(E["tg_d3"], "0.9", C_APPROVE,  LEFT * 0.18),
            plbl(E["tg_r3"], "0.1", C_REJECT,   RIGHT * 0.18),
            plbl(E["ta_d4"], "0.5", C_APPROVE,  LEFT * 0.18),
            plbl(E["ta_r4"], "0.5", C_REJECT,   RIGHT * 0.18),
        ]
        
        # Lưu để scene_s4 dùng
        self._N = N
        self._E = E
        self._PL = PL

        # ── CHUNK 1: Tiêu đề + Intro ──────────────────────────────────────────
        part1_script = "Ta mô hình hóa quá trình này bằng một cây quyết định."
        with self.voiceover(text=part1_script) as tracker:
            self.update_subtitle(
                "Ta mô hình hóa quá trình\nbằng một cây quyết định.",
                style="default"
            )
            self.sp(Write(ttl, run_time=min(1.0, tracker.duration * 0.4)))
            self.sp(skill_pop_in(intro, run_time=min(1.0, tracker.duration * 0.35)))
        
        # ── CHUNK 2: Tầng gốc + Tầng 1 ────────────────────────────────────────
        part2_script = ("60% khách hàng có thu nhập cao. "
                       "40% có thu nhập trung bình. "
                       "Nếu thu nhập cao: 80% có tín dụng tốt. "
                       "Nếu thu nhập TB: 50% có tín dụng tốt.")
        with self.voiceover(text=part2_script) as tracker:
            self.update_subtitle(
                "Phân nhánh theo thu nhập\n"
                "và tín dụng khách hàng.",
                style="default"
            )
            # Tầng 0 – root
            self.sp(skill_pop_in(N["root"], scale=0.8, run_time=min(1.0, tracker.duration * 0.15)))
            
            # Tầng 1 – income
            self.sp(Create(E["r_c"]), Create(E["r_t"]), 
                    run_time=min(0.8, tracker.duration * 0.15))
            self.sp(skill_pop_in(N["cao"]), skill_pop_in(N["tb"]),
                    skill_pop_in(PL[0]), skill_pop_in(PL[1]), 
                    run_time=min(0.8, tracker.duration * 0.15))
        
        # ── CHUNK 3: Tầng 2 ─────────────────────────────────────────────────────
        part3_script = ("Nếu tín dụng tốt, khoản vay sẽ được hoàn trả với tỷ lệ là chín mươi phần trăm. "
                       "Nếu có tín dụng trung bình nhưng thu nhập cao, khả năng này là bảy mươi phần trăm, "
                       "còn thu nhập trung bình sẽ là năm mươi phần trăm.")
        with self.voiceover(text=part3_script) as tracker:
            self.update_subtitle(
                "Rẽ nhánh tín dụng:\nTỷ lệ hoàn trả mỗi kịch bản.",
                style="default"
            )
            # Tầng 2 – credit
            self.sp(*[Create(E[k]) for k in ["c_cg", "c_ca", "t_tg", "t_ta"]], 
                    run_time=min(0.8, tracker.duration * 0.15))
            self.sp(skill_pop_in(N["cc_tot"]), skill_pop_in(N["cc_avg"]),
                    skill_pop_in(N["tb_tot"]), skill_pop_in(N["tb_avg"]),
                    skill_pop_in(PL[2]), skill_pop_in(PL[3]),
                    skill_pop_in(PL[4]), skill_pop_in(PL[5]), 
                    run_time=min(0.8, tracker.duration * 0.2))
        
        # ── CHUNK 4: Tầng 3 (Leaves) ───────────────────────────────────────────
        part4_script = "Mỗi nhánh sẽ dẫn đến tỷ lệ hoàn trả hoặc rủi ro vỡ nợ khác nhau."
        with self.voiceover(text=part4_script) as tracker:
            self.update_subtitle(
                "Kết quả: Hoàn trả hay Vỡ nợ\ntrên từng nhánh cây.",
                style="default"
            )
            # Tầng 3 – leaves
            self.sp(*[Create(E[k]) for k in
                      ["cg_d1", "cg_r1", "ca_d2", "ca_r2", "tg_d3", "tg_r3", "ta_d4", "ta_r4"]],
                    run_time=min(0.8, tracker.duration * 0.25))
            self.sp(*[skill_pop_in(N[k]) for k in ["d1", "r1", "d2", "r2", "d3", "r3", "d4", "r4"]],
                    *[skill_pop_in(pl) for pl in PL[6:]], 
                    run_time=min(0.8, tracker.duration * 0.25))
        
        self._lift()

        # Lưu lại để dùng ở scene sau (scene_s4)
        self._N  = N
        self._E  = E
        self._PL = PL
