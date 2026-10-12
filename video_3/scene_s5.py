"""
scene_s5.py – S5: Hiệp phương sai & Lý thuyết Markowitz
"""

from manim import *
from config import FONT, C_SUCCESS, C_PRIMARY, C_WHITE, C_WARNING, C_GRAY, C_PURPLE, C_DANGER, SCRIPTS, SUBS
from helpers import skill_pop_in, rnode, load_icon, make_centered_markup

def make_fraction(num_str, denom_str, color=C_WHITE, font_size=16):
    num_txt = MarkupText(num_str, font=FONT, font_size=font_size, color=color, weight=BOLD)
    denom_txt = MarkupText(denom_str, font=FONT, font_size=font_size, color=color, weight=BOLD)
    line = Line(start=LEFT*0.5, end=RIGHT*0.5, color=color, stroke_width=2)
    w = max(num_txt.width, denom_txt.width) + 0.2
    line.stretch_to_fit_width(w)
    return VGroup(num_txt, line, denom_txt).arrange(DOWN, buff=0.08)

def make_sqrt_fraction(num_str, denom_str, color=C_WHITE, font_size=12):
    frac = make_fraction(num_str, denom_str, color, font_size)
    h = frac.height
    w = frac.width
    c = frac.get_center()
    p1 = c + LEFT*(w/2 + 0.25) + DOWN*0.1
    p2 = c + LEFT*(w/2 + 0.15) + DOWN*0.2
    p3 = c + LEFT*(w/2 + 0.05) + UP*(h/2 + 0.1)
    p4 = c + RIGHT*(w/2 + 0.1) + UP*(h/2 + 0.1)
    
    sqrt_line = VMobject(color=color, stroke_width=2)
    sqrt_line.set_points_as_corners([p1, p2, p3, p4])
    return VGroup(frac, sqrt_line)

class SceneTotalProbMixin:
    def scene_total_prob(self):
        ttl = self.create_title("Hiệp phương sai")

        # 1. Lý thuyết Markowitz và MPT Card to căn giữa
        mpt_icon = load_icon("icon_books", width=1.5, bg_color=C_PURPLE)
        mpt_txt = make_centered_markup("Lý thuyết Danh mục\nĐầu tư Hiện đại", font=FONT, font_size=28, color=C_WHITE, weight=BOLD, line_spacing=0.2)
        mpt_grp = VGroup(mpt_icon, mpt_txt).arrange(DOWN, buff=0.4)
        mpt_box = SurroundingRectangle(mpt_grp, color=C_PURPLE, buff=0.6, stroke_width=4, fill_color=C_GRAY, fill_opacity=0.1)
        big_mpt_card = VGroup(mpt_box, mpt_grp).move_to([0, 0, 0])

        part1_script = "Để trả lời được câu hỏi này, chúng ta sẽ sử dụng Lý thuyết Danh mục Đầu tư Hiện đại do Harry Markowitz đề xuất."
        with self.voiceover(text=part1_script) as tracker:
            self.update_subtitle("Để trả lời câu hỏi này, chúng ta sử dụng\nLý thuyết Danh mục Đầu tư Hiện đại.", style="default")
            self.sp(Write(ttl, run_time=min(0.5, tracker.duration * 0.3)))
            self.sp(skill_pop_in(big_mpt_card, sound=True, run_time=0.8))
            
            # Thu nhỏ và chỉ xuống khung ghi tên Harry Markowitz
            author_card = rnode("Harry Markowitz", C_PURPLE, w=4.0, h=0.8, fs=22, bold=True).move_to([0, -0.8, 0])
            arrow_to_author = Arrow(start=[0, 0.8, 0] + DOWN*0.2, end=author_card.get_top(), color=C_WHITE, stroke_width=4)
            
            self.sp(big_mpt_card.animate.scale(0.6).move_to([0, 1.8, 0]), run_time=0.8)
            self.sp(Create(arrow_to_author), run_time=0.4)
            self.sp(skill_pop_in(author_card, sound=True, run_time=0.5))
            self.wait(max(0.1, tracker.duration - 2.5))

        # 2. Độ lệch chuẩn CTG và FPT (Công thức tổng quát rồi biến thành công thức thay số)
        icon_sd_a = ImageMobject(os.path.join(os.path.dirname(__file__), "ctg.png")).scale_to_fit_width(0.6)
        lbl_sd_a_gen = MarkupText("CTG: σ<sub>CTG</sub> =", font=FONT, font_size=20, color=C_PRIMARY, weight=BOLD)
        frac_a_gen = make_sqrt_fraction("Σ(x<sub>CTG,i</sub> - ̄x<sub>CTG</sub>)²", "n - 1", color=C_WHITE, font_size=20)
        formula_sd_a_gen = Group(icon_sd_a, lbl_sd_a_gen, frac_a_gen).arrange(RIGHT, buff=0.2).move_to([0, 0.8, 0])
        
        icon_sd_b = ImageMobject(os.path.join(os.path.dirname(__file__), "fpt.png")).scale_to_fit_width(0.6)
        lbl_sd_b_gen = MarkupText("FPT: σ<sub>FPT</sub> =", font=FONT, font_size=20, color=C_SUCCESS, weight=BOLD)
        frac_b_gen = make_sqrt_fraction("Σ(x<sub>FPT,i</sub> - ̄x<sub>FPT</sub>)²", "n - 1", color=C_WHITE, font_size=20)
        formula_sd_b_gen = Group(icon_sd_b, lbl_sd_b_gen, frac_b_gen).arrange(RIGHT, buff=0.2).move_to([0, -0.8, 0])

        icon_sd_a_copy = ImageMobject(os.path.join(os.path.dirname(__file__), "ctg.png")).scale_to_fit_width(0.6)
        lbl_sd_a_num = MarkupText("CTG: σ<sub>CTG</sub> =", font=FONT, font_size=20, color=C_PRIMARY, weight=BOLD)
        frac_a_num = make_sqrt_fraction("(9.40% - 5.39%)² + ... + (-2.76% - 5.39%)²", "5 - 1", color=C_WHITE, font_size=16)
        equals_a = MarkupText("= 6.73%", font=FONT, font_size=20, color=C_PRIMARY, weight=BOLD)
        formula_sd_a_num = Group(icon_sd_a_copy, lbl_sd_a_num, frac_a_num, equals_a).arrange(RIGHT, buff=0.15).move_to([0, 0.8, 0])
        if formula_sd_a_num.width > 8.0:
            formula_sd_a_num.scale_to_fit_width(8.0)

        icon_sd_b_copy = ImageMobject(os.path.join(os.path.dirname(__file__), "fpt.png")).scale_to_fit_width(0.6)
        lbl_sd_b_num = MarkupText("FPT: σ<sub>FPT</sub> =", font=FONT, font_size=20, color=C_SUCCESS, weight=BOLD)
        frac_b_num = make_sqrt_fraction("(2.33% - 0.89%)² + ... + (11.72% - 0.89%)²", "5 - 1", color=C_WHITE, font_size=16)
        equals_b = MarkupText("= 7.37%", font=FONT, font_size=20, color=C_SUCCESS, weight=BOLD)
        formula_sd_b_num = Group(icon_sd_b_copy, lbl_sd_b_num, frac_b_num, equals_b).arrange(RIGHT, buff=0.15).move_to([0, -0.8, 0])
        if formula_sd_b_num.width > 8.0:
            formula_sd_b_num.scale_to_fit_width(8.0)

        part2_script_1 = "Từ dữ liệu trên, ta sẽ tính độ lệch chuẩn để đánh giá mức độ biến động của từng cổ phiếu."
        with self.voiceover(text=part2_script_1) as tracker:
            self.update_subtitle("Ta tính độ lệch chuẩn để đánh giá\nmức độ biến động của từng cổ phiếu.", style="default")
            
            # Biến mất các thành phần trước và hiện 2 công thức tổng quát
            self.sp(FadeOut(big_mpt_card), FadeOut(author_card), FadeOut(arrow_to_author), run_time=0.4)
            self.sp(skill_pop_in(formula_sd_a_gen, sound=True), skill_pop_in(formula_sd_b_gen, sound=True), run_time=0.8)
            self.wait(1.0)
            
            # Biến đổi thành công thức thay số và kết quả (dùng ReplacementTransform từng thành phần cho mượt)
            self.sp(
                ReplacementTransform(icon_sd_a, icon_sd_a_copy),
                ReplacementTransform(lbl_sd_a_gen, lbl_sd_a_num),
                ReplacementTransform(frac_a_gen, frac_a_num),
                FadeIn(equals_a),
                
                ReplacementTransform(icon_sd_b, icon_sd_b_copy),
                ReplacementTransform(lbl_sd_b_gen, lbl_sd_b_num),
                ReplacementTransform(frac_b_gen, frac_b_num),
                FadeIn(equals_b),
                run_time=1.0
            )
            self.wait(max(0.1, tracker.duration - 2.2))

        # 3. Đưa 2 kết quả vào giữa màn hình một chút tránh deadzone (hạ thấp xuống tí) và vẽ 2 khung riêng biệt
        res_a = MarkupText("σ<sub>CTG</sub> = 6.73%", font=FONT, font_size=28, color=C_DANGER, weight=BOLD).move_to([-2.2, -1.1, 0])
        res_b = MarkupText("σ<sub>FPT</sub> = 7.37%", font=FONT, font_size=28, color=C_SUCCESS, weight=BOLD).move_to([2.2, -1.1, 0])
        
        box_a = SurroundingRectangle(res_a, color=C_DANGER, buff=0.3, stroke_width=2.5)
        box_b = SurroundingRectangle(res_b, color=C_SUCCESS, buff=0.3, stroke_width=2.5)
        
        # Phóng to chữ rủi ro và biểu tượng (đẩy lên cao hơn chút)
        risk_icon = load_icon("icon_shield_warning", width=1.5, bg_color=C_DANGER).move_to([0, 1.8, 0])
        risk_lbl = Text("Rủi ro", font=FONT, font_size=28, color=C_DANGER, weight=BOLD).next_to(risk_icon, DOWN, buff=0.15)
        risk_grp = VGroup(risk_icon, risk_lbl)
        
        arrow_a = Arrow(start=[0, 0.3, 0] + LEFT*0.3, end=[-2.2, -0.7, 0], color=C_DANGER, stroke_width=4)
        arrow_b = Arrow(start=[0, 0.3, 0] + RIGHT*0.3, end=[2.2, -0.7, 0], color=C_SUCCESS, stroke_width=4)

        part2_script_2 = "Độ lệch chuẩn càng lớn thì rủi ro càng cao."
        with self.voiceover(text=part2_script_2) as tracker:
            self.update_subtitle("Độ lệch chuẩn càng lớn thì rủi ro càng cao.", style="default")
            
            target_icon_a_pos = res_a.get_bottom() + DOWN * 0.95
            target_icon_b_pos = res_b.get_bottom() + DOWN * 0.95
            
            # Thay thế các thẻ công thức bằng kết quả, di chuyển logo xuống dưới kết quả, phóng to logo, hiện 2 khung và các mũi tên rủi ro
            self.sp(
                FadeOut(lbl_sd_a_num), FadeOut(frac_a_num), FadeOut(equals_a),
                FadeOut(lbl_sd_b_num), FadeOut(frac_b_num), FadeOut(equals_b),
                icon_sd_a_copy.animate.move_to(target_icon_a_pos).scale(1.2),
                icon_sd_b_copy.animate.move_to(target_icon_b_pos).scale(1.2),
                FadeIn(res_a), FadeIn(res_b), Create(box_a), Create(box_b),
                run_time=0.8
            )
            self.sp(skill_pop_in(risk_grp, sound=True), Create(arrow_a), Create(arrow_b), run_time=0.6)
            self.sp(Wiggle(risk_grp), run_time=0.8)
            self.wait(max(0.1, tracker.duration - 2.2))

        # Ẩn các thành phần liên quan rủi ro
        self.sp(
            FadeOut(res_a), FadeOut(res_b), FadeOut(box_a), FadeOut(box_b),
            FadeOut(icon_sd_a_copy), FadeOut(icon_sd_b_copy),
            FadeOut(risk_grp), FadeOut(arrow_a), FadeOut(arrow_b), 
            run_time=0.4
        )

        # 4. Hiển thị hai đồ thị A & B dao động cùng chiều
        ax = Axes(
            x_range=[0, 4, 1],
            y_range=[-1.5, 2, 1],
            x_length=6.0,
            y_length=2.5,
            axis_config={"color": C_GRAY}
        ).move_to([0, 0.5, 0])
        
        curve_a = ax.plot(lambda x: 0.5 + 0.4*np.sin(x*5) + 0.1*x, color=C_PRIMARY, x_range=[0, 3.8])
        curve_b = ax.plot(lambda x: -0.5 + 0.35*np.sin(x*5) + 0.08*x, color=C_SUCCESS, x_range=[0, 3.8])
        curves = VGroup(ax, curve_a, curve_b)

        part3_script_1 = "Tuy nhiên, rủi ro của danh mục không chỉ phụ thuộc vào từng cổ phiếu riêng lẻ, mà còn phụ thuộc vào cách chúng biến động so với nhau."
        with self.voiceover(text=part3_script_1) as tracker:
            self.update_subtitle("Rủi ro danh mục phụ thuộc vào\ncách các cổ phiếu biến động cùng nhau.", style="default")
            self.sp(Create(ax), run_time=0.5)
            self.sp(Create(curve_a), Create(curve_b), run_time=1.0)
            self.wait(max(0.1, tracker.duration - 1.5))

        # 5. Ta sử dụng hiệp phương sai
        cov_title = Text("Hiệp phương sai", font=FONT, font_size=28, color=C_WARNING).move_to([0, -0.4, 0])
        cov_box = SurroundingRectangle(cov_title, color=C_WARNING, buff=0.4, stroke_width=4)
        cov_boxed = VGroup(cov_title, cov_box)

        part3_script_2 = "Để biết hai cổ phiếu ảnh hưởng lẫn nhau như thế nào, ta sử dụng hiệp phương sai."
        with self.voiceover(text=part3_script_2) as tracker:
            self.update_subtitle("Để biết mức độ ảnh hưởng lẫn nhau,\nta sử dụng Hiệp phương sai.", style="default")
            
            # Cho đồ thị bé lại
            self.sp(curves.animate.scale(0.55).move_to([0, 1.8, 0]), run_time=0.6)
            
            # Hiệp phương sai zoom to ra và đóng khung ở trung tâm
            self.sp(skill_pop_in(cov_boxed, sound=True), run_time=0.6)
            self.wait(max(0.1, tracker.duration - 1.2))

        # 6. Cho đồ thị biến mất đi rồi mới hiện bảng ý nghĩa ra
        cov_table = MobjectTable(
            [[Text("> 0", font=FONT, font_size=18), Text("Cùng chiều", font=FONT, font_size=18)],
             [Text("< 0", font=FONT, font_size=18), Text("Ngược chiều", font=FONT, font_size=18)],
             [Text("≈ 0", font=FONT, font_size=18), Text("Độc lập", font=FONT, font_size=18)]],
            col_labels=[MarkupText("Cov(CTG, FPT)", font=FONT, font_size=18, weight=BOLD), Text("Ý nghĩa", font=FONT, font_size=18, weight=BOLD)],
            include_outer_lines=True,
            line_config={"color": C_GRAY}
        ).scale(1.15).move_to([0, 0.5, 0])
        
        cov_table.get_entries((2, 1)).set_color(C_SUCCESS)
        cov_table.get_entries((2, 2)).set_color(C_SUCCESS)
        cov_table.get_entries((3, 1)).set_color(C_DANGER)
        cov_table.get_entries((3, 2)).set_color(C_DANGER)
        cov_table.get_entries((4, 1)).set_color(C_GRAY)
        cov_table.get_entries((4, 2)).set_color(C_GRAY)

        part4_script_1 = "Hiệp phương sai đo lường mức độ biến động cùng nhau của hai biến ngẫu nhiên."
        with self.voiceover(text=part4_script_1) as tracker:
            self.update_subtitle("Hiệp phương sai đo lường mức độ\nbiến động cùng nhau của 2 biến ngẫu nhiên.", style="default")
            
            # Cho đồ thị biến mất hoàn toàn
            self.sp(FadeOut(curves), run_time=0.4)
            # Sau đó mới hiện bảng ý nghĩa ra
            self.sp(ReplacementTransform(cov_boxed, cov_table), run_time=0.8)
            self.wait(max(0.1, tracker.duration - 1.2))

        # 7. Bảng biến mất và hiện rõ công thức tổng quát -> thay số -> kết quả ra giữa màn hình
        # Tách biệt các biến label để tránh lỗi hiện trùng lặp của Manim
        cov_lbl_gen = MarkupText("Cov(CTG, FPT) = ", font=FONT, font_size=22, color=C_WARNING, weight=BOLD)
        cov_frac_gen = make_fraction("Σ(x<sub>CTG,i</sub> - x̄<sub>CTG</sub>)(x<sub>FPT,i</sub> - x̄<sub>FPT</sub>)", "n - 1", color=C_WHITE, font_size=18)
        cov_formula_gen = VGroup(cov_lbl_gen, cov_frac_gen).arrange(RIGHT, buff=0.2).move_to([0, 0, 0])

        cov_lbl_num = MarkupText("Cov(CTG, FPT) = ", font=FONT, font_size=22, color=C_WARNING, weight=BOLD)
        cov_frac_num = make_fraction("(9.40% - 5.39%)(2.33% - 0.89%) + ... + (-2.76% - 5.39%)(11.72% - 0.89%)", "5 - 1", color=C_WHITE, font_size=15)
        cov_formula_num = VGroup(cov_lbl_num, cov_frac_num).arrange(RIGHT, buff=0.2).move_to([0, 0, 0])
        if cov_formula_num.width > 8.0:
            cov_formula_num.scale_to_fit_width(8.0)

        part4_script_2 = "Sau khi áp dụng công thức hiệp phương sai cho dữ liệu lịch sử, ta thu được một giá trị là âm mười phẩy bốn mươi tám."
        with self.voiceover(text=part4_script_2) as tracker:
            self.update_subtitle("Sau khi áp dụng công thức,\nta thu được kết quả là -10.48.", style="default")
            
            # Bảng biến mất, hiện công thức tổng quát ra giữa màn hình
            self.sp(FadeOut(cov_table), run_time=0.4)
            self.sp(skill_pop_in(cov_formula_gen, sound=True), run_time=0.8)
            self.wait(1.0)
            
            # Biến thành công thức đã thay số
            self.sp(ReplacementTransform(cov_formula_gen, cov_formula_num), run_time=1.0)
            self.wait(1.0)
            
            # Morph ra kết quả thôi, không cần phần tính toán nữa, căn giữa
            cov_res_final = MarkupText("Cov(CTG, FPT) = -10.48", font=FONT, font_size=28, color=C_WARNING, weight=BOLD).move_to([0, 0, 0])
            
            self.sp(ReplacementTransform(cov_formula_num, cov_res_final), run_time=0.8)
            self.sp(Wiggle(cov_res_final), run_time=1.0)
            self.wait(max(0.1, tracker.duration - 3.8))

        self._lift()
        self.clear_content()
