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
from scene_s1     import SceneS1Mixin
from scene_s2     import SceneS2Mixin
from scene_s3     import SceneS3Mixin
from scene_s4     import SceneS4Mixin
from scene_s5     import SceneS5Mixin
from scene_s6     import SceneS6Mixin
from scene_s7     import SceneS7Mixin
from scene_s7b    import SceneS7bMixin
from scene_s8     import SceneS8Mixin
from scene_s9     import SceneS9Mixin
from scene_s10    import SceneS10Mixin
from scene_s11    import SceneS11Mixin
from scene_s12    import SceneS12Mixin
from scene_s13    import SceneS13Mixin
from scene_s14    import SceneS14Mixin

# ── Cấu hình Manim ──────────────────────────────────────────────────────────
config.pixel_width      = VIDEO_W
config.pixel_height     = VIDEO_H
config.frame_width      = FRAME_W
config.frame_height     = FRAME_H
config.background_color = BG_COLOR

generate_audio()


# ── Class tổng hợp ──────────────────────────────────────────────────────────
class LoanDecisionTree(
    SceneS1Mixin,
    SceneS2Mixin,
    SceneS3Mixin,
    SceneS4Mixin,
    SceneS5Mixin,
    SceneS6Mixin,
    SceneS7Mixin,
    SceneS7bMixin,
    SceneS8Mixin,
    SceneS9Mixin,
    SceneS10Mixin,
    SceneS11Mixin,
    SceneS12Mixin,
    SceneS13Mixin,
    SceneS14Mixin,
    LoanDecisionTreeBase,   # phải đứng cuối (cung cấp setup & Scene)
):
    def construct(self):
        self.scene_s1()
        self.scene_s2()
        # self.scene_s3()
        self.scene_s4()
        self.scene_s5()
        self.scene_s6()
        self.scene_s7()
        self.scene_s7b()
        self.scene_s8()
        self.scene_s9()
        self.scene_s10()
        self.scene_s11()
        self.scene_s12()
        self.scene_s13()
        self.scene_s14()


# ── Entry point ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Audio ready.")
    print("Render: manim -qh video_3_main.py LoanDecisionTree")
    sys.exit(0)
