from manim import *
import numpy as np
mus = 1
rt = 1
p = 0.75
fts = 1.5*DEFAULT_FONT_SIZE

class Areas(Scene):
    def construct(self):
    
    # Initializing mobjects
        c = Circle(radius=1,color=BLUE)
        c.shift(LEFT*2)
        s = Square(side_length=0.5*PI,color=BLUE)
        s.shift(RIGHT*2)
        br = Brace(s,direction=RIGHT)
        bd = Brace(s,direction=DOWN)
        

        # Playing animations
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

class Line_to_Area(Scene):
    def construct(self):
    
        # Initializing mobjects
        s = Square(color=RED)
        l = Line(start=s.get_vertices()[3],end=s.get_vertices()[0],color=YELLOW_C)
        rec = always_redraw(lambda: Polygon(s.get_corner(UR),s.get_corner(DR),l.get_bottom(),l.get_top(),
                                            color=RED,fill_color=RED,fill_opacity=0.75))
        # Playing animations 
        self.play(Create(s),run_time=rt*2)
        self.wait()
        self.add(rec)
        self.play(l.animate.move_to(s.get_left()),run_time=rt*2)
        self.wait()

