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

class Circum(Scene):
    def construct(self):
        c_group = VGroup(Circle(radius=1),Dot(point=DOWN))
        l = Line(start=[-PI,0,0],end=[PI,0,0],color=RED)
        
        l_ = Line(start=[-PI,0,0],end=[PI,0,0],color=BLUE)
        l_.shift(UP*2)
        b = Brace(l_,direction=UP)
        t = Tex('$2\pi$').next_to(b,direction=UP)
        
        self.play(Create(c_group,run_time=rt))
        self.wait()

        self.play(Create(l_,run_time=rt),
                  Create(b,run_time=rt),
                  Create(t))
        
        self.wait()
        self.play(Transform(c_group,l,run_time=rt*2))
        self.wait()
        
        self.play(l.animate.move_to(l_))
        self.wait(2)

# Explaining the Areas
class Areas(Scene):
    def construct(self):
        c = Circle(radius=1,color=BLUE)
        c.shift(LEFT*2)
        s = Square(side_length=0.5*PI,color=BLUE)
        s.shift(RIGHT*2)
        br = Brace(s,direction=RIGHT)
        bd = Brace(s,direction=DOWN)
        
        
        self.play(Create(c))
        self.play(c.animate.set_fill(color=RED,opacity=1))
        self.play(Create(s))
        self.play(s.animate.set_fill(color=RED,opacity=1))
        
        self.play(Create(br,run_time=rt),
                  Create(bd,run_time=rt),
                  Create(Tex('$1$').next_to(br),run_time=rt),
                  Create(Tex('$1$').next_to(bd,direction=DOWN),run_time=rt))
        
        self.play(Create(Tex('$2\pi$').move_to(c)))
        self.play(Create(Tex('$1$').move_to(s)))
        
        self.wait()


# Try enhancing it
class Try(Scene):
    def construct(self):
        s = Square(color=RED)
        l = Line(start=s.get_vertices()[3],end=s.get_vertices()[0],color=YELLOW_C)
        rec = always_redraw(lambda: Polygon(s.get_corner(UR),s.get_corner(DR),l.get_bottom(),l.get_top(),
                                            color=RED,fill_color=RED,fill_opacity=0.75))
    
        self.play(Create(s),run_time=rt*2)
        self.wait()
        self.add(rec)
        self.play(l.animate.move_to(s.get_left()),run_time=rt*2)
        self.wait()

