from manim import *
import numpy as np
mus = 1
rt = 1
p = 0.75
fts = 1.5*DEFAULT_FONT_SIZE

# Define the equation scene
class Eq1(Scene):
    def construct(self):
        # Define the steps of solving the equation
        eq1 = MathTex('{{x}}', '+', '{{5}}', '=', '{{7}}',font_size=fts)
        eq2 = MathTex('{{x}}', '=', '{{7}}', '-', '{{5}}',font_size=fts)
        eq3 = MathTex('{{x}}', '=', '{{2}}',font_size=fts)
        
        # Define some arrows showing the flow of the solution
        """ arr1 = Arrow(start=UP,
                     end=DOWN,
                     color=RED)
        arr2 = Arrow(start=UP,
                     end=DOWN,
                     color=BLUE) """
        
        # Shift each equation so they fit in the screen
        """ arr1.shift(UP)
        arr2.shift(DOWN)
        eq1.shift(UP*2)
        eq3.shift(DOWN*2) """
        
        # Play the animations
        self.play(Write(eq1),run_time=rt*2)
        self.wait()
        self.play(TransformMatchingTex(eq1,eq2),run_time=rt*2)
        self.wait()
        self.play(TransformMatchingTex(eq2,eq3),run_time=rt*2)
 
# Make another class with equations with factor other than 1
class Eq2(Scene):
    def construct(self):
    # Define the steps of solving the equation
        eq1 = Tex('2x + 15 = 25 ',font_size=fts)
        eq2 = Tex('2x = 25 - 15',font_size=fts)
        eq3 = Tex('2x = 10',font_size=fts)
        eq4 = Tex(r'$\frac{2x}{2} = \frac{10}{2}$',font_size=fts)
        eq5 = Tex('x = 5',font_size=fts)

        # Shift the positions of the equations
        eq1.shift([-3,2,0])
        eq2.shift([3,2,0])
        eq3.shift([-3,-1,0])
        eq4.shift([-3,-1,0])
        eq5.shift([3,-1,0])
        
        # Define some arrows showing the flow of the solution
        arr1 = Arrow(start=eq1.get_right(),
                    end=eq2.get_left(),
                    color=RED)
        arr2 = Arrow(start=eq2.get_bottom(),
                    end=eq3.get_top(),
                    color=BLUE)
        arr3 = Arrow(start=eq3.get_right(),
                    end=eq5.get_left(),
                    color=GREEN)

        # Play the animations
        mobjects = [eq1,arr1,eq2,arr2,eq3,eq4,arr3,eq5]
        for mobj in mobjects:
            if mobj == eq4:
                self.play(Transform(eq3,eq4))
            self.play(Create(mobj),run_time=rt)
            self.pause(p)