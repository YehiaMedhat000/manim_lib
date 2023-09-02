from manim import *
import numpy as np
mus = 1
rt = 1
p = 0.75
fts = 1.5*DEFAULT_FONT_SIZE

class Circum(Scene):
    def construct(self):

        # Initializing mobjects
        c_group = VGroup(Circle(radius=1),Dot(point=DOWN))
        l = Line(start=[-PI,0,0],end=[PI,0,0],color=RED)
        
        l_ = Line(start=[-PI,0,0],end=[PI,0,0],color=BLUE)
        l_.shift(UP*2)
        b = Brace(l_,direction=UP)
        t = Tex('$2\pi$').next_to(b,direction=UP)
        
        # Playing animations
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