from manim import *

class S_nat_l(Scene):
    def construct(self):
        # Initializing mobjects

        nat_l = NumberLine(x_range=[0,7],include_numbers=True,numbers_with_elongated_ticks=[0],
                            color=BLUE_C,include_tip=True)
        
        rec = SurroundingRectangle(nat_l[3][0],color=RED)
        rec_tip = SurroundingRectangle(nat_l.get_tip(), color=RED)

        arr = Arrow(start=nat_l.n2p(3),end=nat_l.n2p(6),color=RED).next_to(nat_l,UP)
        arr_x = Arrow(start=nat_l.n2p(6),end=nat_l.n2p(3),color=YELLOW).next_to(nat_l,DOWN)
        d = Dot(arr_x.get_center(),color=arr_x.get_color())
        cross = Cross(d,scale_factor=4)
        
        # Playing animations
        self.play(Write(nat_l),run_time=2)
        self.wait()
        self.play(Create(rec),Create(rec_tip))
        self.wait()
        self.play(FadeOut(rec,rec_tip))
        self.wait()
        self.play(Create(arr))
        self.wait()
        self.play(Create(arr_x))
        self.wait(3)
        self.play(Create(cross))

        for number in nat_l[3]:
            sign = MathTex('<').next_to(number, RIGHT)
            self.play(Write(sign),run_time=0.2)
        
        self.wait()