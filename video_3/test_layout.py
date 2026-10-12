from manim import *
from config import FONT, C_PRIMARY, C_PURPLE, C_WARNING, C_GRAY, C_WHITE, C_SUCCESS, C_DANGER, VIDEO_W, VIDEO_H, FRAME_W, FRAME_H
from helpers import make_centered_markup

config.pixel_width      = VIDEO_W
config.pixel_height     = VIDEO_H
config.frame_width      = FRAME_W
config.frame_height     = FRAME_H

def make_bold_text(text):
    return Text(text, font=FONT, font_size=20, weight=BOLD)

def make_fraction(num_str, denom_str, color=C_WHITE, font_size=16):
    num_txt = MarkupText(num_str, font=FONT, font_size=font_size, color=color, weight=BOLD)
    denom_txt = MarkupText(denom_str, font=FONT, font_size=font_size, color=color, weight=BOLD)
    line = Line(start=LEFT*0.5, end=RIGHT*0.5, color=color, stroke_width=2)
    w = max(num_txt.width, denom_txt.width) + 0.2
    line.stretch_to_fit_width(w)
    return VGroup(num_txt, line, denom_txt).arrange(DOWN, buff=0.08)

class TestLayout(Scene):
    def construct(self):
        # Background
        self.camera.background_color = "#121214"
        
        # Title
        ttl = Text("Dữ liệu lịch sử", font=FONT, font_size=24, color=C_PRIMARY, weight=BOLD)
        ttl.to_edge(UP, buff=0.4)
        
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
                make_centered_markup("Tháng", font=FONT, font_size=16, color=C_WHITE, weight=BOLD),
                make_centered_markup("Giá cuối tháng\nCTG", font=FONT, font_size=16, color=C_PRIMARY, weight=BOLD),
                make_centered_markup("Tỷ suất\nCTG", font=FONT, font_size=16, color=C_PRIMARY, weight=BOLD),
                make_centered_markup("Giá cuối tháng\nFPT", font=FONT, font_size=16, color=C_SUCCESS, weight=BOLD),
                make_centered_markup("Tỷ suất\nFPT", font=FONT, font_size=16, color=C_SUCCESS, weight=BOLD)
            ],
            h_buff=0.7,
            v_buff=0.5,
            element_to_mobject=make_bold_text,
            include_outer_lines=True,
            line_config={"color": C_GRAY}
        ).scale(0.7).move_to([0, 1.2, 0])

        for idx in range(1, 6):
            val_a = data[idx-1][2]
            color_a = C_DANGER if "-" in val_a else C_SUCCESS
            history_table.get_entries((idx+1, 3)).set_color(color_a)
            
            val_b = data[idx-1][4]
            color_b = C_DANGER if "-" in val_b else C_SUCCESS
            history_table.get_entries((idx+1, 5)).set_color(color_b)
            
        table_subtitle = Text("Thời gian: 6/2025 - 10/2025", font=FONT, font_size=26, color=C_WHITE).next_to(history_table, DOWN, buff=0.25)
            
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

        self.add(ttl, history_table, table_subtitle)
