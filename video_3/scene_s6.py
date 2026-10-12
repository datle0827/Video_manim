"""
scene_s6.py – S6: Phương sai danh mục đầu tư
"""

from manim import *
from config import FONT, C_SUCCESS, C_PRIMARY, C_WHITE, C_WARNING, C_GRAY, C_DANGER, C_PURPLE, SCRIPTS, SUBS
from helpers import skill_pop_in, rnode, load_icon

def make_sqrt(mobject, color=C_WHITE, stroke_width=2.5):
    """Tạo một ký hiệu căn bậc hai (radical) ôm trọn lấy mobject"""
    w = mobject.width
    h = mobject.height
    c = mobject.get_center()
    
    p1 = c + LEFT*(w/2 + 0.25) + DOWN*0.05
    p2 = c + LEFT*(w/2 + 0.15) + DOWN*0.2
    p3 = c + LEFT*(w/2 + 0.05) + UP*(h/2 + 0.1)
    p4 = c + RIGHT*(w/2 + 0.1) + UP*(h/2 + 0.1)
    
    sqrt_line = VMobject(color=color, stroke_width=stroke_width)
    sqrt_line.set_points_as_corners([p1, p2, p3, p4])
    return VGroup(mobject, sqrt_line)

class SceneSummaryMixin:
    def scene_summary(self):
        ttl = self.create_title("Rủi ro danh mục")

        # 1. wCTG, wFPT chia thành 2 khung riêng biệt, wCTG, wFPT trong 2 ô tròn
        # Dòng w_CTG
        circle_a = Circle(radius=0.35, color=C_PRIMARY, fill_color=C_GRAY, fill_opacity=0.2, stroke_width=3)
        lbl_w_a = MarkupText("w<sub>CTG</sub>", font=FONT, font_size=18, color=C_PRIMARY, weight=BOLD).move_to(circle_a.get_center())
        w_a_badge = VGroup(circle_a, lbl_w_a)
        
        txt_a = MarkupText("Tỷ trọng vốn đầu tư vào cổ phiếu CTG", font=FONT, font_size=18, color=C_WHITE)
        box_a = SurroundingRectangle(txt_a, color=C_PRIMARY, buff=0.25, stroke_width=3, fill_color=C_GRAY, fill_opacity=0.1)
        # Đồng bộ vị trí chữ vào giữa hộp và đặt badge bên trái
        txt_a.move_to(box_a.get_center())
        w_a_badge.next_to(box_a, LEFT, buff=0.3)
        row_a = VGroup(w_a_badge, box_a, txt_a).move_to([0.3, 1.2, 0])

        # Dòng w_FPT
        circle_b = Circle(radius=0.35, color=C_SUCCESS, fill_color=C_GRAY, fill_opacity=0.2, stroke_width=3)
        lbl_w_b = MarkupText("w<sub>FPT</sub>", font=FONT, font_size=18, color=C_SUCCESS, weight=BOLD).move_to(circle_b.get_center())
        w_b_badge = VGroup(circle_b, lbl_w_b)
        
        txt_b = MarkupText("Tỷ trọng vốn đầu tư vào cổ phiếu FPT", font=FONT, font_size=18, color=C_WHITE)
        box_b = SurroundingRectangle(txt_b, color=C_SUCCESS, buff=0.25, stroke_width=3, fill_color=C_GRAY, fill_opacity=0.1)
        # Đồng bộ vị trí chữ vào giữa hộp và đặt badge bên trái
        txt_b.move_to(box_b.get_center())
        w_b_badge.next_to(box_b, LEFT, buff=0.3)
        row_b = VGroup(w_b_badge, box_b, txt_b).move_to([0.3, 0.0, 0])

        weights_card = VGroup(row_a, row_b)

        # Công thức biến ra to rõ giữa màn hình
        formula = MarkupText(
            "Var(P) = w<sub>CTG</sub>²·σ<sub>CTG</sub>² + w<sub>FPT</sub>²·σ<sub>FPT</sub>² + 2·w<sub>CTG</sub>·w<sub>FPT</sub>·Cov(CTG, FPT)",
            font=FONT,
            font_size=20,
            color=C_WHITE
        ).move_to([0, 0, 0])

        part1_script_1 = "Quay lại câu hỏi ban đầu, ta đặt w c t g là tỷ trọng vốn đầu tư vào cổ phiếu C T G và w f p t là tỷ trọng vốn đầu tư vào cổ phiếu F P T."
        with self.voiceover(text=part1_script_1) as tracker:
            self.update_subtitle("Đặt w_CTG, w_FPT là tỷ trọng đầu tư vào CTG và FPT.", style="default")
            self.sp(Write(ttl, run_time=min(0.5, tracker.duration * 0.3)))
            self.sp(skill_pop_in(weights_card, sound=True, run_time=0.8))
            self.wait(max(0.1, tracker.duration - 1.1))

        part1_script_2 = "Ta sẽ tính được phương sai của danh mục đầu tư theo công thức:"
        with self.voiceover(text=part1_script_2) as tracker:
            self.update_subtitle("Ta tính phương sai danh mục theo công thức:", style="default")
            # 2 khung biến mất và morph ra công thức to rõ giữa màn hình
            self.sp(ReplacementTransform(weights_card, formula), run_time=1.0)
            self.wait(max(0.1, tracker.duration - 1.0))

        # 2. Giả thiết w_CTG = 60%, w_FPT = 40% (Tốc độ chậm, khớp thoại)
        self.sp(FadeOut(formula), run_time=0.4)
        
        # Hiện ảnh money to giữa màn hình
        money_icon = load_icon("icon_money", width=2.2, bg_color=C_WARNING).move_to([0, 0, 0])
        
        alloc_a = MarkupText("60% vào CTG", font=FONT, font_size=24, color=C_PRIMARY, weight=BOLD).move_to([-2.6, -0.4, 0])
        icon_ctg = ImageMobject(os.path.join(os.path.dirname(__file__), "ctg.png")).scale_to_fit_width(0.8).next_to(alloc_a, DOWN, buff=0.3)
        
        alloc_b = MarkupText("40% vào FPT", font=FONT, font_size=24, color=C_SUCCESS, weight=BOLD).move_to([2.6, -0.4, 0])
        icon_fpt = ImageMobject(os.path.join(os.path.dirname(__file__), "fpt.png")).scale_to_fit_width(0.8).next_to(alloc_b, DOWN, buff=0.3)
        
        arrow_a = Arrow(start=[0, 1.4, 0] + LEFT*0.2, end=alloc_a.get_top(), color=C_PRIMARY, stroke_width=4)
        arrow_b = Arrow(start=[0, 1.4, 0] + RIGHT*0.2, end=alloc_b.get_top(), color=C_SUCCESS, stroke_width=4)
        
        calc_step = MarkupText(
            "Var(P) = 0.6² · 45.32 + 0.4² · 54.30 + 2 · 0.6 · 0.4 · (-10.48)",
            font=FONT,
            font_size=18,
            color=C_GRAY
        ).move_to([0, 0, 0])
        if calc_step.width > 8.0:
            calc_step.scale_to_fit_width(8.0)
        
        # Kết quả Var đóng khung to
        calc_res_val = MarkupText("Var(P) = 19.97", font=FONT, font_size=28, color=C_DANGER, weight=BOLD)
        calc_res_box = SurroundingRectangle(calc_res_val, color=C_DANGER, buff=0.4, stroke_width=4, fill_color=C_GRAY, fill_opacity=0.1)
        calc_res = VGroup(calc_res_box, calc_res_val).move_to([0, 0, 0])
 
        part2_script = "Giả sử bạn quyết định đầu tư sáu mươi phần trăm vào C T G và bốn mươi phần trăm cho F P T, khi đó phương sai sẽ bằng mười chín phẩy chín mươi bảy."
        with self.voiceover(text=part2_script) as tracker:
            self.update_subtitle("Với tỷ trọng 60% vào CTG và 40% vào FPT,\nta tính được Var(P) = 19.97.", style="default")
            
            # Hiện money_icon to giữa màn hình
            self.sp(skill_pop_in(money_icon, sound=True), run_time=0.6)
            self.wait(0.2)
            
            # Thu nhỏ đưa lên và rẽ mũi tên đầu tiên (60% vào CTG) cùng logo CTG
            self.sp(money_icon.animate.scale(0.6).move_to([0, 1.8, 0]), run_time=0.6)
            self.sp(FadeIn(alloc_a), Create(arrow_a), FadeIn(icon_ctg), run_time=0.6)
            self.wait(0.8) # Chờ đọc xong "sáu mươi phần trăm vào CTG"
            
            # Rẽ mũi tên thứ hai (40% vào FPT) cùng logo FPT
            self.sp(FadeIn(alloc_b), Create(arrow_b), FadeIn(icon_fpt), run_time=0.6)
            self.wait(1.0) # Đọc xong "bốn mươi phần trăm cho FPT"
            
            # Biến ra công thức thay số ở giữa màn hình
            self.sp(
                ReplacementTransform(VGroup(money_icon, alloc_a, alloc_b, arrow_a, arrow_b), calc_step),
                FadeOut(icon_ctg),
                FadeOut(icon_fpt),
                run_time=0.8
            )
            self.wait(2.2) # Giữ hiển thị công thức thay số lâu một chút
            
            # Biến thành kết quả Var(P) = 17.59 đóng khung
            self.sp(ReplacementTransform(calc_step, calc_res), run_time=0.8)
            self.sp(Wiggle(calc_res), run_time=1.0)
            self.wait(max(0.1, tracker.duration - 8.0))

        # 3. Tính độ lệch chuẩn (Đưa Var(P) lên cao rồi chỉ xuống khung độ lệch chuẩn)
        # Công thức độ lệch chuẩn được to ra và đóng khung
        lbl_sig = MarkupText("σ<sub>P</sub> = ", font=FONT, font_size=24, color=C_WHITE, weight=BOLD)
        var_text = MarkupText("Var(P)", font=FONT, font_size=24, color=C_WHITE)
        sqrt_var = make_sqrt(var_text, color=C_WHITE, stroke_width=2.5)
        equals_sign = MarkupText(" = ", font=FONT, font_size=24, color=C_WHITE, weight=BOLD)
        num_text = MarkupText("19.97", font=FONT, font_size=24, color=C_WHITE)
        sqrt_num = make_sqrt(num_text, color=C_WHITE, stroke_width=2.5)
        
        sd_formula_val = VGroup(lbl_sig, sqrt_var, equals_sign, sqrt_num).arrange(RIGHT, buff=0.1)
        sd_formula_box = SurroundingRectangle(sd_formula_val, color=C_WHITE, buff=0.4, stroke_width=4, fill_color=C_GRAY, fill_opacity=0.1)
        sd_formula = VGroup(sd_formula_box, sd_formula_val).move_to([0, -0.2, 0])
        
        arrow_to_sd = Arrow(start=[0, 1.3, 0], end=[0, 0.4, 0], color=C_WHITE, stroke_width=4)

        part3_script_1 = "Phương sai không phải là một giá trị dễ giải thích, vì vậy hầu hết các nhà phân tích sử dụng độ lệch chuẩn để đo lường rủi ro hiệu quả hơn."
        with self.voiceover(text=part3_script_1) as tracker:
            self.update_subtitle("Các nhà phân tích sử dụng độ lệch chuẩn\nđể đo lường rủi ro dễ hiểu hơn.", style="default")
            
            # Đưa khung Var(P) cao lên
            self.sp(calc_res.animate.scale(0.85).move_to([0, 1.8, 0]), run_time=1.2)
            
            # Chỉ xuống khung tính độ lệch chuẩn
            self.sp(skill_pop_in(sd_formula, sound=True), Create(arrow_to_sd), run_time=1.5)
            self.wait(max(0.1, tracker.duration - 1.6))

        # 4. Morph ra độ lệch chuẩn kết quả cuối cùng (đẩy cao lên)
        sd_res = MarkupText(
            "σ<sub>P</sub> = 4.47%",
            font=FONT,
            font_size=38,
            color=C_SUCCESS,
            weight=BOLD
        ).move_to([0, 0.4, 0])
        
        # Badge rủi ro (đóng khung, hạ thấp xuống - không cần icon ở đầu nữa)
        risk_txt = Text("Mức độ rủi ro danh mục", font=FONT, font_size=18, color=C_WHITE, weight=BOLD)
        risk_box = SurroundingRectangle(risk_txt, color=C_PURPLE, buff=0.3, stroke_width=3, fill_color=C_GRAY, fill_opacity=0.1)
        risk_badge = VGroup(risk_box, risk_txt).move_to([0, -1.4, 0])

        # Mũi tên chỉ xuống to ra chút nữa, màu trắng
        arrow_to_risk = Arrow(start=[0, 0.0, 0], end=risk_badge.get_top() + UP*0.1, color=C_WHITE, stroke_width=6, max_tip_length_to_length_ratio=0.3)

        part3_script_2 = "Vậy độ lệch chuẩn của danh mục đầu tư này sẽ là bốn phẩy ¼ bốn mươi bảy phần trăm, hay còn là thước đo cho Mức độ rủi ro trong danh mục đầu tư."
        # Wait, let's write it cleanly in Vietnamese text: "bốn phẩy bốn mươi bảy phần trăm"
        part3_script_2 = "Vậy độ lệch chuẩn của danh mục đầu tư này sẽ là bốn phẩy bốn mươi bảy phần trăm, hay còn là thước đo cho Mức độ rủi ro trong danh mục đầu tư."
        with self.voiceover(text=part3_script_2) as tracker:
            self.update_subtitle("Độ lệch chuẩn danh mục\ntính được là 4.47%.", style="default")
            
            # Biến đổi mượt mà
            self.sp(
                ReplacementTransform(sd_formula_val, sd_res),
                FadeOut(sd_formula_box),
                FadeOut(arrow_to_sd),
                FadeOut(calc_res),
                run_time=0.8
            )
            self.sp(
                skill_pop_in(risk_badge, sound=True),
                Create(arrow_to_risk),
                run_time=0.6
            )
            self.sp(Wiggle(sd_res), run_time=1.0)
            self.wait(max(0.1, tracker.duration - 2.4))

        self._lift()
        self.clear_content()
