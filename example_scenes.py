import os
from manimlib import *

class DynamicTexScene(Scene):
    def construct(self):
        # 1. Gather default values
        formula_text = r"F = ma"
        animation_style = "physics_simulation"

        # 2. Extract configuration data sent by the GitHub pop-up window
        if os.path.exists("formula_input.txt"):
            with open("formula_input.txt", "r", encoding="utf-8") as f:
                content = f.read().strip()
                if content: formula_text = content

        if os.path.exists("style_input.txt"):
            with open("style_input.txt", "r", encoding="utf-8") as f:
                content = f.read().strip()
                if content: animation_style = content

        # --- LAYOUT STYLE 1: Elegant centered text layout ---
        if animation_style == "text_only":
            math_tex = Tex(formula_text)
            math_tex.scale(2.5)
            math_tex.center()
            
            self.play(Write(math_tex), run_time=2)
            self.wait(2)
            self.play(FadeOut(math_tex))

        # --- LAYOUT STYLE 2: Live physical vector block simulation ---
        elif animation_style == "physics_simulation":
            # Display the law/formula at the top
            title_formula = Tex(formula_text, color=YELLOW)
            title_formula.scale(1.8)
            title_formula.to_edge(UP, buff=0.5)
            self.play(FadeIn(title_formula, UP))

            # Create a simple flat ground track
            ground = Line(LEFT * 5, RIGHT * 5, color=GREY_B)
            ground.shift(DOWN * 1.5)
            self.play(ShowCreation(ground))

            # Draw a physical mass box on the track
            box = Square(side_length=1.5, fill_color=BLUE, fill_opacity=0.6)
            box.next_to(ground, UP, buff=0)
            box.align_to(ground, LEFT).shift(RIGHT * 1.5)
            
            box_label = Text("Mass (m)", font_size=18).move_to(box.get_center())
            self.play(FadeIn(box), FadeIn(box_label))

            # Create a Force vector pushing the box from behind
            force_arrow = Arrow(LEFT * 2, LEFT * 0.1, color=RED, buff=0)
            force_arrow.next_to(box, LEFT, buff=0.2)
            force_label = Tex(r"\vec{F}", color=RED).next_to(force_arrow, UP, buff=0.1)
            
            self.play(GrowArrow(force_arrow), Write(force_label))
            self.wait(0.5)

            # Animate constant acceleration (F = ma displacement effect)
            # The force, label, and mass move synchronously across the screen
            self.play(
                box.animate.shift(RIGHT * 4.5),
                box_label.animate.shift(RIGHT * 4.5),
                force_arrow.animate.shift(RIGHT * 4.5),
                force_label.animate.shift(RIGHT * 4.5),
                rate_func=quad_ease_in, # Smooth realistic tracking acceleration
                run_time=2.5
            )
            self.wait(1.5)
