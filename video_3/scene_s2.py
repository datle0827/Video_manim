"""
scene_s2.py – S2: Giả thuyết bài toán
"""

from manim import *
from config import (
    FONT, C_WARNING, C_PURPLE, C_SUCCESS, C_GRAY, C_WHITE, C_DANGER, C_PRIMARY,
    SCRIPTS, SUBS
)
from helpers import skill_pop_in, sec_title, rnode, load_icon

class SceneProblemMixin:
    def scene_problem(self):
        ttl = self.create_title("Mô tả bài toán")

        # 1. Businessman icon (custom_icon) in center first
        businessman_icon = SVGMobject(os.path.join(os.path.dirname(__file__), "asset", "undraw_bull-market_4a8e.svg")).scale_to_fit_width(3.6).move_to([0, 1.0, 0])
        
        # Badge số vốn 100M
        mb_icon = load_icon("icon_process", width=0.6, bg_color=C_WARNING)
        capital_txt = Text("Vốn đầu tư: 100 Triệu VNĐ", font=FONT, font_size=21, color=C_WHITE, weight=BOLD)
        capital_badge = VGroup(mb_icon, capital_txt).arrange(RIGHT, buff=0.3).move_to([0, -0.8, 0])

        part1_script_1 = "Giả sử bạn là một nhà đầu tư tham gia vào thị trường chứng khoán"
        with self.voiceover(text=part1_script_1) as tracker:
            self.update_subtitle("Giả sử bạn là một nhà đầu tư", style="default")
            self.sp(Write(ttl, run_time=min(0.5, tracker.duration * 0.3)))
            self.sp(skill_pop_in(businessman_icon, sound=True, run_time=0.6))
            self.wait(max(0.1, tracker.duration - 1.1))

        part1_script_2 = "và đang có một trăm triệu đồng."
        with self.voiceover(text=part1_script_2) as tracker:
            self.update_subtitle("và hiện đang có số vốn 100 triệu đồng.", style="default")
            # Zoom to capital (make it big in center) and shrink the businessman icon
            self.sp(
                businessman_icon.animate.scale(0.6).move_to([0, 1.8, 0]),
                capital_badge.animate.scale(1.4).move_to([0, 0.2, 0]),
                run_time=0.8
            )
            self.wait(max(0.1, tracker.duration - 0.8))
            
            # Sau khi nói xong chỗ có 100 triệu thì ảnh đấy biến mất
            self.sp(FadeOut(businessman_icon), FadeOut(capital_badge), run_time=0.5)

        # 2. Vẽ biểu đồ chứng khoán và chỉ 2 hướng vào cổ phiếu CTG và FPT (không đè nhau)
        ax = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=4.0,
            y_length=2.2,
            axis_config={"color": C_GRAY},
        ).move_to([0, 1.4, 0])
        
        graph = ax.plot(lambda x: 0.8 + 0.6*x + 0.3*np.sin(x*4), color=C_SUCCESS, x_range=[0, 3.8])
        chart_grp = VGroup(ax, graph)

        icon_a = ImageMobject(os.path.join(os.path.dirname(__file__), "ctg.png")).scale_to_fit_width(0.8)
        label_a = MarkupText("Cổ phiếu CTG", font=FONT, font_size=20, color=C_WHITE, weight=BOLD)
        stock_a = Group(icon_a, label_a).arrange(RIGHT, buff=0.2).move_to([-1.8, -1.0, 0])
        
        icon_b = ImageMobject(os.path.join(os.path.dirname(__file__), "fpt.png")).scale_to_fit_width(0.8)
        label_b = MarkupText("Cổ phiếu FPT", font=FONT, font_size=20, color=C_WHITE, weight=BOLD)
        stock_b = Group(icon_b, label_b).arrange(RIGHT, buff=0.2).move_to([1.8, -1.0, 0])

        arrow_to_a = Arrow(start=[0, 0.4, 0] + LEFT*0.3, end=stock_a.get_top(), color=C_PRIMARY, stroke_width=4)
        arrow_to_b = Arrow(start=[0, 0.4, 0] + RIGHT*0.3, end=stock_b.get_top(), color=C_SUCCESS, stroke_width=4)

        part2_script = SCRIPTS["s2"].split(". ")[1] # Sau khi phân tích thị trường, bạn tìm được hai cổ phiếu tiềm năng là CTG và FPT.
        with self.voiceover(text=part2_script) as tracker:
            self.update_subtitle("Sau phân tích, bạn tìm được hai cổ phiếu\ntiềm năng là CTG và FPT.", style="default")
            
            # Vẽ biểu đồ
            self.sp(Create(ax), run_time=0.4)
            self.sp(Create(graph), run_time=0.4)
            
            # Lần lượt hiện cổ phiếu CTG và FPT và chỉ hướng
            self.sp(FadeIn(stock_a), Create(arrow_to_a), run_time=0.6)
            self.sp(FadeIn(stock_b), Create(arrow_to_b), run_time=0.6)
            self.wait(max(0.1, tracker.duration - 2.0))

        self._lift()
        self.clear_content()
