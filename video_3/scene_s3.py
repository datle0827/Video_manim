"""
scene_s3.py – S3: Dữ liệu lịch sử
"""

from manim import *
from config import FONT, C_PRIMARY, C_PURPLE, C_WARNING, C_GRAY, C_WHITE, C_SUCCESS, C_DANGER, SCRIPTS, SUBS
from helpers import skill_pop_in, rnode, load_icon, make_centered_markup

def make_bold_text(text):
    return Text(text, font=FONT, font_size=20, weight=BOLD)

def make_fraction(num_str, denom_str, color=C_WHITE, font_size=16):
    num_txt = MarkupText(num_str, font=FONT, font_size=font_size, color=color, weight=BOLD)
    denom_txt = MarkupText(denom_str, font=FONT, font_size=font_size, color=color, weight=BOLD)
    line = Line(start=LEFT*0.5, end=RIGHT*0.5, color=color, stroke_width=2)
    w = max(num_txt.width, denom_txt.width) + 0.2
    line.stretch_to_fit_width(w)
    return VGroup(num_txt, line, denom_txt).arrange(DOWN, buff=0.08)

class SceneTreeMixin: 
    def scene_tree(self): 
        # Standard title at the top
        ttl = self.create_title("Dữ liệu lịch sử")
        
        center_db_icon = load_icon("icon_database", width=1.8, bg_color=C_WARNING).move_to([0, 0, 0])
        
        data = [
            ["6", "28.74", "9.40%", "100.34", "2.33%"],
            ["7", "31.48", "9.53%", "101.53", "1.19%"],
            ["8", "35.19", "11.79%", "99.19", "-2.30%"],
            ["9", "34.84", "-0.99%", "90.79", "-8.47%"],
            ["10", "33.88", "-2.76%", "101.43", "11.72%"]
        ]
        
        history_table = Table(
            data,
            col_labels=[
                make_centered_markup("Tháng", font=FONT, font_size=20, color=C_WHITE, weight=BOLD),
                make_centered_markup("Giá cuối \ntháng CTG", font=FONT, font_size=20, color=C_PRIMARY, weight=BOLD),
                make_centered_markup("Tỷ suất \nsinh lợi", font=FONT, font_size=20, color=C_PRIMARY, weight=BOLD),
                make_centered_markup("Giá cuối \ntháng FPT", font=FONT, font_size=20, color=C_SUCCESS, weight=BOLD),
                make_centered_markup("Tỷ suất \nsinh lợi", font=FONT, font_size=20, color=C_SUCCESS, weight=BOLD)
            ],
            h_buff=0.7,
            v_buff=0.5,
            element_to_mobject=make_bold_text,
            include_outer_lines=True,
            line_config={"color": C_GRAY}
        ).scale(0.7).move_to([0, 1.2, 0])

        # Color the cells: positive is Green (C_SUCCESS), negative is Red (C_DANGER)
        for idx in range(1, 6):
            val_a = data[idx-1][2]
            color_a = C_DANGER if "-" in val_a else C_SUCCESS
            history_table.get_entries((idx+1, 3)).set_color(color_a)
            
            val_b = data[idx-1][4]
            color_b = C_DANGER if "-" in val_b else C_SUCCESS
            history_table.get_entries((idx+1, 5)).set_color(color_b)
            
        table_subtitle = Text("Thời gian: 6/2025 - 10/2025", font=FONT, font_size=26, color=C_WHITE).next_to(history_table, DOWN, buff=0.25)
            
        # Fractions and stock icons for average returns calculation
        icon_a = ImageMobject(os.path.join(os.path.dirname(__file__), "ctg.png")).scale_to_fit_width(0.6)
        lbl_a = MarkupText("CTG:", font=FONT, font_size=20, color=C_PRIMARY, weight=BOLD)
        fraction_a = make_fraction("9.40% + 9.53% + 11.79% - 0.99% - 2.76%", "5", color=C_WHITE, font_size=18)
        equals_a = MarkupText("= 5.39%", font=FONT, font_size=20, color=C_PRIMARY, weight=BOLD)
        formula_a = Group(icon_a, lbl_a, fraction_a, equals_a).arrange(RIGHT, buff=0.2).move_to([0, 0.8, 0]).scale(1.15)
        
        icon_b = ImageMobject(os.path.join(os.path.dirname(__file__), "fpt.png")).scale_to_fit_width(0.6)
        lbl_b = MarkupText("FPT:", font=FONT, font_size=20, color=C_SUCCESS, weight=BOLD)
        fraction_b = make_fraction("2.33% + 1.19% - 2.30% - 8.47% + 11.72%", "5", color=C_WHITE, font_size=18)
        equals_b = MarkupText("= 0.89%", font=FONT, font_size=20, color=C_SUCCESS, weight=BOLD)
        formula_b = Group(icon_b, lbl_b, fraction_b, equals_b).arrange(RIGHT, buff=0.2).move_to([0, -0.8, 0]).scale(1.15)

        part1_script_1 = "Dựa trên dữ liệu lịch sử về tỷ suất sinh lợi của hai cổ phiếu"
        with self.voiceover(text=part1_script_1) as tracker:
            self.update_subtitle("Dựa trên tỷ suất sinh lợi lịch sử\ncủa hai cổ phiếu CTG và FPT", style="default")
            
            # Show standard title and center database icon
            self.sp(Write(ttl, run_time=min(0.5, tracker.duration * 0.3)))
            self.sp(skill_pop_in(center_db_icon, sound=True, run_time=0.6))
            
            # Transform database icon into table grid and headers
            grid = VGroup(history_table.get_horizontal_lines(), history_table.get_vertical_lines())
            headers = history_table.get_rows()[0]
            self.sp(
                ReplacementTransform(center_db_icon, grid),
                Write(headers),
                run_time=0.8
            )
            self.wait(max(0.1, tracker.duration - 1.9))
            
        part1_script_2 = "trong khoảng thời gian từ tháng sáu đến tháng mười năm 2025 như sau,"
        with self.voiceover(text=part1_script_2) as tracker:
            self.update_subtitle("trong khoảng thời gian 6/2025 - 10/2025", style="default")
            rows = history_table.get_rows()
            # Draw rows one by one (no rotation) and write subtitle
            self.sp(
                LaggedStart(
                    *[Write(rows[i]) for i in range(1, 6)],
                    lag_ratio=0.2
                ),
                Write(table_subtitle),
                run_time=max(1.0, tracker.duration - 0.2)
            )
            
        part2_script_1 = "ta tính tỷ suất sinh lợi trung bình của từng cổ phiếu"
        with self.voiceover(text=part2_script_1) as tracker:
            self.update_subtitle("Ta tính tỷ suất sinh lợi trung bình\ncủa từng cổ phiếu", style="default")
            
            # Fade out table skeleton and subtitle
            self.sp(FadeOut(grid), FadeOut(headers), FadeOut(table_subtitle), run_time=0.4)
            
            # Extract number columns and morph them into formulas
            cells_a = VGroup(*[history_table.get_entries((i+1, 3)) for i in range(1, 6)])
            cells_b = VGroup(*[history_table.get_entries((i+1, 5)) for i in range(1, 6)])
            cells_other = VGroup(*[
                history_table.get_entries((i+1, col)) 
                for i in range(1, 6) 
                for col in (1, 2, 4)
            ])
            
            self.sp(
                FadeIn(icon_a), FadeIn(lbl_a), FadeIn(icon_b), FadeIn(lbl_b),
                ReplacementTransform(cells_a, fraction_a),
                ReplacementTransform(cells_b, fraction_b),
                FadeIn(equals_a), FadeIn(equals_b),
                FadeOut(cells_other),
                run_time=1.0
            )
            self.wait(max(0.1, tracker.duration - 1.4))

        part2_script_2 = "và thấy cổ phiếu CTG có lợi nhuận trung bình cao hơn"
        with self.voiceover(text=part2_script_2) as tracker:
            self.update_subtitle("và thấy cổ phiếu CTG có lợi nhuận trung bình\ncao hơn.", style="default")
            
            # Create a target Group for positioning
            res_a = Group(icon_a, lbl_a, equals_a)
            res_b = Group(icon_b, lbl_b, equals_b)
            
            # Build target compact configurations (centered horizontally)
            target_a = res_a.copy().arrange(RIGHT, buff=0.2).move_to([0, 0.8, 0]).scale(1.2)
            target_b = res_b.copy().arrange(RIGHT, buff=0.2).move_to([0, -0.8, 0])
            
            self.sp(
                FadeOut(fraction_a),
                FadeOut(fraction_b),
                icon_a.animate.move_to(target_a[0].get_center()).scale(1.2),
                lbl_a.animate.move_to(target_a[1].get_center()).scale(1.2).set_color(C_WARNING),
                equals_a.animate.move_to(target_a[2].get_center()).scale(1.2).set_color(C_WARNING),
                
                icon_b.animate.move_to(target_b[0].get_center()).set_opacity(0.4),
                lbl_b.animate.move_to(target_b[1].get_center()).set_opacity(0.4),
                equals_b.animate.move_to(target_b[2].get_center()).set_opacity(0.4),
                run_time=0.8
            )
            self.sp(Wiggle(res_a, run_time=0.8))
            self.wait(max(0.1, tracker.duration - 1.6))

        self._lift()
        self.clear_content()
