from manim import *

class TestLatex(Scene):
    def construct(self):
        try:
            m = MathTex(r"\sigma_p^2 = w^T \Sigma w")
            self.add(m)
            self.play(Write(m))
        except Exception as e:
            print(f"LATEX_ERROR: {e}")
