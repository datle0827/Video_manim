"""
scene_s8.py – S8: Tổng kết bài học
"""

from manim import *
from config import FONT, C_SUCCESS, C_PRIMARY, C_WHITE, C_WARNING, C_GRAY, C_PURPLE, C_DANGER, C_DARK_BG, SCRIPTS, SUBS
from helpers import skill_pop_in, load_icon, rnode

class SceneSummaryTopicsMixin:
    def scene_summary_topics(self):
        ttl = self.create_title("Tổng kết bài học")
        
        # Đăng ký trước các Mobjects sử dụng trong Cảnh 8
        cov_word = Text("Covariance", font=FONT, font_size=42, color=C_PRIMARY, weight=BOLD).move_to([0, 0.8, 0])
        underline = Underline(cov_word, color=C_PRIMARY)
        
        # Phiên bản tiếng Việt có gạch chân
        cov_vn_word = Text("Hiệp phương sai", font=FONT, font_size=38, color=C_PRIMARY, weight=BOLD).move_to([0, 0.8, 0])
        underline_vn = Underline(cov_vn_word, color=C_PRIMARY)
        
        visual_data_img = ImageMobject(os.path.join(os.path.dirname(__file__), "asset", "xstk.png")).scale_to_fit_width(4.5).move_to([0, -0.6, 0])
        
        # 3 Đồ thị covariance side-by-side (được thu nhỏ lại và điều chỉnh khoảng cách để tránh tràn màn hình)
        ax_w, ax_h = 2.4, 1.6
        ax1 = Axes(x_range=[0, 5, 1], y_range=[0, 5, 1], x_length=ax_w, y_length=ax_h, axis_config={"stroke_width": 2, "color": C_GRAY}).move_to([-2.6, -0.5, 0])
        ax2 = Axes(x_range=[0, 5, 1], y_range=[0, 5, 1], x_length=ax_w, y_length=ax_h, axis_config={"stroke_width": 2, "color": C_GRAY}).move_to([0, -0.5, 0])
        ax3 = Axes(x_range=[0, 5, 1], y_range=[0, 5, 1], x_length=ax_w, y_length=ax_h, axis_config={"stroke_width": 2, "color": C_GRAY}).move_to([2.6, -0.5, 0])
        
        lbl1 = Text("Cov > 0 (Dương)", font=FONT, font_size=12, color=C_SUCCESS, weight=BOLD).next_to(ax1, UP, buff=0.15)
        lbl2 = Text("Cov = 0 (Bằng 0)", font=FONT, font_size=12, color=C_WARNING, weight=BOLD).next_to(ax2, UP, buff=0.15)
        lbl3 = Text("Cov < 0 (Âm)", font=FONT, font_size=12, color=C_DANGER, weight=BOLD).next_to(ax3, UP, buff=0.15)
        
        line1 = ax1.plot(lambda x: 0.8*x + 1, x_range=[0.5, 4.5], color=C_SUCCESS, stroke_width=3)
        dots2 = VGroup(*[Dot(ax2.c2p(x, y), color=C_WARNING, radius=0.05) for x, y in [(1,2), (2,4), (3,1), (4,3.5), (1.5,1.2), (3.5,4.2), (2.5,2)]])
        line3 = ax3.plot(lambda x: 5 - 0.8*x, x_range=[0.5, 4.5], color=C_DANGER, stroke_width=3)
        
        grp1 = VGroup(ax1, lbl1, line1)
        grp2 = VGroup(ax2, lbl2, dots2)
        grp3 = VGroup(ax3, lbl3, line3)
        
        # Vòng tròn phân bổ nhiều màu sắc (Pie Chart) & Rủi ro
        money_bag = load_icon("icon_process", width=2.2, bg_color=C_WARNING).move_to([0, 0.4, 0])
        
        # Vẽ các cung tròn đầy màu sắc (để mặc định tại 0,0,0 rồi move_to cả nhóm)
        sec1 = Sector(radius=1.3, angle=2*PI/3, start_angle=0, color=C_PRIMARY, fill_opacity=0.85, stroke_color=C_WHITE, stroke_width=1.5)
        sec2 = Sector(radius=1.3, angle=PI/2, start_angle=2*PI/3, color=C_SUCCESS, fill_opacity=0.85, stroke_color=C_WHITE, stroke_width=1.5)
        sec3 = Sector(radius=1.3, angle=5*PI/6, start_angle=7*PI/6, color=C_WARNING, fill_opacity=0.85, stroke_color=C_WHITE, stroke_width=1.5)
        divided_circle = VGroup(sec1, sec2, sec3).move_to([0, 0.4, 0])
        
        # Thêm viền tròn xanh lục làm nổi bật
        green_highlight = Circle(radius=1.4, color=C_SUCCESS, stroke_width=6).move_to([0, 0.4, 0])
        
        # Dấu tích xanh bên cạnh vòng tròn
        checkmark = VMobject(color=C_SUCCESS, stroke_width=6)
        checkmark.set_points_as_corners([[-0.2, -0.1, 0], [0, -0.3, 0], [0.3, 0.1, 0]])
        checkmark.next_to(green_highlight, RIGHT, buff=0.2).shift(UP*0.3)
        
        allocation_grp = VGroup(divided_circle, green_highlight, checkmark)
        
        # Icon rủi ro và mũi tên hướng xuống ở bên cạnh
        risk_box = load_icon("icon_risk", width=1.5, bg_color=C_DANGER)
        down_arrow = Arrow(start=UP*0.5, end=DOWN*0.5, color=C_DANGER, stroke_width=6)
        risk_side_grp = VGroup(risk_box, down_arrow).arrange(RIGHT, buff=0.4).move_to([0, -1.0, 0])

        part1_script_1 = "Qua ví dụ này, chúng ta thấy rằng hiệp phương sai không chỉ là một công cụ thống kê."
        with self.voiceover(text=part1_script_1) as tracker:
            self.update_subtitle("Qua ví dụ này, hiệp phương sai không chỉ\nlà một công cụ thống kê đơn thuần.", style="default")
            self.sp(Write(ttl, run_time=min(0.5, tracker.duration * 0.3)))
            
            # Viết chữ Covariance và gạch chân
            self.sp(Write(cov_word), run_time=0.8)
            self.sp(Create(underline), run_time=0.4)
            self.wait(0.4)
            
            # Xoay/Morph chữ đấy thành chữ "Hiệp phương sai" tiếng Việt
            self.sp(
                ReplacementTransform(cov_word, cov_vn_word),
                ReplacementTransform(underline, underline_vn),
                run_time=0.8
            )
            self.wait(0.6)
            
            # Biến đổi thành hình visual data
            self.sp(
                FadeOut(cov_vn_word),
                FadeOut(underline_vn),
                FadeIn(visual_data_img, scale=0.8),
                run_time=0.8
            )
            self.wait(max(0.1, tracker.duration - 3.4))

        part1_script_2 = "Nó giúp chúng ta đo lường sự biến động cùng nhau giữa các tài sản."
        with self.voiceover(text=part1_script_2) as tracker:
            self.update_subtitle("Nó giúp đo lường sự biến động\ncùng nhau giữa các tài sản.", style="default")
            
            self.sp(FadeOut(visual_data_img), run_time=0.4)
            
            # Vẽ lần lượt 3 đồ thị biểu diễn
            self.sp(Create(ax1), Write(lbl1), Create(line1), run_time=0.8)
            self.wait(0.3)
            self.sp(Create(ax2), Write(lbl2), FadeIn(dots2, scale=0.5), run_time=0.8)
            self.wait(0.3)
            self.sp(Create(ax3), Write(lbl3), Create(line3), run_time=0.8)
            self.wait(max(0.1, tracker.duration - 3.4))

        part1_script_3 = "Nhờ đó, nhà đầu tư có thể đưa ra quyết định phân bổ vốn hợp lý và giảm thiểu rủi ro cho danh mục."
        with self.voiceover(text=part1_script_3) as tracker:
            self.update_subtitle("Nhờ đó, nhà đầu tư phân bổ vốn hợp lý\nvà giảm thiểu rủi ro danh mục.", style="default")
            
            # Ẩn 3 đồ thị, hiện túi tiền rồi biến thành vòng tròn nhiều màu sắc, tích xanh, đẩy lên và chỉ rủi ro
            self.sp(FadeOut(grp1), FadeOut(grp2), FadeOut(grp3), run_time=0.5)
            self.sp(skill_pop_in(money_bag, sound=True), run_time=0.6)
            self.wait(0.4)
            self.sp(ReplacementTransform(money_bag, divided_circle), run_time=0.8)
            self.wait(0.2)
            self.sp(Create(green_highlight), run_time=0.4)
            self.wait(0.2)
            self.sp(Create(checkmark), run_time=0.6)
            self.wait(0.4)
            self.sp(
                allocation_grp.animate.scale(0.7).move_to([0, 1.5, 0]),
                skill_pop_in(risk_box, sound=True),
                Create(down_arrow),
                run_time=0.8
            )
            self.wait(max(0.1, tracker.duration - 4.3))
            
        # 3 Khái niệm chính (cho to ra và cách nhau tí)
        # i1 dùng icon_covariate (covariate-svgrepo-com.svg)
        i1 = load_icon("icon_covariate", width=0.8, bg_color=C_PRIMARY)
        k1_grp = VGroup(i1, rnode("Hiệp phương sai (Covariance)", C_PRIMARY, w=5.2, fs=20, bold=True)).arrange(RIGHT, buff=0.3)
        
        # i2 dùng icon_database (database-svgrepo-com.svg)
        i2 = load_icon("icon_database", width=0.8, bg_color=C_WARNING)
        k2_grp = VGroup(i2, rnode("Phương sai danh mục đầu tư", C_WARNING, w=5.2, fs=20, bold=True)).arrange(RIGHT, buff=0.3)
        
        # i3 dùng icon_books (books-svgrepo-com.svg)
        i3 = load_icon("icon_books", width=0.8, bg_color=C_SUCCESS)
        k3_grp = VGroup(i3, rnode("Đa dạng hóa & Lý thuyết Markowitz", C_SUCCESS, w=5.2, fs=18, bold=True)).arrange(RIGHT, buff=0.3)
        
        # Thiết lập vị trí ban đầu cho hiệu ứng cuộn đẩy lên
        k1_grp.move_to([0, -0.3, 0])
        k2_grp.move_to([0, -0.3, 0])
        k3_grp.move_to([0, -0.3, 0])

        part2_script_1 = "Trong video này mình đề cập tới ba khái niệm quan trọng"
        with self.voiceover(text=part2_script_1) as tracker:
            self.update_subtitle("Video này đề cập đến 3 khái niệm quan trọng", style="default")
            self.sp(
                FadeOut(allocation_grp),
                FadeOut(risk_box),
                FadeOut(down_arrow),
                run_time=0.6
            )
            self.wait(max(0.1, tracker.duration - 0.6))

        part2_script_2 = "Hiệp phương sai, Phương sai danh mục đầu tư, Đa dạng hóa đầu tư và Lý thuyết Markowitz."
        with self.voiceover(text=part2_script_2) as tracker:
            self.update_subtitle("Hiệp phương sai, Phương sai danh mục,\nvà Đa dạng hóa đầu tư.", style="default")
            
            # 1. Hiện Hiệp phương sai ở giữa
            self.sp(skill_pop_in(k1_grp, sound=True), run_time=0.6)
            self.wait(0.8)
            
            # 2. Đẩy Hiệp phương sai lên và hiện Phương sai danh mục
            self.sp(
                k1_grp.animate.move_to([0, 1.3, 0]),
                skill_pop_in(k2_grp, sound=True),
                run_time=0.8
            )
            self.wait(0.8)
            
            # 3. Đẩy cả hai lên và hiện Đa dạng hóa (cách nhau khoảng rộng rãi hơn)
            self.sp(
                k1_grp.animate.move_to([0, 2.6, 0]),
                k2_grp.animate.move_to([0, 1.3, 0]),
                skill_pop_in(k3_grp, sound=True),
                run_time=0.8
            )
            self.wait(max(0.1, tracker.duration - 3.8))

        self._lift()
        self.clear_content()
