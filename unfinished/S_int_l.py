from manim import *

class S_int_l(Scene):
    def construct(self):
        
        # Initializing mobjects
        int_l = NumberLine(x_range=[-7,7],include_numbers=True,numbers_with_elongated_ticks=[0],
                           color=BLUE_B,include_tip=True,
                           numbers_to_exclude=[-7],).add_tip(at_start=True)
        
        rec = SurroundingRectangle(int_l[3][6],color=YELLOW)
        rec_tip_pos = SurroundingRectangle(int_l.get_tips()[0], color=GREEN)
        rec_tip_neg = SurroundingRectangle(int_l.get_tips()[1], color=RED)
        recs = VGroup(rec,rec_tip_neg,rec_tip_pos)

        arr = Arrow(start=int_l.n2p(3),end=int_l.n2p(6),color=RED).next_to(int_l,UP)
        arr_x = Arrow(start=int_l.n2p(6),end=int_l.n2p(3),color=YELLOW).next_to(int_l,DOWN)
        arrs = VGroup(arr,arr_x)

        # Playing animations
        self.play(GrowFromCenter(int_l))
        self.wait()
        self.play(Create(recs))
        self.wait()
        self.play(Create(arrs))
        self.wait()
        self.play(FadeOut(recs))
        self.wait()
        self.play(FadeOut(arrs))
        
        for number in int_l[3]:
            sign = MathTex('<').next_to(number, RIGHT)
            self.play(Write(sign),run_time=0.2)
            
        self.wait()