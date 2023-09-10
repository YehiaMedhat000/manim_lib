from manim import *

class S_count_l(Scene):
    def construct(self):
        
        # Initializing mobjects
        count_l = NumberLine(x_range=[1,7],include_numbers=True,numbers_with_elongated_ticks=[1],
                             color=BLUE_C,include_tip=True)
        
        dots = MathTex('\dots').next_to(count_l.get_tip(),DOWN)
        rec_dots = SurroundingRectangle(dots) 
        g1 = VGroup(dots,rec_dots)
        
        rec = SurroundingRectangle(count_l[3][0],color=RED)
        rec_tip = SurroundingRectangle(count_l.get_tip(), color=RED)
        g_rec_ticks = VGroup(rec,rec_tip)
        
        arr = Arrow(start=count_l.n2p(3),end=count_l.n2p(6),color=RED).next_to(count_l,UP)

        arr_x = Arrow(start=count_l.n2p(6),end=count_l.n2p(3),color=YELLOW).next_to(count_l,DOWN)
        d = Dot(arr_x.get_center(),color=arr_x.get_color())
        cross = Cross(d,scale_factor=4)

        # Playing animations
        self.play(Write(count_l))
        self.wait()

        for number in count_l[3]:
            rec_surr = SurroundingRectangle(number)
            self.play(Create(rec_surr),run_time=0.2)
            self.wait(0.1)
            self.play(FadeOut(rec_surr))
        
        self.play(Create(g1))
        self.wait()
        self.play(FadeOut(g1))
        self.play(Create(g_rec_ticks))
        self.wait()
        self.play(FadeOut(g_rec_ticks))
        self.play(Create(arr))
        self.wait(2)
        self.play(Create(arr_x))
        self.wait(2)
        self.play(Create(cross))

        for number in count_l[3]:
            sign = MathTex('<').next_to(number, RIGHT)
            self.play(Write(sign),run_time=0.2)
        self.wait()