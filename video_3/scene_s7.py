"""
scene_s7.py – S7: Đa dạng hóa đầu tư
"""

from manim import *
from config import FONT, C_SUCCESS, C_PRIMARY, C_WHITE, C_WARNING, C_GRAY, C_DANGER, C_PURPLE, SCRIPTS, SUBS
from helpers import skill_pop_in, load_icon

class SceneKeywordsMixin:
    def scene_keywords(self):
        ttl = self.create_title("Đa dạng hóa đầu tư")

        # PA1: 100% Cổ phiếu CTG (phóng to ra chút cho dễ nhìn, căn chỉnh chính xác trục dọc)
        icon1 = ImageMobject(os.path.join(os.path.dirname(__file__), "ctg.png")).scale_to_fit_width(0.85).move_to([-2.0, 1.6, 0])
        pa1_lbl = MarkupText("PA 1: Đầu tư 100% CTG", font=FONT, font_size=20, color=C_PRIMARY)
        pa1_ret = Text("L.Nhuận: 5.39%", font=FONT, font_size=20, color=C_WHITE)
        pa1_risk = Text("Rủi ro: 6.73%", font=FONT, font_size=20, color=C_DANGER)
        pa1_texts = VGroup(pa1_lbl, pa1_ret, pa1_risk).arrange(DOWN, buff=0.3).move_to([-2.0, -0.4, 0])
        pa1_grp = Group(icon1, pa1_texts)

        # PA2: Danh mục tối ưu 60/40 (với 2 hình ảnh CTG và FPT cạnh nhau, phóng to ra và căn chỉnh chính xác trục dọc)
        icon_ctg_pa2 = ImageMobject(os.path.join(os.path.dirname(__file__), "ctg.png")).scale_to_fit_width(0.6)
        icon_fpt_pa2 = ImageMobject(os.path.join(os.path.dirname(__file__), "fpt.png")).scale_to_fit_width(0.6)
        icon2 = Group(icon_ctg_pa2, icon_fpt_pa2).arrange(RIGHT, buff=0.15).move_to([2.0, 1.6, 0])
        
        pa2_lbl = Text("PA 2: Danh mục 60/40", font=FONT, font_size=20, color=C_SUCCESS)
        pa2_ret = Text("L.Nhuận: 3.59%", font=FONT, font_size=20, color=C_WHITE)
        pa2_risk = Text("Rủi ro: 4.47%", font=FONT, font_size=20, color=C_SUCCESS)
        pa2_texts = VGroup(pa2_lbl, pa2_ret, pa2_risk).arrange(DOWN, buff=0.3).move_to([2.0, -0.4, 0])
        pa2_grp = Group(icon2, pa2_texts)

        part1_script = "Ta có thể thấy bằng cách kết hợp C T G và F P T theo tỷ trọng phù hợp, nhà đầu tư có thể giảm rủi ro mà vẫn duy trì mức lợi nhuận hấp dẫn."
        with self.voiceover(text=part1_script) as tracker:
            self.update_subtitle("Bằng cách kết hợp CTG và FPT hợp lý,\nta giảm rủi ro nhưng vẫn giữ lợi nhuận tốt.", style="default")
            self.sp(Write(ttl, run_time=min(0.5, tracker.duration * 0.3)))
            
            # Show PA 1 with 3D Flip
            self.sp(Rotate(pa1_grp, angle=2*PI, axis=UP, run_time=0.8))
            self.wait(0.2)
            # Show PA 2 with 3D Flip
            self.sp(Rotate(pa2_grp, angle=2*PI, axis=UP, run_time=0.8))
            self.wait(max(0.1, tracker.duration - 2.1))

        # Khung viền xanh làm nổi bật PA 2 làm phương án tối ưu
        opt_rect = RoundedRectangle(
            corner_radius=0.25,
            width=3.6,
            height=3.4,
            color=C_SUCCESS,
            stroke_width=4
        ).move_to([2.0, 0.4, 0])

        # # Using new scale balance SVG for shield icon to center it
        # shield_icon = load_icon("icon_scales", width=1.5, bg_color=C_SUCCESS).move_to([0, 0.4, 0])
        # shield_lbl = Text("Tối ưu hóa & Đa dạng hóa rủi ro", font=FONT, font_size=28, color=C_SUCCESS, weight=BOLD).next_to(shield_icon, DOWN, buff=0.3)
        # shield_grp = VGroup(shield_icon, shield_lbl)

        part2_script_1 = "Đây chính là cách áp dụng xác suất thống kê trong đầu tư tài chính"
        with self.voiceover(text=part2_script_1) as tracker:
            self.update_subtitle("Đây chính là cách áp dụng xác suất thống kê", style="default")
            self.sp(Create(opt_rect), run_time=0.5)
            self.sp(Flash(opt_rect, color=C_SUCCESS))
            # Virtual Zoom-in to PA2 card and Zoom-out PA1 card
            self.sp(
                Group(pa2_grp, opt_rect).animate.scale(1.1).move_to([1.8, 0.4, 0]),
                pa1_grp.animate.scale(0.8).move_to([-2.2, 0.4, 0]),
                run_time=0.5    
            )
            self.wait(max(0.1, tracker.duration - 1.2))
            self.sp(
                FadeOut(pa1_grp),
                FadeOut(opt_rect),
                FadeOut(pa2_grp),
                run_time=0.8
            )

        # part2_script_2 = "mà hiện nay hầu hết các quỹ đầu tư chuyên nghiệp vẫn đang sử dụng để tìm kiếm sự kết hợp tối ưu giữa nhiều tài sản."
        # with self.voiceover(text=part2_script_2) as tracker:
        #     self.update_subtitle("Hầu hết các quỹ chuyên nghiệp dùng \nđể tìm sự kết hợp tối ưu.", style="default")
        #     # Morph PA1 and PA2 into the Balance shield group at the center
        #     self.sp(
        #         FadeOut(pa1_grp),
        #         FadeOut(opt_rect),
        #         FadeOut(pa2_grp),
        #         FadeIn(shield_grp),
        #         run_time=0.8
        #     )
        #     # 3D Flip of the newly morphed shield_grp
        #     self.sp(Rotate(shield_grp, angle=2*PI, axis=UP, run_time=0.8))
        #     self.wait(max(0.1, tracker.duration - 1.6))

        # ─── PHẦN MỚI 1: BIỂU ĐỒ ĐƯỜNG BIÊN HIỆU QUẢ (EFFICIENT FRONTIER) ───
        ax = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 10, 2],
            x_length=6.0,
            y_length=4.0,
            axis_config={"color": C_GRAY},
            tips=False
        ).move_to([0.8, -0.2, 0]) # Dịch đồ thị sang phải
        
        # Nhãn của các trục tọa độ
        x_lbl = Text("Rủi ro", font=FONT, font_size=15, color=C_WHITE).next_to(ax.x_axis.get_end(), DOWN+LEFT, buff=0.15)
        y_lbl = Text("Lợi nhuận", font=FONT, font_size=15, color=C_WHITE).next_to(ax.y_axis.get_end(), UP+LEFT, buff=0.15)
        
        # Đường cong phân bổ danh mục (C-Shape Curve) xoay trục
        # u đại diện cho mức Rủi ro (trục đứng) chạy từ 1.5 đến 8.5
        # Phương trình: x = 2.0 + 0.15 * (u - 3.0)^2
        curve_func = lambda u: ax.c2p(2.0 + 0.15 * (u - 3.0)**2, u, 0)
        
        # Nhánh kém hiệu quả (Inefficient Frontier) màu xám: u chạy từ 1.5 đến 3.0
        inefficient_curve = ParametricFunction(
            curve_func,
            t_range=[1.5, 3.0],
            color=C_GRAY,
            stroke_width=4
        )
        
        # Nhánh hiệu quả (Efficient Frontier) màu xanh: u chạy từ 3.0 đến 8.5
        efficient_curve = ParametricFunction(
            curve_func,
            t_range=[3.0, 8.5],
            color=C_SUCCESS,
            stroke_width=4
        )
        
        # Đám mây các điểm chấm biểu diễn các tỷ lệ phân bổ vốn khác nhau trên đường biên
        dots = VGroup()
        for u_val in [2.2, 4.0, 5.0, 6.0, 7.0, 8.0]:
            dot = Dot(curve_func(u_val), color=C_WHITE, radius=0.06, fill_opacity=0.8)
            dots.add(dot)
            
        # Các điểm quan trọng trên đồ thị
        # 1. 100% Asset A tại u = 1.5
        dot_a = Dot(curve_func(1.5), color=C_WHITE, radius=0.09)
        
        # 2. 100% Asset B tại u = 8.5
        dot_b = Dot(curve_func(8.5), color=C_WHITE, radius=0.09)
        
        # 3. Danh mục rủi ro tối thiểu (Minimum Variance Portfolio) tại u = 3.0
        dot_min = Dot(curve_func(3.0), color=C_WHITE, radius=0.09)
        lbl_min = MarkupText("Rủi ro tối thiểu", font=FONT, font_size=13, color=C_WHITE).next_to(dot_min, RIGHT, buff=0.15)
        
        frontier_points = VGroup(dot_b, dot_a, dot_min, lbl_min)
        
        # Nhãn của đường biên hiệu quả được đưa hẳn sang bên phải của đồ thị để tránh đè chữ
        lbl_frontier = MarkupText("Đường biên hiệu quả", font=FONT, font_size=15, color=C_SUCCESS, weight=BOLD).next_to(dot_b, RIGHT, buff=0.2)

        part3_script_1 = "Bằng cách tính toán nhiều cách phân bổ vốn khác nhau, khi đưa các tổ hợp này lên một biểu đồ, mô hình Markowitz sẽ giúp bạn thấy được một đường biên hiệu quả."
        with self.voiceover(text=part3_script_1) as tracker:
            self.update_subtitle(
                "Bằng cách tính toán nhiều cách phân bổ vốn, mô\n"
                "hình Markowitz sẽ chỉ ra một đường biên hiệu quả.", 
                style="default"
            )
            # Ẩn cái cân, hiện hệ trục tọa độ và tên trục
            # self.sp(FadeOut(shield_grp), run_time=0.5)
            self.sp(Create(ax), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.8)
            
            # Hiện đường cong và các điểm chấm phân bổ
            self.sp(
                Create(efficient_curve),
                Create(inefficient_curve),
                FadeIn(dots, lag_ratio=0.05),
                run_time=1.5
            )
            self.sp(FadeIn(frontier_points), run_time=0.8)
            self.wait(max(0.1, tracker.duration - 3.6))
            
        part3_script_2 = "Đây là tập hợp những danh mục đầu tư đáng tiền nhất."
        with self.voiceover(text=part3_script_2) as tracker:
            self.update_subtitle(
                "Đây là tập hợp những danh mục \n đầu tư \"đáng tiền\" nhất.",
                style="default"
            )
            self.sp(skill_pop_in(lbl_frontier, sound=True), run_time=0.6)
            self.wait(max(0.1, tracker.duration - 0.6))
            
        part3_script_3 = "Từ đó, bạn có thể chọn ra cho mình một danh mục đầu tư phù hợp."
        with self.voiceover(text=part3_script_3) as tracker:
            self.update_subtitle(
                "Từ đó, bạn có thể chọn ra cho mình\n"
                "một danh mục đầu tư phù hợp.",
                style="default"
            )
            self.wait(max(0.1, tracker.duration))

        part3_script_4 = "Tối ưu lợi nhuận, hay tối thiểu rủi ro."
        with self.voiceover(text=part3_script_4) as tracker:
            self.update_subtitle(
                "Tối ưu lợi nhuận, hay tối thiểu rủi ro.",
                style="default"
            )
            # Trục lợi nhuận sáng lên (Y-axis label "Lợi nhuận" + Y-axis line)
            self.sp(
                Indicate(y_lbl, color=C_SUCCESS, scale_factor=1.3),
                Indicate(ax.y_axis, color=C_SUCCESS),
                run_time=1.5
            )
            # Trục rủi ro sáng lên (X-axis label "Rủi ro" + X-axis line)
            self.sp(
                Indicate(x_lbl, color=C_DANGER, scale_factor=1.3),
                Indicate(ax.x_axis, color=C_DANGER),
                run_time=1.5
            )
            self.wait(max(0.1, tracker.duration - 2.0))
        
        # ─── PHẦN MỚI 2: PHẦN MỞ RỘNG CÔNG THỨC NHIỀU TÀI SẢN (MATRIX FORMULA) ───
        # Tạo helper vẽ dấu ngoặc vuông ma trận thủ công để tránh lỗi latex
        def draw_bracket(height, is_left=True, width=0.15, stroke_width=2.5, color=WHITE):
            h = height / 2
            w = width if is_left else -width
            points = [
                [w, h, 0],
                [0, h, 0],
                [0, -h, 0],
                [w, -h, 0]
            ]
            bracket = VMobject(color=color, stroke_width=stroke_width)
            bracket.set_points_as_corners(points)
            bracket.set_fill(opacity=0)
            return bracket

        # Tạo các helper vẽ dấu ba chấm bằng Dot để tránh lỗi hiển thị font trên các hệ điều hành khác nhau
        def create_vertical_dots(color=WHITE, buff=0.08):
            d1 = Dot(radius=0.03, color=color)
            d2 = Dot(radius=0.03, color=color).next_to(d1, DOWN, buff=buff)
            d3 = Dot(radius=0.03, color=color).next_to(d2, DOWN, buff=buff)
            return VGroup(d1, d2, d3)

        def create_horizontal_dots(color=WHITE, buff=0.08):
            d1 = Dot(radius=0.03, color=color)
            d2 = Dot(radius=0.03, color=color).next_to(d1, RIGHT, buff=buff)
            d3 = Dot(radius=0.03, color=color).next_to(d2, RIGHT, buff=buff)
            return VGroup(d1, d2, d3)

        def create_diagonal_dots(color=WHITE, buff=0.08):
            d1 = Dot(radius=0.03, color=color)
            d2 = Dot(radius=0.03, color=color).move_to(d1.get_center() + DOWN*buff + RIGHT*buff)
            d3 = Dot(radius=0.03, color=color).move_to(d2.get_center() + DOWN*buff + RIGHT*buff)
            return VGroup(d1, d2, d3)

        # Tạo tiêu đề Mở rộng
        exp_title = self.create_title("Mở rộng")
        
        # Công thức ma trận ban đầu đóng khung
        formula_latex = MarkupText("σ<sub>p</sub><sup>2</sup> = w<sup>T</sup> Σ w", font=FONT, font_size=38, color=C_WHITE, weight=BOLD)
        formula_box = SurroundingRectangle(formula_latex, color=C_WARNING, buff=0.4, stroke_width=3)
        formula_grp = VGroup(formula_box, formula_latex).move_to([0, 0, 0])
        
        # 1. Khối Vector trọng số w (Sử dụng MarkupText để tránh lỗi tofu) đại diện n tài sản
        # w_title = MarkupText("<b>w</b> (Vector trọng số):", font=FONT, font_size=20, color=C_PRIMARY)
        w_desc = Text("Tỷ lệ phân bổ vốn vào các tài sản", font=FONT, font_size=24, color=C_WHITE)
        w_cond = MarkupText("w<sub>1</sub> + w<sub>2</sub> + ... + w<sub>n</sub> = 1", font=FONT, font_size=24, color=C_PRIMARY)
        
        w1 = MarkupText("w<sub>1</sub>", font=FONT, font_size=24, color=C_WHITE)
        w2 = MarkupText("w<sub>2</sub>", font=FONT, font_size=24, color=C_WHITE)
        w_dots = create_vertical_dots(C_WHITE, buff=0.08)
        wn = MarkupText("w<sub>n</sub>", font=FONT, font_size=24, color=C_WHITE)
        w_vals = VGroup(w1, w2, w_dots, wn).arrange(DOWN, buff=0.22)
        
        w_lbracket = draw_bracket(height=1.8, is_left=True, color=C_PRIMARY)
        w_rbracket = draw_bracket(height=1.8, is_left=False, color=C_PRIMARY)
        w_lbracket.next_to(w_vals, LEFT, buff=0.12)
        w_rbracket.next_to(w_vals, RIGHT, buff=0.12)
        w_vec = VGroup(w_lbracket, w_vals, w_rbracket)
        
        w_eq_lbl = MarkupText("w = ", font=FONT, font_size=18, color=C_PRIMARY).next_to(w_vec, LEFT, buff=0.12)
        w_matrix_grp = VGroup(w_eq_lbl, w_vec)
        w_all = VGroup(w_desc, w_matrix_grp, w_cond).arrange(DOWN, buff=0.2).move_to([0, -0.9, 0])
        
        # 2. Khối Ma trận hiệp phương sai Σ (Sử dụng MarkupText để tránh lỗi tofu) đại diện n tài sản
       # cov_title = MarkupText("<b>Σ</b> (Ma trận hiệp phương sai):", font=FONT, font_size=20, color=C_SUCCESS)
        cov_desc = Text("Biến động & mối quan hệ giữa các tài sản", font=FONT, font_size=24, color=C_WHITE)
        
        sig11 = MarkupText("σ<sub>1</sub><sup>2</sup>", font=FONT, font_size=21, color=C_WHITE)
        sig12 = MarkupText("σ<sub>12</sub>", font=FONT, font_size=21, color=C_WHITE)
        sig1n = MarkupText("σ<sub>1n</sub>", font=FONT, font_size=21, color=C_WHITE)
        
        sig21 = MarkupText("σ<sub>21</sub>", font=FONT, font_size=21, color=C_WHITE)
        sig22 = MarkupText("σ<sub>2</sub><sup>2</sup>", font=FONT, font_size=21, color=C_WHITE)
        sig2n = MarkupText("σ<sub>2n</sub>", font=FONT, font_size=21, color=C_WHITE)
        
        sign1 = MarkupText("σ<sub>n1</sub>", font=FONT, font_size=21, color=C_WHITE)
        sign2 = MarkupText("σ<sub>n2</sub>", font=FONT, font_size=21, color=C_WHITE)
        signn = MarkupText("σ<sub>n</sub><sup>2</sup>", font=FONT, font_size=21, color=C_WHITE)
        
        # Ba chấm hàng/cột/chéo
        dots_r1 = create_horizontal_dots(C_WHITE, buff=0.08)
        dots_r2 = create_horizontal_dots(C_WHITE, buff=0.08)
        dots_rn = create_horizontal_dots(C_WHITE, buff=0.08)
        
        dots_c1 = create_vertical_dots(C_WHITE, buff=0.08)
        dots_c2 = create_vertical_dots(C_WHITE, buff=0.08)
        dots_cn = create_vertical_dots(C_WHITE, buff=0.08)
        
        dots_diag = create_diagonal_dots(C_WHITE, buff=0.08)
        
        col1 = VGroup(sig11, sig21, dots_c1, sign1).arrange(DOWN, buff=0.22)
        col2 = VGroup(sig12, sig22, dots_c2, sign2)
        col3 = VGroup(dots_r1, dots_r2, dots_diag, dots_rn)
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
            
        grid = VGroup(col1, col2, col3, col4)
        
        cov_lbracket = draw_bracket(height=2.2, is_left=True, color=C_SUCCESS)
        cov_rbracket = draw_bracket(height=2.2, is_left=False, color=C_SUCCESS)
        cov_lbracket.next_to(grid, LEFT, buff=0.15)
        cov_rbracket.next_to(grid, RIGHT, buff=0.15)
        cov_matrix = VGroup(cov_lbracket, grid, cov_rbracket)
        
        cov_eq_lbl = MarkupText("Σ = ", font=FONT, font_size=18, color=C_SUCCESS).next_to(cov_matrix, LEFT, buff=0.12)
        cov_matrix_grp = VGroup(cov_eq_lbl, cov_matrix)
        cov_all = VGroup(cov_desc, cov_matrix_grp).arrange(DOWN, buff=0.2).move_to([0, -0.9, 0])

        # Load stock images
        stock_paths = [
            "stock/MSN.jpg", "stock/fox.png", "stock/hpg.png",
            "stock/kbc.png", "stock/plx.png", "stock/ssi.png",
            "stock/vpb.jpg", "ctg.png", "fpt.png"
        ]
        stock_imgs = []
        for path in stock_paths:
            img = ImageMobject(path).scale_to_fit_width(1.0)
            stock_imgs.append(img)
            
        # Arrange in 3 rows, 3 columns centered
        row1 = Group(*stock_imgs[0:3]).arrange(RIGHT, buff=0.8).move_to([0, 1.4, 0])
        row2 = Group(*stock_imgs[3:6]).arrange(RIGHT, buff=0.8).move_to([0, 0.0, 0])
        row3 = Group(*stock_imgs[6:9]).arrange(RIGHT, buff=0.8).move_to([0, -1.4, 0])
        stock_group_flat = Group(*stock_imgs)

        part4_script_1a = "Mở rộng hơn, với danh mục đầu tư gồm có nhiều loại tài sản khác nhau,"
        with self.voiceover(text=part4_script_1a) as tracker:
            # 1. Hiện tiêu đề "Mở rộng"
            self.sp(Write(exp_title), run_time=0.5)
    
            self.update_subtitle(
                "Mở rộng hơn, với danh mục đầu tư gồm\n"
                "có nhiều loại tài sản khác nhau,",
                style="default"
            )
            
            # Dọn dẹp các đối tượng biểu đồ trước đó và cả tiêu đề cũ
            self.sp(
                FadeOut(ax), FadeOut(dots),
                FadeOut(frontier_points), FadeOut(lbl_frontier),
                FadeOut(efficient_curve), FadeOut(inefficient_curve),
                FadeOut(ttl), FadeOut(x_lbl), FadeOut(y_lbl),
                run_time=0.6
            )
            
            # Xuất hiện lần lượt từng cái một thành 3 hàng
            self.sp(FadeIn(stock_group_flat, lag_ratio=0.15), run_time=2.0)
            self.wait(max(0.1, tracker.duration - 2.6))
            
        part4_script_1b = "phương sai của danh mục được tính bằng công thức sau."
        with self.voiceover(text=part4_script_1b) as tracker:
            self.update_subtitle(
                "phương sai của danh mục được tính\nbằng công thức sau.",
                style="default"
            )
            
            # 9 ảnh biến mất
            self.sp(FadeOut(stock_group_flat), run_time=0.6)
            
            
            
            # 2. Hiện công thức đóng khung to rõ ở giữa màn hình
            self.sp(skill_pop_in(formula_grp, sound=True), run_time=0.8)
            self.wait(1.0)
            
            # 3. Đẩy công thức lên vị trí cao hơn
            self.sp(formula_grp.animate.scale(0.85).move_to([0, 1.8, 0]), run_time=0.8)
            self.wait(max(0.1, tracker.duration - 3.7))
            
        part4_script_2 = "Với w là Vector trọng số tỷ lệ phân bổ vốn vào các tài sản"
        with self.voiceover(text=part4_script_2) as tracker:
            self.update_subtitle(
                "Với w là Vector trọng số",
                style="default"
            )
            w_temp = MarkupText("w", font=FONT, font_size=32, color=C_PRIMARY, weight=BOLD).move_to([1.1, 1.8, 0])
            # Slide w down and transform it to the label first
            self.sp(ReplacementTransform(w_temp, w_eq_lbl, run_time=0.8))
            # After that, pop in the w details
            self.sp(
                skill_pop_in(w_desc),
                skill_pop_in(w_vec),
                skill_pop_in(w_cond),
                run_time=1.0
            )
            self.wait(max(0.1, tracker.duration - 1.8))
            
        part4_script_3 = "Và sigma là Ma trận hiệp phương sai của các tài sản trong danh mục "
        with self.voiceover(text=part4_script_3) as tracker:
            self.update_subtitle(
                "Và Σ là Ma trận hiệp phương sai",
                style="default"
            )
            self.sp(FadeOut(w_all), run_time=0.6)
            
            sig_temp = MarkupText("Σ", font=FONT, font_size=32, color=C_SUCCESS, weight=BOLD).move_to([0.6, 1.8, 0])
            # Slide sigma down and transform to label
            self.sp(ReplacementTransform(sig_temp, cov_eq_lbl, run_time=0.8))
            # Then pop in the covariance matrix details
            self.sp(
                skill_pop_in(cov_desc),
                skill_pop_in(cov_matrix),
                run_time=1.5
            )
            self.wait(max(0.1, tracker.duration - 2.4))

        # Dọn dẹp toàn bộ để chuyển sang scene tiếp theo
        self.sp(
            FadeOut(exp_title),
            FadeOut(formula_grp),
            FadeOut(cov_all),
            run_time=0.5
        )
        self._lift()
        self.clear_content()
