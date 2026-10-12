"""
scene_s4.py – S4: Highlight một kịch bản + công thức nhân xác suất
Lưu ý: cần chạy sau scene_s3 vì dùng self._N, self._E, self._PL.
Tuân thủ voiceover-first: Chia thành 2 voiceover blocks.
"""

from manim import *
from config import FONT, CONTENT_BOT, C_WARNING, C_SUCCESS, C_DANGER, C_WHITE, SCRIPTS
from helpers import skill_pop_in, load_icon
from config import audio_path


class SceneSinglePathMixin:
    def scene_single_path(self):
        # Không dùng add_sound() vì đã dùng with self.voiceover() ở dưới
        
        N, E, PL = self._N, self._E, self._PL
        all_m = list(N.values()) + list(E.values()) + PL
        
        # Từng nhánh cuối (định nghĩa sớm để dùng ở cleanup)
        leaves = [N["d1"], N["r1"], N["d2"], N["r2"], N["d3"], N["r3"], N["d4"], N["r4"]]
        leaf_edges = [E["cg_d1"], E["cg_r1"], E["ca_d2"], E["ca_r2"], 
                     E["tg_d3"], E["tg_r3"], E["ta_d4"], E["ta_r4"]]
        leaf_labels = PL[6:]  # Labels cho leaves

        # Chuẩn bị các object để highlight
        hl_n = [N["root"], N["cao"], N["cc_tot"], N["d1"]]
        hl_e = [E["r_c"], E["c_cg"], E["cg_d1"]]
        hl_p = [PL[0], PL[2], PL[6]]
        
        glows = VGroup(*[
            SurroundingRectangle(n, color=C_WARNING, stroke_width=3,
                                 corner_radius=0.18, buff=0.06)
            for n in hl_n
        ])

        # Chuẩn bị công thức (rút ngắn lại để không chạm Y=-4.5)
        calc_y = -2.8
        calc_txt = Text("P = 0.6 × 0.8 × 0.9 = 0.432",
                         font=FONT, font_size=22, color=C_WARNING, weight=BOLD)
        
        calc_w = min(calc_txt.width + 0.8, 7.5)
        if calc_txt.width > calc_w - 0.4:
            calc_txt.scale_to_fit_width(calc_w - 0.4)
            
        calc_bg = RoundedRectangle(
            corner_radius=0.22, width=calc_w, height=0.98,
            fill_color="#1F2937", fill_opacity=1,
            stroke_color=C_WARNING, stroke_width=2.2)
        calc_bg.move_to([0, calc_y, 0])
        calc_txt.move_to(calc_bg.get_center())

        # ── CHUNK 1: Fade out + highlight path + công thức ──────────────────
        part1_script = ("Đây là chuỗi xác suất có điều kiện. "
                       "Để biết xác suất xảy ra của một kịch bản cụ thể, "
                       "ta nhân các xác suất trên cùng một nhánh. "
                       "Ví dụ: khách có thu nhập cao, tín dụng tốt, hoàn trả khoản vay. "
                       "P bằng 0.6 nhân 0.8 nhân 0.9 bằng 0.432.")
        with self.voiceover(text=part1_script) as tracker:
            self.update_subtitle(
                "Đây là chuỗi xác suất có điều kiện.\n"
                "Nhân xác suất trên cùng nhánh.",
                style="default"
            )
            
            # Fade out non-highlight
            self.sp(*[m.animate.set_opacity(0.12) for m in all_m], 
                    run_time=min(0.8, tracker.duration * 0.15))
            
            # Highlight path
            self.sp(*[m.animate.set_opacity(1) for m in hl_n + hl_e + hl_p], 
                    run_time=min(0.8, tracker.duration * 0.15))
            
            # Glow
            self.sp(Create(glows, run_time=min(0.8, tracker.duration * 0.15)))
            
            # Công thức
            self.sp(skill_pop_in(calc_bg, run_time=min(0.6, tracker.duration * 0.15)))
            self.sp(Write(calc_txt, run_time=min(1.2, tracker.duration * 0.35)))
        
        # ── CHUNK 2: Ngưỡng duyệt - chỉ giữ nhánh cuối + mô tả dưới ──────────
        part2_script = ("Giả sử ngân hàng đặt ra một ngưỡng duyệt tại nhánh cuối là bảy mươi phần trăm. "
                       "Các hồ sơ nếu có xác suất duyệt tại nhánh này lớn hơn bảy mươi phần trăm "
                       "sẽ được tự động duyệt, còn không sẽ được thẩm định thêm.")
        with self.voiceover(text=part2_script) as tracker:
            self.update_subtitle(
                "Ngưỡng ≥ 70%: Tự động duyệt.\n"
                "< 70%: Thẩm định thêm.",
                style="default"
            )
            
            # Dọn sạch cây cũ và các hiệu ứng chunk 1
            self.sp(*[m.animate.set_opacity(0.0) for m in all_m] +
                    [FadeOut(calc_bg), FadeOut(calc_txt), FadeOut(glows)],
                    run_time=min(0.8, tracker.duration * 0.15))
            
            # Khởi tạo 4 kịch bản xếp dọc
            data = [
                ("Thu nhập cao + Tín dụng tốt", "90%", True),
                ("Thu nhập cao + Tín dụng TB", "70%", True),
                ("Thu nhập TB + Tín dụng tốt", "90%", True),
                ("Thu nhập TB + Tín dụng TB", "50%", False),
            ]
            cases = VGroup()
            for text, rate, is_pass in data:
                c_col = C_SUCCESS if is_pass else C_DANGER
                
                t_desc = Text(text, font=FONT, font_size=18, color=C_WHITE)
                t_rate = Text(rate, font=FONT, font_size=18, color=C_WHITE, weight=BOLD)
                t_rate_bg = RoundedRectangle(corner_radius=0.1, width=0.8, height=0.4, 
                                             fill_color=c_col, fill_opacity=0.3, stroke_width=0)
                t_rate.move_to(t_rate_bg.get_center())
                g_rate = VGroup(t_rate_bg, t_rate)

                t_status = Text("Tự động duyệt" if is_pass else "Thẩm định thêm", 
                                font=FONT, font_size=17, color=c_col, weight=BOLD)
                
                # Vẽ icon thủ công không dùng text hay latex
                if is_pass:
                    icon_t = VGroup(
                        Line(LEFT*0.1, DOWN*0.1, stroke_width=3, color=c_col),
                        Line(DOWN*0.1, RIGHT*0.15 + UP*0.15, stroke_width=3, color=c_col)
                    ).shift(UP*0.05)
                else:
                    icon_t = VGroup(
                        Line(LEFT*0.12+UP*0.12, RIGHT*0.12+DOWN*0.12, stroke_width=3, color=c_col),
                        Line(RIGHT*0.12+UP*0.12, LEFT*0.12+DOWN*0.12, stroke_width=3, color=c_col)
                    )
                
                row_items = VGroup(t_desc, g_rate, icon_t, t_status)
                row_items.arrange(RIGHT, buff=0.25)
                
                actual_w = min(row_items.width + 0.6, 7.5)
                if row_items.width > actual_w - 0.4:
                    row_items.scale_to_fit_width(actual_w - 0.4)
                    
                bg = RoundedRectangle(corner_radius=0.18, width=actual_w, height=0.85,
                                      fill_color="#1F2937", fill_opacity=1, 
                                      stroke_color=c_col, stroke_width=1.5)
                row_items.move_to(bg.get_center())
                cases.add(VGroup(bg, row_items))
            
            cases.arrange(DOWN, buff=0.25)
            
            # Ngưỡng quyết định
            thresh_txt = Text("Ngưỡng quy định: 70%", font=FONT, font_size=20, color=C_WARNING, weight=BOLD)
            tw = min(thresh_txt.width + 1.2, 7.5)
            thresh_bg = RoundedRectangle(corner_radius=0.2, width=tw, height=0.75,
                                         fill_color="#1C1917", fill_opacity=1,
                                         stroke_color=C_WARNING, stroke_width=2.0)
            thresh_txt.move_to(thresh_bg.get_center())
            thresh_grp = VGroup(thresh_bg, thresh_txt)
            
            thresh_grp.next_to(cases, DOWN, buff=0.5)
            
            board = VGroup(cases, thresh_grp)
            board.move_to([0, 0.5, 0])
            
            # Kiểm tra vướng phụ đề
            if board.get_bottom()[1] < CONTENT_BOT:
                shift_up = CONTENT_BOT - board.get_bottom()[1] + 0.5
                board.shift(UP * shift_up)
            
            self.sp(skill_pop_in(cases, run_time=min(0.8, tracker.duration * 0.2)))
            self.wait(min(0.5, tracker.duration * 0.1))
            self.sp(skill_pop_in(thresh_grp, run_time=min(0.6, tracker.duration * 0.15)))

        # Khôi phục cây
        self.sp(FadeOut(board),
                *[m.animate.set_opacity(1) for m in all_m], 
                run_time=0.7)
        
        self._lift()
        self.clear_content()
