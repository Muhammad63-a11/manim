import os
from manimlib import *

class DynamicTexScene(Scene):
    def construct(self):
        # Default fallback formula text
        formula_text = r"E = mc^2"
        
        # Read the formula text passed from the GitHub workflow popup
        if os.path.exists("formula_input.txt"):
            with open("formula_input.txt", "r", encoding="utf-8") as f:
                content = f.read().strip()
                if content:
                    formula_text = content

        # Render the custom raw formula text dynamically
        math_tex = Tex(formula_text)
        math_tex.scale(2)
        math_tex.center()

        # Beautiful default animation effects
        self.play(Write(math_tex), run_time=2)
        self.wait(2)
        self.play(FadeOut(math_tex))
