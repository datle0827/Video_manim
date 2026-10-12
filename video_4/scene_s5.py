"""
scene_s5.py – S5: Phương pháp 1: IQR
"""

from manim import *
from config import FONT, C_PRIMARY, C_SUCCESS, C_WARNING, C_GRAY, C_WHITE, C_DANGER, FAMI_BLUE, FAMI_CYAN
from helpers import skill_pop_in

def get_math_design(tex, fallback_markup, font_size=24, color=WHITE):
    try:
        return MathTex(tex, font_size=font_size, color=color)
    except Exception:
        return MarkupText(fallback_markup, font=FONT, font_size=font_size - 4, color=color)

class SceneS5Mixin:
    def scene_s5(self):
        ttl = self.create_title("Quy tắc 1.5 IQR")

        # 1. IQR morph text
        iqr_txt = Text("IQR", font=FONT, font_size=64, color=FAMI_CYAN, weight=BOLD).move_to([0, 0.4, 0])

        # 2. Central box coordinates
        box = Rectangle(
            width=3.2, height=2.4,
            stroke_color=FAMI_BLUE, stroke_width=4,
            fill_color=C_WHITE, fill_opacity=0.0
        ).move_to([0, 0.4, 0])

        median_line = Line(
            start=[0, -0.8, 0], end=[0, 1.6, 0],
            color=FAMI_BLUE, stroke_width=4
        )

        # Labels for Q1, Median, Q3
        q1_lbl = Text("Q1", font=FONT, font_size=16, color=FAMI_BLUE).move_to([-1.6, -1.2, 0])
        median_lbl = Text("Median", font=FONT, font_size=16, color=FAMI_BLUE).move_to([0, -1.2, 0])
        q3_lbl = Text("Q3", font=FONT, font_size=16, color=FAMI_BLUE).move_to([1.6, -1.2, 0])

        # Double bracket above Q1-Q3
        br_left = Line(start=[-1.6, 1.9, 0], end=[-1.6, 2.1, 0], color=FAMI_BLUE, stroke_width=2)
        br_top = Line(start=[-1.6, 2.1, 0], end=[1.6, 2.1, 0], color=FAMI_BLUE, stroke_width=2)
        br_right = Line(start=[1.6, 2.1, 0], end=[1.6, 1.9, 0], color=FAMI_BLUE, stroke_width=2)
        br_mid = Line(start=[0, 2.1, 0], end=[0, 2.7, 0], color=FAMI_BLUE, stroke_width=2)
        br_arr_l = Arrow(start=[-1.6, 2.0, 0], end=[-1.6, 1.7, 0], color=FAMI_BLUE, max_tip_length_to_length_ratio=0.3, stroke_width=2)
        br_arr_r = Arrow(start=[1.6, 2.0, 0], end=[1.6, 1.7, 0], color=FAMI_BLUE, max_tip_length_to_length_ratio=0.3, stroke_width=2)
        bracket_lbl = Text("Interquartile range (IQR)", font=FONT, font_size=17, color=FAMI_BLUE, weight=BOLD).next_to(br_mid, UP, buff=0.1)
        bracket_grp = VGroup(br_left, br_top, br_right, br_mid, br_arr_l, br_arr_r, bracket_lbl)

        # Whiskers
        left_whisker = Line(start=[-1.6, 0.4, 0], end=[-3.6, 0.4, 0], color=FAMI_BLUE, stroke_width=4)
        right_whisker = Line(start=[1.6, 0.4, 0], end=[3.6, 0.4, 0], color=FAMI_BLUE, stroke_width=4)

        # Fences
        lower_fence = Line(start=[-3.6, -0.1, 0], end=[-3.6, 0.9, 0], color=FAMI_BLUE, stroke_width=4)
        upper_fence = Line(start=[3.6, -0.1, 0], end=[3.6, 0.9, 0], color=FAMI_BLUE, stroke_width=4)

        # Fence Labels and Arrows (pointing up to fences)
        lbl_lf = Text("Lower fence", font=FONT, font_size=14, color=FAMI_BLUE).move_to([-3.6, -1.4, 0])
        arr_lf = Arrow(start=[-3.6, -1.1, 0], end=[-3.6, -0.2, 0], color=FAMI_BLUE, max_tip_length_to_length_ratio=0.3, stroke_width=3)
        lbl_uf = Text("Upper fence", font=FONT, font_size=14, color=FAMI_BLUE).move_to([3.6, -1.4, 0])
        arr_uf = Arrow(start=[3.6, -1.1, 0], end=[3.6, -0.2, 0], color=FAMI_BLUE, max_tip_length_to_length_ratio=0.3, stroke_width=3)

        # Outliers (Dots + Arrows pointing down + Outliers Label)
        outliers_l = VGroup(
            Dot(point=[-4.1, 0.4, 0], color=FAMI_CYAN, radius=0.12),
            Dot(point=[-4.5, 0.4, 0], color=FAMI_CYAN, radius=0.12)
        )
        lbl_out_l = Text("Outliers", font=FONT, font_size=14, color=FAMI_BLUE).move_to([-4.3, 1.4, 0])
        arr_out_l = Arrow(start=[-4.3, 1.2, 0], end=[-4.3, 0.6, 0], color=FAMI_BLUE, max_tip_length_to_length_ratio=0.3, stroke_width=3)
        outliers_l_grp = VGroup(outliers_l, lbl_out_l, arr_out_l)

        outliers_r = VGroup(
            Dot(point=[4.1, 0.4, 0], color=FAMI_CYAN, radius=0.12),
            Dot(point=[4.5, 0.4, 0], color=FAMI_CYAN, radius=0.12)
        )
        lbl_out_r = Text("Outliers", font=FONT, font_size=14, color=FAMI_BLUE).move_to([4.3, 1.4, 0])
        arr_out_r = Arrow(start=[4.3, 1.2, 0], end=[4.3, 0.6, 0], color=FAMI_BLUE, max_tip_length_to_length_ratio=0.3, stroke_width=3)
        outliers_r_grp = VGroup(outliers_r, lbl_out_r, arr_out_r)

        # Group and scale down the diagram components to 80% to avoid overflow
        diagram_grp = VGroup(
            box, median_line, q1_lbl, median_lbl, q3_lbl,
            bracket_grp, left_whisker, right_whisker, lower_fence, upper_fence,
            lbl_lf, arr_lf, lbl_uf, arr_uf,
            outliers_l_grp, outliers_r_grp
        )
        diagram_grp.scale(0.8).move_to([0, 0.6, 0])

        # Bottom explanations
        desc_part2 = get_math_design(
            r"\text{IQR} = Q3 - Q1 \quad (\text{Chứa 50\% dữ liệu trung tâm})",
            r"IQR = Q3 - Q1 (Chứa 50% dữ liệu trung tâm)",
            font_size=28, color=FAMI_CYAN
        ).move_to([0, -2.6, 0])
        
        desc_part3 = get_math_design(
            r"\text{Outlier} < Q1 - 1.5\text{IQR} \quad \text{hoặc} \quad \text{Outlier} > Q3 + 1.5\text{IQR}",
            r"Outlier nằm ngoài: [Q1 - 1.5×IQR; Q3 + 1.5×IQR]",
            font_size=32, color=C_WHITE
        ).move_to([0, -2.6, 0])

        # Framed Question Card (centered and snugly fits the text)
        line1 = Text("Điểm dữ liệu này có bất thường", font=FONT, font_size=18, color=C_WHITE, weight=BOLD, t2c={"bất thường": C_WARNING})
        line2 = Text("so với phần lớn dữ liệu hay không?", font=FONT, font_size=18, color=C_WHITE, weight=BOLD)
        question_txt = VGroup(line1, line2).arrange(DOWN, buff=0.15).move_to([0, -0.4, 0])
        
        question_box = RoundedRectangle(
            width=question_txt.width + 0.8, height=question_txt.height + 0.6, corner_radius=0.15,
            color=FAMI_CYAN, fill_color="#0f172a", fill_opacity=0.9, stroke_width=4
        ).move_to(question_txt.get_center())
        question_card = VGroup(question_box, question_txt)

        # --- ANIMATIONS ---

        # 1. Morph text "IQR" to Central Box
        part1_script = "Đầu tiên, chúng ta có thể sử dụng khoảng tứ phân vị IQR để phát hiện những giá trị bất thường, trong phân bố dữ liệu."
        with self.voiceover(text=part1_script) as tracker:
            self.update_subtitle("Chúng ta có thể sử dụng \n khoảng tứ phân vị IQR", style="default")
            self.sp(Write(ttl, run_time=1))
            self.sp(Write(iqr_txt), run_time=1)
            self.wait(0.5)
            
            self.update_subtitle("để phát hiện bất thường \ntrong phân bố dữ liệu.", style="default")
            self.sp(
                ReplacementTransform(iqr_txt, box),
                Create(median_line),
                Write(q1_lbl), Write(median_lbl), Write(q3_lbl),
                run_time=1.2
            )
            self.wait(max(0.1, tracker.duration - 2.8))
 
        # 2. IQR calculation & bracket
        part2_script = "Khoảng tứ phân vị IQR được tính bằng hiệu giữa tứ phân vị thứ ba và thứ nhất."
        with self.voiceover(text=part2_script) as tracker:
            self.update_subtitle("Khoảng tứ phân vị IQR được tính bằng hiệu giữa", style="default")
            self.sp(Create(bracket_grp), run_time=0.8)
            self.wait(0.5)
            
            self.update_subtitle("tứ phân vị thứ ba và thứ nhất.", style="default")
            self.sp(Write(desc_part2), run_time=0.8)
            self.wait(max(0.1, tracker.duration - 2.3))
 
        # 3. Whiskers, Fences, Outliers & Explanations
        part3_script = "Một điểm được xem là Outlier nếu nhỏ hơn Q 1 trừ một phẩy năm IQR, hoặc lớn hơn Q 3 cộng một phẩy năm IQR."
        with self.voiceover(text=part3_script) as tracker:
            self.update_subtitle("Một điểm được xem là Outlier \n nếu nhỏ hơn Q1 - 1.5IQR", style="default")
            
            # Show whiskers and fences
            self.sp(
                Create(left_whisker), Create(right_whisker),
                Create(lower_fence), Create(upper_fence),
                run_time=1.2
            )
            self.sp(
                Create(arr_lf), Write(lbl_lf),
                Create(arr_uf), Write(lbl_uf),
                run_time=1.2
            )
            
            self.update_subtitle("hoặc lớn hơn Q3 + 1.5IQR.", style="default")
            # Pop in the outliers
            self.sp(
                skill_pop_in(outliers_l_grp, sound=True),
                skill_pop_in(outliers_r_grp, sound=True),
                run_time=1.0
            )
            
            # Change bottom explanation formula
            self.sp(
                ReplacementTransform(desc_part2, desc_part3),
                run_time=0.8
            )
            self.wait(max(0.1, tracker.duration - 3.7))
 
        # 4. Morph everything to framed core question card (keeping the title visible)
        part4_script = "IQR giúp chúng ta trả lời câu hỏi: điểm này có bất thường so với phần lớn dữ liệu hay không?"
        with self.voiceover(text=part4_script) as tracker:
            self.update_subtitle("IQR trả lời câu hỏi: điểm này \n có bất thường so với đa số hay không", style="default")
            
            # Morph the diagram and bottom explanation into the centered framed card
            all_diagram_elements = VGroup(diagram_grp, desc_part3)
            self.sp(
                ReplacementTransform(all_diagram_elements, question_card),
                run_time=1.2
            )
            self.sp(Wiggle(question_card), run_time=0.8)
            self.wait(max(0.1, tracker.duration - 2.2))

        self._lift()
        self.clear_content()
