"""
scene_s8.py – S8: Tổng kết kiến thức
"""

from manim import *
from config import FONT, C_SUCCESS, C_PRIMARY, C_WHITE, C_WARNING, C_GRAY, C_PURPLE, C_DANGER, SCRIPTS, SUBS
from helpers import skill_pop_in, flow_block, load_icon, rnode

class SceneSummaryTopicsMixin:
    def scene_summary_topics(self):
        ttl = self.create_title("Tổng kết bài học")

        part1_script = "Qua ví dụ này, ta thấy rằng biến ngẫu nhiên rời rạc là một công cụ rất hữu ích."
        with self.voiceover(text=part1_script) as tracker:
            self.update_subtitle("Qua ví dụ này, ta thấy biến ngẫu nhiên rời rạc\nlà một công cụ rất hữu ích.", style="default")
            self.sp(Write(ttl, run_time=min(0.5, tracker.duration * 0.5)))
            self.wait(tracker.duration)
            
        # Các khái niệm đóng khung kèm Icon
        i1 = load_icon("icon_process", width=0.7, bg_color=C_PRIMARY)
        k1_grp = VGroup(i1, rnode("Biến ngẫu nhiên", C_PRIMARY, w=4.0)).arrange(RIGHT, buff=0.3)
        
        i2 = load_icon("icon_decision_tree", width=0.7, bg_color=C_WARNING)
        k2_grp = VGroup(i2, rnode("Hàm phân phối", C_WARNING, w=4.0)).arrange(RIGHT, buff=0.3)
        
        i3 = load_icon("icon_approve", width=0.7, bg_color=C_SUCCESS)
        k3_grp = VGroup(i3, rnode("Kỳ vọng E(X)", C_SUCCESS, w=4.0)).arrange(RIGHT, buff=0.3)
        
        i4 = load_icon("icon_risk", width=0.7, bg_color=C_DANGER)
        k4_grp = VGroup(i4, rnode("Phương sai Var(X)", C_DANGER, w=4.0)).arrange(RIGHT, buff=0.3)
        
        grp = VGroup(k1_grp, k2_grp, k3_grp, k4_grp).arrange(DOWN, buff=0.4).move_to([0, -0.5, 0])

        part2_script = "Trong video này mình đề cập tới các khái niệm quan trọng: Biến ngẫu nhiên rời rạc, hàm phân phối xác suất, kỳ vọng, và phương sai."
        with self.voiceover(text=part2_script) as tracker:
            self.update_subtitle("Trong video này mình đề cập tới 4 khái niệm:\nBiến rời rạc, Hàm phân phối, Kỳ vọng & Phương sai.", style="default")
            self.wait(min(1.0, tracker.duration * 0.1)) # Đợi đọc phần đầu câu
            
            t_left = tracker.duration - min(1.0, tracker.duration * 0.1)
            interval = max(0.5, t_left / 4.0)
            
            self.sp(skill_pop_in(k1_grp, sound=True, run_time=0.4))
            self.wait(max(0.1, interval - 0.4))
            self.sp(skill_pop_in(k2_grp, sound=True, run_time=0.4))
            self.wait(max(0.1, interval - 0.4))
            self.sp(skill_pop_in(k3_grp, sound=True, run_time=0.4))
            self.wait(max(0.1, interval - 0.4))
            self.sp(skill_pop_in(k4_grp, sound=True, run_time=0.4))
            self.wait(max(0.1, interval - 0.4))

        self._lift()
        self.clear_content()

