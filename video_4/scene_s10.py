"""
scene_s10.py – S10: Giải quyết vấn đề
"""

from manim import *
from config import FONT, C_PRIMARY, C_SUCCESS, C_WARNING, C_GRAY, C_WHITE, C_DANGER, FAMI_BLUE, FAMI_CYAN
from helpers import skill_pop_in, rnode

class SceneS10Mixin:
    def scene_s10(self):
        ttl = self.create_title("Quy trình Xử lý")

        # --- STAGE 1: Data Pipeline ---
        n1 = rnode("Thu thập dữ liệu", FAMI_BLUE, w=3.5, h=0.7, fs=14)
        n2 = rnode("Tiền xử lý dữ liệu", FAMI_CYAN, w=3.5, h=0.7, fs=14)
        n3 = rnode("Xây dựng mô hình", C_WARNING, w=3.5, h=0.7, fs=14)
        n4 = rnode("Đánh giá mô hình", C_DANGER, w=3.5, h=0.7, fs=14)
        n5 = rnode("Ra quyết định", C_SUCCESS, w=3.5, h=0.7, fs=14)

        n1.move_to([0, 2.8, 0])
        n2.move_to([0, 1.5, 0])
        n3.move_to([0, 0.2, 0])
        n4.move_to([0, -1.1, 0])
        n5.move_to([0, -2.4, 0])

        arr1 = Arrow(n1.get_bottom(), n2.get_top(), color=C_GRAY, buff=0.1, max_stroke_width_to_length_ratio=8)
        arr2 = Arrow(n2.get_bottom(), n3.get_top(), color=C_GRAY, buff=0.1, max_stroke_width_to_length_ratio=8)
        arr3 = Arrow(n3.get_bottom(), n4.get_top(), color=C_GRAY, buff=0.1, max_stroke_width_to_length_ratio=8)
        arr4 = Arrow(n4.get_bottom(), n5.get_top(), color=C_GRAY, buff=0.1, max_stroke_width_to_length_ratio=8)

        pipeline_grp = VGroup(n1, arr1, n2, arr2, n3, arr3, n4, arr4, n5)

        # --- STAGE 2: Decision Tree ---
        root = rnode("Phát hiện Outlier", C_DANGER, w=4.5, h=0.7, fs=16, bold=True).move_to([0, 2.0, 0])

        branch_left = rnode("Lỗi nhập liệu", C_WARNING, w=3.2, h=0.7, fs=15).move_to([-2.0, 0.4, 0])
        action_left = rnode("Chỉnh sửa / Loại bỏ", C_GRAY, w=3.2, h=0.7, fs=15).move_to([-2.0, -1.4, 0])

        branch_right = rnode("Trường hợp thực tế", C_SUCCESS, w=3.2, h=0.7, fs=15).move_to([2.0, 0.4, 0])
        action_right = rnode("Mô hình khác", FAMI_BLUE, w=3.2, h=0.9, fs=15, bold=True).move_to([2.0, -1.4, 0])

        # Connective arrows for decision tree
        arr_root_l = Arrow(root.get_bottom(), branch_left.get_top(), color=C_GRAY, buff=0.1)
        arr_root_r = Arrow(root.get_bottom(), branch_right.get_top(), color=C_GRAY, buff=0.1)
        arr_l_act  = Arrow(branch_left.get_bottom(), action_left.get_top(), color=C_GRAY, buff=0.1)
        arr_r_act  = Arrow(branch_right.get_bottom(), action_right.get_top(), color=C_GRAY, buff=0.1)

        # --- ANIMATION FLOW ---

        part1_script = "Vì vậy, trước khi xây dựng một mô hình, tiền xử lý dữ liệu là 1 bước quan trọng để làm sạch và phát hiện những điểm bất thường, có thể làm ảnh hưởng đến kết quả của mô hình."
        with self.voiceover(text=part1_script) as tracker:
            self.update_subtitle("Trước khi xây dựng mô hình, tiền xử lý dữ liệu", style="default")
            self.sp(Write(ttl, run_time=0.5))
            
            # Pop in pipeline steps sequentially
            self.sp(skill_pop_in(n1, sound=True), run_time=1)
            self.wait(0.3)
            self.sp(Create(arr1), skill_pop_in(n2, sound=True), run_time=0.5)
            self.wait(0.8)
            
            self.update_subtitle("là bước quan trọng để làm sạch", style="default")
            self.sp(Create(arr2), skill_pop_in(n3, sound=True), run_time=0.7)
            self.wait(0.8)
            
            self.sp(Create(arr3), skill_pop_in(n4, sound=True), run_time=0.7)
            self.wait(0.8)
            
            self.update_subtitle("và phát hiện bất thường \n làm ảnh hưởng mô hình.", style="default")
            self.sp(Create(arr4), skill_pop_in(n5, sound=True), run_time=0.7)
            self.wait(max(0.1, tracker.duration - 5.5))
 
        part2_script = "Nếu điểm đó là lỗi nhập liệu, có thể loại bỏ hoặc chỉnh sửa. Nếu là trường hợp đặc biệt nhưng có ý nghĩa thực tế, cần cân nhắc các phương pháp hồi quy bền vững hơn."
        with self.voiceover(text=part2_script) as tracker:
            self.update_subtitle("Nếu là lỗi nhập liệu, có thể loại bỏ hoặc sửa.", style="default")
            
            # 3D Flip Card Transition: Rotate pipeline_grp out 90 degrees
            self.sp(Rotate(pipeline_grp, angle=PI/2, axis=UP), run_time=0.5)
            self.remove(pipeline_grp)
            
            # Pre-rotate root by -90 degrees, add and flip it back in
            root.rotate(angle=-PI/2, axis=UP)
            self.add(root)
            self.sp(Rotate(root, angle=PI/2, axis=UP), run_time=0.5)
            self.wait(0.4)
            
            # Reveal left decision branch
            self.sp(
                Create(arr_root_l),
                skill_pop_in(branch_left, sound=True),
                run_time=0.8
            )
            self.sp(
                Create(arr_l_act),
                skill_pop_in(action_left, sound=True),
                run_time=0.8
            )
            self.wait(1)
            
            # Reveal right decision branch
            self.update_subtitle("Nếu là trường hợp đặc biệt,\n cần hồi quy bền vững.", style="default")
            self.sp(
                Create(arr_root_r),
                skill_pop_in(branch_right, sound=True),
                run_time=0.5
            )
            self.sp(
                Create(arr_r_act),
                skill_pop_in(action_right, sound=True),
                run_time=0.5
            )
            self.sp(Wiggle(action_right), run_time=0.8)
            self.wait(max(0.1, tracker.duration - 5.0))

        self._lift()
        self.clear_content()
