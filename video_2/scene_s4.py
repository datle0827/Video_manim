"""
scene_s4.py – S4: Bảng phân phối xác suất
"""

from manim import *
from config import FONT, C_SUCCESS, C_PRIMARY, C_WHITE, C_WARNING, C_GRAY, C_DANGER, SCRIPTS, SUBS
from helpers import skill_pop_in

class SceneSinglePathMixin:
    def scene_single_path(self):
        ttl = self.create_title("Bảng phân phối xác suất")

        part1_script = "Trong thực tế, không phải ngày nào nhà máy cũng có số lượng sản phẩm lỗi giống nhau."
        with self.voiceover(text=part1_script) as tracker:
            self.update_subtitle("Trong thực tế, không phải ngày nào\ncũng có số lượng lỗi giống nhau.", style="default")
            self.sp(Write(ttl, run_time=min(0.5, tracker.duration * 0.3)))
            self.wait(tracker.duration)

        # Table
        dist_table = Table(
            [["0", "0.3"],
             ["1", "0.4"],
             ["2", "0.2"],
             ["3", "0.1"]],
            col_labels=[Text("X (Số lỗi)", font=FONT, weight=BOLD), Text("P(X)", font=FONT, weight=BOLD)],
            include_outer_lines=True,
            line_config={"color": C_GRAY}
        ).scale(0.65).move_to([0, 0.8, 0])
        
        # Colorize cells
        for idx, color in enumerate([C_SUCCESS, C_WARNING, C_WARNING, C_DANGER]):
            dist_table.get_entries((idx+2, 1)).set_color(color)
            dist_table.get_entries((idx+2, 2)).set_color(color)
            
        part2_script = "Dựa trên dữ liệu trong quá khứ, số sản phẩm lỗi mỗi ngày thường rơi vào các trường hợp sau:"
        with self.voiceover(text=part2_script) as tracker:
            self.update_subtitle("Dựa trên dữ liệu trong quá khứ,\nsự phân bố lỗi thường xuất hiện như sau:", style="default")
            # Vẽ bộ khung và header bảng
            grid = VGroup(dist_table.get_horizontal_lines(), dist_table.get_vertical_lines())
            headers = dist_table.get_rows()[0]
            self.sp(Create(grid), Write(headers), run_time=1.0)
            self.wait(max(0.1, tracker.duration - 1.0))

        part3_script = "xác suất không có lỗi là không phẩy ba, có 1 lỗi là không phẩy bốn, 2 lỗi là không phẩy hai, và 3 lỗi là không phẩy một."
        with self.voiceover(text=part3_script) as tracker:
            self.update_subtitle("0 lỗi (0.3), 1 lỗi (0.4),\n2 lỗi (0.2), 3 lỗi (0.1).", style="default")
            rows = dist_table.get_rows()
            # Dùng LaggedStart để từng hàng xuất hiện khớp với thời gian đọc từng ý.
            self.sp(LaggedStart(
                Write(rows[1]),
                Write(rows[2]),
                Write(rows[3]),
                Write(rows[4]),
                lag_ratio=0.8, run_time=tracker.duration * 0.95
            ))
            self.wait(max(0.1, tracker.duration * 0.05))

        part4_script = "Bảng này chính là bảng phân phối xác suất của X,"
        with self.voiceover(text=part4_script) as tracker:
            self.update_subtitle("Bảng này chính là\nbảng phân phối xác suất của X,", style="default")
            lbl = Text("Bảng phân phối xác suất của X", font=FONT, font_size=24, color=C_WARNING).next_to(dist_table, DOWN, buff=0.6)
            self.sp(skill_pop_in(lbl, run_time=0.5))
            self.wait(tracker.duration)

        part5_script = "cho biết khả năng xảy ra của từng số lượng lỗi."
        with self.voiceover(text=part5_script) as tracker:
            self.update_subtitle("cho biết khả năng xảy ra\ncủa từng mức độ lỗi.", style="default")
            self.sp(Circumscribe(dist_table, color=C_WHITE, time_width=0.5, run_time=1.0))
            self.wait(max(0.1, tracker.duration - 1.0))

        self._lift()
        self.clear_content()

