"""
scene_s8.py – S8: Kết hợp IQR và Leverage
"""

from manim import *
from config import FONT, C_PRIMARY, C_SUCCESS, C_WARNING, C_GRAY, C_WHITE, C_DANGER, FAMI_SUB
from helpers import skill_pop_in

class SceneScene8Mixin: # Note: class name can be anything, but we will make sure we import it correctly in main
    pass

class SceneS8Mixin:
    def scene_s8(self):
        ttl = self.create_title("Phân loại Điểm Dữ liệu")

        # Modern Card-based table layout
        # Card backgrounds for cells (shifted up by 0.4 units)
        card_11_bg = RoundedRectangle(width=2.1, height=1.6, corner_radius=0.1, color="#475569", fill_color="#475569", fill_opacity=0.05, stroke_width=2).move_to([-0.7, 0.8, 0])
        card_12_bg = RoundedRectangle(width=2.1, height=1.6, corner_radius=0.1, color=C_SUCCESS, fill_color=C_SUCCESS, fill_opacity=0.05, stroke_width=2).move_to([1.6, 0.8, 0])
        card_21_bg = RoundedRectangle(width=2.1, height=1.6, corner_radius=0.1, color=C_WARNING, fill_color=C_WARNING, fill_opacity=0.05, stroke_width=2).move_to([-0.7, -1.0, 0])
        
        # Highlighted card for dangerous cell_22
        card_22_bg = RoundedRectangle(width=2.1, height=1.6, corner_radius=0.1, color=C_DANGER, fill_color=C_DANGER, fill_opacity=0.15, stroke_width=3).move_to([1.6, -1.0, 0])

        # Column Headers
        hdr_iqr_low_bg = RoundedRectangle(width=2.1, height=0.5, corner_radius=0.08, color="#334155", fill_color="#334155", fill_opacity=0.4, stroke_width=1).move_to([-0.7, 1.9, 0])
        lbl_iqr_low = Text("IQR Thấp", font=FONT, font_size=14, color=C_WHITE).move_to([-0.7, 1.9, 0])
        hdr_iqr_low = VGroup(hdr_iqr_low_bg, lbl_iqr_low)

        hdr_iqr_high_bg = RoundedRectangle(width=2.1, height=0.5, corner_radius=0.08, color=C_DANGER, fill_color=C_DANGER, fill_opacity=0.2, stroke_width=1).move_to([1.6, 1.9, 0])
        lbl_iqr_high = Text("IQR Cao", font=FONT, font_size=14, color=FAMI_SUB, weight=BOLD).move_to([1.6, 1.9, 0])
        hdr_iqr_high = VGroup(hdr_iqr_high_bg, lbl_iqr_high)

        # Row Headers (centered lines)
        lbl_lev_low_bg = RoundedRectangle(width=1.8, height=0.9, corner_radius=0.08, color="#334155", fill_color="#334155", fill_opacity=0.4, stroke_width=1).move_to([-2.8, 0.8, 0])
        lbl_lev_low_l1 = Text("Leverage Thấp", font=FONT, font_size=14, color=C_GRAY)
        # lbl_lev_low_l2 = Text("(Ít đòn bẩy)", font=FONT, font_size=9, color=C_GRAY)
        lbl_lev_low = VGroup(lbl_lev_low_l1).arrange(DOWN, buff=0.08).move_to([-2.8, 0.8, 0])
        hdr_lev_low = VGroup(lbl_lev_low_bg, lbl_lev_low)

        lbl_lev_high_bg = RoundedRectangle(width=1.8, height=0.9, corner_radius=0.08, color=C_DANGER, fill_color=C_DANGER, fill_opacity=0.2, stroke_width=1).move_to([-2.8, -1.0, 0])
        lbl_lev_high_l1 = Text("Leverage Cao", font=FONT, font_size=14, color=FAMI_SUB, weight=BOLD)
        # lbl_lev_high_l2 = Text("(Đòn bẩy lớn)", font=FONT, font_size=9, color=FAMI_SUB, weight=BOLD)
        lbl_lev_high = VGroup(lbl_lev_high_l1).arrange(DOWN, buff=0.08).move_to([-2.8, -1.0, 0])
        hdr_lev_high = VGroup(lbl_lev_high_bg, lbl_lev_high)

        # Grid cells content (centered lines)
        # Cell [Low Lev, Low IQR]
        cell_11 = VGroup(
            Text("Bình thường", font=FONT, font_size=14, color=C_WHITE, weight=BOLD),
            Text("Không bất thường,", font=FONT, font_size=10, color=C_GRAY),
            Text("không ảnh hưởng", font=FONT, font_size=10, color=C_GRAY)
        ).arrange(DOWN, buff=0.08).move_to([-0.7, 0.8, 0])

        # Cell [Low Lev, High IQR]
        cell_12 = VGroup(
            Text("Ít ảnh hưởng", font=FONT, font_size=14, color=C_SUCCESS, weight=BOLD),
            Text("Bất thường giá trị,", font=FONT, font_size=10, color=C_GRAY),
            Text("nhưng không lệch mô hình", font=FONT, font_size=10, color=C_GRAY)
        ).arrange(DOWN, buff=0.08).move_to([1.6, 0.8, 0])

        # Cell [High Lev, Low IQR]
        cell_21 = VGroup(
            Text("Nguy cơ ẩn", font=FONT, font_size=14, color=C_WARNING, weight=BOLD),
            Text("Bình thường,", font=FONT, font_size=10, color=C_GRAY),
            Text("nhưng nhạy cảm lớn", font=FONT, font_size=10, color=C_GRAY)
        ).arrange(DOWN, buff=0.08).move_to([-0.7, -1.0, 0])

        # Cell [High Lev, High IQR]
        cell_22 = VGroup(
            Text("NGUY HIỂM", font=FONT, font_size=14, color=C_DANGER, weight=BOLD),
            Text("Vừa bất thường,", font=FONT, font_size=10, color=C_WHITE),
            Text("vừa kéo lệch mô hình", font=FONT, font_size=10, color=C_WHITE)
        ).arrange(DOWN, buff=0.08).move_to([1.6, -1.0, 0])

        # --- ANIMATION FLOW ---

        part1_script = "Khi kết hợp cả hai phương pháp, chúng ta có thể phân loại các điểm dữ liệu theo mức độ nguy hiểm."
        with self.voiceover(text=part1_script) as tracker:
            self.update_subtitle("Khi kết hợp cả hai phương pháp, chúng ta", style="default")
            self.sp(Write(ttl, run_time=0.5))
            
            # Show grid headers and axes (no cell boxes yet)
            self.sp(
                FadeIn(hdr_iqr_low), FadeIn(hdr_iqr_high),
                FadeIn(hdr_lev_low), FadeIn(hdr_lev_high),
                run_time=0.8
            )
            self.update_subtitle("có thể phân loại điểm dữ liệu theo độ nguy hiểm.", style="default")
            self.wait(max(0.1, tracker.duration - 1.3))

        part2_1 = "Có những điểm bất thường nhưng ít ảnh hưởng."
        with self.voiceover(text=part2_1) as tracker:
            self.update_subtitle("Có những điểm bất thường nhưng ít ảnh hưởng.", style="default")
            # Pop normal cell
            self.sp(
                Create(card_11_bg),
                skill_pop_in(cell_11, sound=True),
                run_time=0.8
            )
            # Pop outlier low-impact cell and highlight green
            self.sp(
                Create(card_12_bg),
                skill_pop_in(cell_12, sound=True),
                run_time=0.8
            )
            self.sp(Flash(card_12_bg, color=C_SUCCESS), run_time=0.5)
            self.wait(max(0.1, tracker.duration - 2.1))

        part2_2 = "Có những điểm không quá bất thường nhưng lại có Leverage cao."
        with self.voiceover(text=part2_2) as tracker:
            self.update_subtitle("Có những điểm không quá bất thường\nnhưng lại có Leverage cao.", style="default")
            # Pop risk cell and highlight warning
            self.sp(
                Create(card_21_bg),
                skill_pop_in(cell_21, sound=True),
                run_time=0.8
            )
            self.sp(Flash(card_21_bg, color=C_WARNING), run_time=0.5)
            self.wait(max(0.1, tracker.duration - 1.3))

        part2_3 = "Và đáng chú ý nhất là những điểm vừa là Outlier theo khoảng tứ phân vị IQR, vừa có Leverage lớn."
        with self.voiceover(text=part2_3) as tracker:
            self.update_subtitle("Đáng chú ý nhất là các điểm vừa là Outlier\ntheo IQR, vừa có Leverage lớn.", style="default")
            # Pop dangerous cell, flash red, and wiggle
            self.sp(
                Create(card_22_bg),
                skill_pop_in(cell_22, sound=True),
                run_time=0.8
            )
            self.sp(Flash(card_22_bg, color=C_DANGER), run_time=0.6)
            self.sp(Wiggle(cell_22), run_time=0.8)
            self.wait(max(0.1, tracker.duration - 2.2))

        # Fade out all table elements gracefully
        all_grid_mobs = VGroup(
            card_11_bg, card_12_bg, card_21_bg, card_22_bg,
            hdr_iqr_low, hdr_iqr_high, hdr_lev_low, hdr_lev_high,
            cell_11, cell_12, cell_21, cell_22, ttl
        )
        self.sp(FadeOut(all_grid_mobs), run_time=0.8)
        self.clear_content()
