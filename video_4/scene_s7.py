"""
scene_s7.py – S7: Phương pháp 2: Leverage
"""

from manim import *
from config import FONT, C_PRIMARY, C_SUCCESS, C_WARNING, C_GRAY, C_WHITE, C_DANGER, FAMI_BLUE, FAMI_CYAN
from helpers import skill_pop_in

def get_math_design(tex, fallback_markup, font_size=24, color=WHITE):
    try:
        return MathTex(tex, font_size=font_size, color=color)
    except Exception:
        return MarkupText(fallback_markup, font=FONT, font_size=font_size - 4, color=color)

def get_leverage_formula(font_size=42, color=WHITE):
    try:
        return MathTex(r"h_i = \frac{1}{n} + \frac{(x_i - \bar{x})^2}{\displaystyle\sum (x_j - \bar{x})^2}", font_size=font_size, color=color)
    except Exception:
        h_part = MarkupText("h<sub>i</sub> = ", font=FONT, font_size=font_size - 6, color=color)
        num1 = MarkupText("1", font=FONT, font_size=font_size - 10, color=color)
        den1 = MarkupText("n", font=FONT, font_size=font_size - 10, color=color)
        line1 = Line(start=[-0.15, 0, 0], end=[0.15, 0, 0], stroke_width=2, color=color)
        num1.next_to(line1, UP, buff=0.08)
        den1.next_to(line1, DOWN, buff=0.08)
        frac1 = VGroup(num1, line1, den1)
        plus_part = MarkupText(" + ", font=FONT, font_size=font_size - 6, color=color)
        num2 = MarkupText("(x<sub>i</sub> - x̄)<sup>2</sup>", font=FONT, font_size=font_size - 10, color=color)
        den2 = MarkupText("Σ (x<sub>j</sub> - x̄)<sup>2</sup>", font=FONT, font_size=font_size - 10, color=color)
        line2_w = max(num2.width, den2.width) + 0.15
        line2 = Line(start=[-line2_w/2, 0, 0], end=[line2_w/2, 0, 0], stroke_width=2, color=color)
        num2.next_to(line2, UP, buff=0.08)
        den2.next_to(line2, DOWN, buff=0.08)
        frac2 = VGroup(num2, line2, den2)
        return VGroup(h_part, frac1, plus_part, frac2).arrange(RIGHT, buff=0.1)

def get_threshold_formula(font_size=36, color=WHITE):
    try:
        return MathTex(r"h > \frac{2(k + 1)}{n}", font_size=font_size, color=color)
    except Exception:
        h_part = MarkupText("h &gt; ", font=FONT, font_size=font_size - 6, color=color)
        num = MarkupText("2(k + 1)", font=FONT, font_size=font_size - 10, color=color)
        den = MarkupText("n", font=FONT, font_size=font_size - 10, color=color)
        line_w = max(num.width, den.width) + 0.15
        line = Line(start=[-line_w/2, 0, 0], end=[line_w/2, 0, 0], stroke_width=2, color=color)
        num.next_to(line, UP, buff=0.08)
        den.next_to(line, DOWN, buff=0.08)
        frac = VGroup(num, line, den)
        return VGroup(h_part, frac).arrange(RIGHT, buff=0.1)

def get_brackets(mobject, color=C_WARNING, stroke_width=2, tick_length=0.15, buff=0.12):
    left = mobject.get_left()[0] - buff
    right = mobject.get_right()[0] + buff
    top = mobject.get_top()[1] + buff
    bottom = mobject.get_bottom()[1] - buff
    
    left_vertical = Line(start=[left, top, 0], end=[left, bottom, 0], color=color, stroke_width=stroke_width)
    left_top_tick = Line(start=[left, top, 0], end=[left + tick_length, top, 0], color=color, stroke_width=stroke_width)
    left_bottom_tick = Line(start=[left, bottom, 0], end=[left + tick_length, bottom, 0], color=color, stroke_width=stroke_width)
    left_bracket = VGroup(left_vertical, left_top_tick, left_bottom_tick)
    
    right_vertical = Line(start=[right, top, 0], end=[right, bottom, 0], color=color, stroke_width=stroke_width)
    right_top_tick = Line(start=[right, top, 0], end=[right - tick_length, top, 0], color=color, stroke_width=stroke_width)
    right_bottom_tick = Line(start=[right, bottom, 0], end=[right - tick_length, bottom, 0], color=color, stroke_width=stroke_width)
    right_bracket = VGroup(right_vertical, right_top_tick, right_bottom_tick)
    
    return left_bracket, right_bracket

def create_horizontal_dots(color=WHITE, buff=0.08):
    return VGroup(
        Dot(radius=0.025, color=color),
        Dot(radius=0.025, color=color),
        Dot(radius=0.025, color=color)
    ).arrange(RIGHT, buff=buff)

def create_vertical_dots(color=WHITE, buff=0.08):
    return VGroup(
        Dot(radius=0.025, color=color),
        Dot(radius=0.025, color=color),
        Dot(radius=0.025, color=color)
    ).arrange(DOWN, buff=buff)

def create_diagonal_dots(color=WHITE, buff=0.08):
    dots = VGroup(
        Dot(radius=0.025, color=color),
        Dot(radius=0.025, color=color),
        Dot(radius=0.025, color=color)
    )
    dots[0].move_to([-0.08, 0.08, 0])
    dots[1].move_to([0, 0, 0])
    dots[2].move_to([0.08, -0.08, 0])
    return dots

class SceneS7Mixin:
    def scene_s7(self):
        ttl = self.create_title("Độ đo Leverage")

        # Start of scene Leverage title & underline
        leverage_title_txt = Text("Leverage", font=FONT, font_size=64, color=C_DANGER, weight=BOLD).move_to([0, 0.5, 0])
        underline = Underline(leverage_title_txt, color=C_DANGER, stroke_width=3)
        intro_grp = VGroup(leverage_title_txt, underline)

        # Scatter plot axes
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            x_length=5.5,
            y_length=4.0,
            axis_config={"color": C_GRAY},
        ).move_to([-0.8, 0.2, 0])

        # Grid lines for charts
        grid_lines = VGroup()
        for x in range(1, 10):
            grid_lines.add(DashedLine(ax.c2p(x, 0), ax.c2p(x, 10), color="#1e293b", stroke_width=1))
        for y in range(1, 10):
            grid_lines.add(DashedLine(ax.c2p(0, y), ax.c2p(10, y), color="#1e293b", stroke_width=1))

        # Axis ticks/numbers (using buff=0.22 to prevent overlap)
        x_nums = VGroup(*[
            Text(str(val), font=FONT, font_size=10, color=C_GRAY).next_to(ax.c2p(val, 0), DOWN, buff=0.22)
            for val in range(2, 10, 2)
        ])
        y_nums = VGroup(*[
            Text(str(val), font=FONT, font_size=10, color=C_GRAY).next_to(ax.c2p(0, val), LEFT, buff=0.22)
            for val in range(2, 10, 2)
        ])

        # Clustered normal blue data points centered around x = 3.5
        normal_data = [
            [2.0, 2.5], [2.5, 2.8], [3.0, 3.2], [3.5, 3.5], [3.8, 3.6],
            [4.2, 3.9], [4.5, 4.1], [5.0, 4.5]
        ]
        dots = VGroup(*[
            Dot(ax.c2p(x, y), color=C_PRIMARY, radius=0.08)
            for x, y in normal_data
        ])

        # Mean x vertical dashed line (x = 3.5)
        mean_line = DashedLine(
            start=ax.c2p(3.5, 0.5), end=ax.c2p(3.5, 8.5),
            color=C_WHITE, stroke_width=2
        )
        mean_lbl = Text("x̄", font=FONT, font_size=16, color=C_WHITE).next_to(mean_line, UP, buff=0.1)

        # Red Leverage point starting close
        outlier = Dot(ax.c2p(5.5, 4.8), color=C_DANGER, radius=0.12)
        outlier_lbl = Text("Quan sát X", font=FONT, font_size=12, color=C_DANGER).next_to(outlier, UP, buff=0.1)

        # -------------------------------------------------------------
        # Leverage formula in LaTeX (enlarged with fraction fallback support)
        formula_leverage = get_leverage_formula(font_size=42, color=C_WHITE).move_to([0, 2.7, 0])
        # -------------------------------------------------------------

        # Leverage Visual Bar / Gauge on the right
        bar_bg = Rectangle(width=0.3, height=2.5, color=C_GRAY).move_to([3.4, 0.2, 0])
        initial_height = 0.3
        initial_y = bar_bg.get_bottom()[1] + initial_height / 2
        bar_fill = Rectangle(
            width=0.3, height=initial_height,
            fill_color=C_DANGER, fill_opacity=0.8, stroke_width=0
        ).move_to([3.4, initial_y, 0])
        bar_lbl = Text("Leverage", font=FONT, font_size=12, color=C_WHITE).next_to(bar_bg, UP, buff=0.1)
        bar_grp = VGroup(bar_bg, bar_fill, bar_lbl)

        # --- ASSESSMENT THRESHOLD (Formula only in card, title/note outside, centered) ---
        thresh_formula = get_threshold_formula(font_size=36, color=C_WHITE).move_to([0, 0, 0])

        box_thresh = RoundedRectangle(
            width=thresh_formula.width + 0.4, height=thresh_formula.height + 0.25, corner_radius=0.1,
            color=FAMI_CYAN, fill_color="#0f172a", fill_opacity=0.95, stroke_width=2
        ).move_to(thresh_formula.get_center())

        lbl_thresh_title = Text("Ngưỡng đánh giá", font=FONT, font_size=32, color=FAMI_CYAN, weight=BOLD)
        lbl_thresh_title.next_to(box_thresh, UP, buff=0.4)
        
        thresh_note = MarkupText("<b>k:</b> Số biến độc lập      <b>n:</b> Số lượng quan sát", font=FONT, font_size=24, color=C_GRAY)
        thresh_note.next_to(box_thresh, DOWN, buff=0.4)
        
        thresh_card_grp = VGroup(lbl_thresh_title, box_thresh, thresh_formula, thresh_note).move_to([0, -0.1, 0])

        # --- MULTI-VARIABLE EXTENSION (Hat Matrix) ---
        formula_hat_large = get_math_design(
            r"H = X(X^T X)^{-1} X^T",
            r"H = X(X<sup>T</sup>X)<sup>-1</sup>X<sup>T</sup>",
            font_size=42, color=C_WHITE
        ).move_to([0, 0.2, 0])

        # Box around formula - Snug fit!
        formula_hat_box = RoundedRectangle(
            width=formula_hat_large.width + 1, height=formula_hat_large.height + 1,
            corner_radius=0.12, color=C_WARNING, fill_color="#0f172a", fill_opacity=0.9, stroke_width=3
        ).move_to(formula_hat_large.get_center())
        formula_hat_grp = VGroup(formula_hat_box, formula_hat_large)
        
        # Spawn letter X at formula's position to separate and move it
        x_char = Text("X", font=FONT, font_size=20, color=C_WARNING, weight=BOLD)
        matrix_title = MarkupText("là Ma trận dữ liệu đầu vào:", font=FONT, font_size=20, color=C_WARNING)
        
        # Matrix diagram variables - Row-column grid representation
        # Ba chấm hàng/cột/chéo
        dots_r1 = create_horizontal_dots(C_WHITE, buff=0.06)
        dots_r2 = create_horizontal_dots(C_WHITE, buff=0.06)
        dots_rn = create_horizontal_dots(C_WHITE, buff=0.06)
        
        dots_c1 = create_vertical_dots(C_WHITE, buff=0.06)
        dots_c2 = create_vertical_dots(C_WHITE, buff=0.06)
        dots_cn = create_vertical_dots(C_WHITE, buff=0.06)
        
        dots_diag = create_diagonal_dots(C_WHITE, buff=0.06)
        
        # Cột 1
        sig11 = Text("1", font=FONT, font_size=18, color=C_WHITE)
        sig21 = Text("1", font=FONT, font_size=18, color=C_WHITE)
        sign1 = Text("1", font=FONT, font_size=18, color=C_WHITE)
        col1 = VGroup(sig11, sig21, dots_c1, sign1).arrange(DOWN, buff=0.22)
        
        # Cột 2
        sig12 = MarkupText("x<sub>11</sub>", font=FONT, font_size=18, color=C_WHITE)
        sig22 = MarkupText("x<sub>21</sub>", font=FONT, font_size=18, color=C_WHITE)
        sign2 = MarkupText("x<sub>n1</sub>", font=FONT, font_size=18, color=C_WHITE)
        col2 = VGroup(sig12, sig22, dots_c2, sign2)
        
        # Cột 3
        col3 = VGroup(dots_r1, dots_r2, dots_diag, dots_rn)
        
        # Cột 4
        sig1n = MarkupText("x<sub>1k</sub>", font=FONT, font_size=18, color=C_WHITE)
        sig2n = MarkupText("x<sub>2k</sub>", font=FONT, font_size=18, color=C_WHITE)
        signn = MarkupText("x<sub>nk</sub>", font=FONT, font_size=18, color=C_WHITE)
        col4 = VGroup(sig1n, sig2n, dots_cn, signn)
        
        # Sắp xếp các cột theo chiều ngang
        col2.next_to(col1, RIGHT, buff=0.45)
        col3.next_to(col2, RIGHT, buff=0.45)
        col4.next_to(col3, RIGHT, buff=0.45)
        
        # Căn chỉnh hoàn hảo các phần tử theo hàng dọc (dựa theo y-coordinate của col1)
        for i in range(4):
            col2[i].move_to([col2[i].get_x(), col1[i].get_y(), 0])
            col3[i].move_to([col3[i].get_x(), col1[i].get_y(), 0])
            col4[i].move_to([col4[i].get_x(), col1[i].get_y(), 0])
            
        matrix_rows = VGroup(col1, col2, col3, col4).move_to([0, -0.4, 0])
        
        matrix_left_bracket, matrix_right_bracket = get_brackets(matrix_rows, color=C_WARNING, stroke_width=2.5, buff=0.2)
        matrix_dims = Text("Kích thước n × (k+1)", font=FONT, font_size=17, color=C_GRAY).next_to(matrix_rows, DOWN, buff=0.15)
        matrix_body = VGroup(matrix_left_bracket, matrix_rows, matrix_right_bracket)
        matrix_title_grp = VGroup(x_char, matrix_title).arrange(RIGHT, buff=0.15).move_to([0, 0.7, 0])
        target_x_pos = x_char.get_center().copy()
        
        # Boxed Diagonal element explanation group - Repositioned below Matrix X with dynamic snug fit
        h_diag_title = MarkupText("Leverage thứ i", font=FONT, font_size=15, color=FAMI_CYAN, weight=BOLD)
        h_diag_formula = get_math_design(
            r"h_i = H_{ii}",
            r"h<sub>i</sub> = H<sub>ii</sub>",
            font_size=32, color=C_WHITE
        )
        h_diag_desc = Text("Phần tử đường chéo chính của ma trận H", font=FONT, font_size=15, color=C_WHITE)
        
        h_diag_content = VGroup(h_diag_title, h_diag_formula, h_diag_desc).arrange(DOWN, buff=0.15)
        h_diag_box = RoundedRectangle(
            width=h_diag_content.width + 0.3, height=h_diag_content.height + 0.3, corner_radius=0.1,
            color=FAMI_CYAN, fill_color="#0f172a", fill_opacity=0.9, stroke_width=2
        )
        h_diag_grp = VGroup(h_diag_box, h_diag_content).move_to([0, -2.3, 0])

        # Framed Question Card (centered, aligned, dynamic snug fit)
        q_line1 = Text("Điểm dữ liệu này có đủ sức", font=FONT, font_size=22, color=C_WHITE, weight=BOLD)
        q_line2 = Text("kéo lệch mô hình hay không?", font=FONT, font_size=22, color=C_WHITE, weight=BOLD, t2c={"kéo lệch": C_WARNING})
        question_txt = VGroup(q_line1, q_line2).arrange(DOWN, buff=0.15)
        
        question_box = RoundedRectangle(
            width=question_txt.width + 1, height=question_txt.height + 1, corner_radius=0.15,
            color=C_WARNING, fill_color="#0f172a", fill_opacity=0.9, stroke_width=4
        )
        question_card = VGroup(question_box, question_txt).move_to([0, -0.4, 0])
        question_txt.move_to(question_box.get_center())

        # --- ANIMATION FLOW ---

        # 1. Introduce Leverage (with word Leverage morphing to graph)
        part1_script = "Để đánh giá mức độ ảnh hưởng của một điểm đến mô hình. chúng ta sử dụng Leverage, hay độ đòn bẩy."
        with self.voiceover(text=part1_script) as tracker:
            self.update_subtitle("Để đánh giá mức độ ảnh hưởng của một điểm", style="default")
            self.sp(Write(ttl, run_time=0.5))
            self.sp(Write(intro_grp), run_time=0.8)
            self.wait(0.5)
            
            self.update_subtitle("chúng ta sử dụng Leverage.", style="default")
            self.sp(
                ReplacementTransform(intro_grp, VGroup(ax, grid_lines, x_nums, y_nums)),
                LaggedStart(*[FadeIn(d, scale=0.5) for d in dots], lag_ratio=0.1),
                skill_pop_in(outlier, sound=True), FadeIn(outlier_lbl),
                run_time=1.2
            )
            self.wait(max(0.1, tracker.duration - 2.5))

        # 2. Explain Leverage formula and mean distance
        part2_script = "Leverage đo lường mức độ khác biệt của một quan sát so với vị trí trung tâm của dữ liệu."
        with self.voiceover(text=part2_script) as tracker:
            self.update_subtitle("Leverage đo lường mức độ khác biệt của", style="default")
            self.sp(Write(formula_leverage), run_time=0.8)
            self.sp(Create(mean_line), FadeIn(mean_lbl), run_time=0.6)
            self.update_subtitle("quan sát so với vị trí trung tâm dữ liệu.", style="default")
            self.wait(max(0.1, tracker.duration - 2.2))

        # 3. Dynamic Leverage Demo
        part3_script = "Điểm càng xa giá trị trung bình của biến độc lập thì Leverage càng lớn."
        with self.voiceover(text=part3_script) as tracker:
            self.update_subtitle("Điểm càng xa giá trị trung \n bình thì Leverage càng lớn.", style="default")
            
            # Show Leverage gauge
            self.sp(Create(bar_bg), FadeIn(bar_lbl), Create(bar_fill), run_time=0.6)
            self.wait(0.5)

            # Move point further away and increase leverage bar
            new_height = 2.3
            new_y = bar_bg.get_bottom()[1] + new_height / 2
            self.sp(
                outlier.animate.move_to(ax.c2p(9.5, 4.0)),
                outlier_lbl.animate.next_to(ax.c2p(9.5, 4.0), UP, buff=0.1),
                bar_fill.animate.stretch_to_fit_height(new_height).move_to([3.4, new_y, 0]),
                run_time=2.0
            )
            self.sp(Flash(outlier, color=C_DANGER), run_time=0.5)
            self.wait(max(0.1, tracker.duration - 3.6))

        # 4. Assess Threshold (Card pops in center)
        part_thresh_1 = "Để đánh giá Leverage có cao hay không, người ta thường so sánh với ngưỡng hai nhân k cộng một chia n."
        with self.voiceover(text=part_thresh_1) as tracker:
            self.update_subtitle("Đánh giá Leverage bằng cách \n so sánh với ngưỡng 2(k+1)/n.", style="default")
            
            # Fade out scatter plot elements
            all_plot_elements = VGroup(ax, grid_lines, x_nums, y_nums, dots, outlier, outlier_lbl, mean_line, mean_lbl, formula_leverage, bar_grp)
            self.sp(FadeOut(all_plot_elements), run_time=0.8)
            
            # Pop in Threshold Card in the center
            self.sp(skill_pop_in(thresh_card_grp, sound=True), run_time=0.8)
            self.wait(max(0.1, tracker.duration - 1.6))

        part_thresh_2 = "Với k là số biến độc lập và n là số quan sát."
        with self.voiceover(text=part_thresh_2) as tracker:
            self.update_subtitle("k là số biến độc lập,\n n là số quan sát.", style="default")
            self.wait(max(0.1, tracker.duration))

        # 5. Matrix Extension (To center boxed, shrinks, explain X in matrix form)
        part_multi_1 = "Trong trường hợp nhiều biến độc lập, công thức được mở rộng qua ma trận Hat."
        with self.voiceover(text=part_multi_1) as tracker:
            self.update_subtitle("Với nhiều biến, công thức \n mở rộng qua ma trận Hat.", style="default")
            
            # Fade out threshold card
            self.sp(FadeOut(thresh_card_grp), run_time=0.5)
            
            # Show large Hat Matrix formula in the center (boxed)
            self.sp(Create(formula_hat_box), Write(formula_hat_large), run_time=0.8)
            self.wait(0.6)
            
            # Shrink and move formula up to top center
            self.sp(formula_hat_grp.animate.scale(0.75).move_to([0, 1.6, 0]), run_time=1.0)
            self.wait(max(0.1, tracker.duration - 2.9))

        part_multi_2 = "Trong đó, ma trận X là ma trận dữ liệu đầu vào chứa các biến độc lập."
        with self.voiceover(text=part_multi_2) as tracker:
            self.update_subtitle("Trong đó, X là ma trận dữ liệu đầu vào.", style="default")
            # Spawn X at formula position, invisible initially
            x_char.move_to([-0.56, 1.6, 0]).set_opacity(0)
            self.add(x_char)
            
            # Animate moving down to target position and fading in
            self.sp(
                x_char.animate.move_to(target_x_pos).set_opacity(1),
                run_time=0.8
            )
            self.sp(
                Write(matrix_title),
                run_time=0.6
            )
            self.sp(
                Create(matrix_left_bracket), Create(matrix_right_bracket),
                Write(matrix_rows), FadeIn(matrix_dims),
                run_time=1.0
            )
            self.wait(max(0.1, tracker.duration - 2.4))
            
        part_multi_3 = "Giá trị Leverage của điểm thứ i chính là phần tử thứ i trên đường chéo chính của ma trận H."
        with self.voiceover(text=part_multi_3) as tracker:
            self.update_subtitle("Leverage điểm thứ i là \n  phần tử chéo chính của ma trận H.", style="default")
            self.sp(
                Create(h_diag_box), Write(h_diag_title),
                Write(h_diag_formula), Write(h_diag_desc),
                run_time=1.0
            )
            self.wait(max(0.1, tracker.duration - 1.0))

        # 6. Wrap up Leverage role (Morph to framed question card, title persistent)
        part4_script = "Leverage giúp trả lời câu hỏi: điểm này có đủ sức kéo lệch mô hình hay không?"
        with self.voiceover(text=part4_script) as tracker:
            self.update_subtitle("Leverage trả lời câu hỏi: Điểm này \n có đủ sức kéo lệch mô hình hay không?", style="default")
            
            # Morph Hat matrix structure into the framed question card
            all_multi_elements = VGroup(formula_hat_grp, matrix_title_grp, matrix_body, matrix_dims, h_diag_grp)
            self.sp(
                ReplacementTransform(all_multi_elements, question_card),
                run_time=1.2
            )
            self.sp(Wiggle(question_card), run_time=0.8)
            self.wait(max(0.1, tracker.duration - 2.0))

        self._lift()
        self.clear_content()
