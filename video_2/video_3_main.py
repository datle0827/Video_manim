#!/usr/bin/env python3
"""
video_3_main.py – Class tổng hợp, kết hợp tất cả mixin scene.

Render:
    manim -qh video_3_main.py LoanDecisionTree

Sinh audio trước:
    python video_3_main.py
"""

import os, sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)
from manim import *
from config import (
    VIDEO_W, VIDEO_H, FRAME_W, FRAME_H, BG_COLOR,
    generate_audio,
)
from base_scene   import LoanDecisionTreeBase
from scene_s1     import SceneIntroMixin
from scene_s2     import SceneProblemMixin
from scene_s3     import SceneTreeMixin
from scene_s4     import SceneSinglePathMixin
from scene_s5     import SceneTotalProbMixin
from scene_s6     import SceneSummaryMixin
from scene_s7     import SceneKeywordsMixin
from scene_s8     import SceneSummaryTopicsMixin
from scene_s9     import SceneQuestionMixin

# ── Cấu hình Manim ──────────────────────────────────────────────────────────
config.pixel_width      = VIDEO_W
config.pixel_height     = VIDEO_H
config.frame_width      = FRAME_W
config.frame_height     = FRAME_H
config.background_color = BG_COLOR

generate_audio()


# ── Class tổng hợp ──────────────────────────────────────────────────────────
class LoanDecisionTree(
    SceneIntroMixin,
    SceneProblemMixin,
    SceneTreeMixin,
    SceneSinglePathMixin,
    SceneTotalProbMixin,
    SceneSummaryMixin,
    SceneKeywordsMixin,
    SceneSummaryTopicsMixin,
    SceneQuestionMixin,
    LoanDecisionTreeBase,   # phải đứng cuối (cung cấp setup & Scene)
):
    def construct(self):
        self.scene_intro()
        self.scene_problem()
        self.scene_tree()
        self.scene_single_path()
        self.scene_total_prob()
        self.scene_summary()
        self.scene_keywords()
        self.scene_summary_topics()
        self.scene_question()


# ── Entry point ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Audio ready.")
    print("Render: manim -qh video_3_main.py LoanDecisionTree")
    sys.exit(0)
