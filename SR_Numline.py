from manim import *

class SR_Numline(Scene):
    def construct(self):
        
        # Initialize Mobjects
        num_l_0 = NumberLine(x_range=[-10,10],include_numbers=True,include_ticks=True,length=13,color=BLUE)
        num = ValueTracker(3) 
        multiplier = ValueTracker(-2)
        p_end = ValueTracker(3)

        arr = always_redraw(lambda: Arrow(start=num_l_0.n2p(0)+(UP*0.5),
                                            end=num_l_0.n2p(p_end.get_value())+(UP*0.5),color=BLUE,buff=0))

        num_0 = always_redraw(lambda: DecimalNumber(number=num.get_value(),num_decimal_places=0,
                                                    include_sign=True,color=arr.get_color()))

        f_0 = always_redraw(lambda: MathTex('\\times').next_to(num_0))

        num_1 = always_redraw(lambda: DecimalNumber(number=multiplier.get_value(),num_decimal_places=0,include_sign=True))

        arr.add_updater(lambda mob: mob.set_color(RED) if p_end.get_value() < 0 else mob.set_color(BLUE))
        num_0.add_updater(lambda mob: mob.next_to(arr,UP))
        f_0.add_updater(lambda mob: mob.next_to(num_0))
        num_1.add_updater(lambda mob: mob.next_to(f_0))
        
        # Playing animations
        self.play(Write(num_l_0))
        
        self.wait(2)
        self.play(Create(arr),Write(num_0))
        
        self.wait(2)
        self.play(Write(f_0),Write(num_1))
        
        self.wait(2)
        self.play(p_end.animate.set_value(-6),
                  num.animate.set_value(-6),
                  multiplier.animate.set_value(1))
        
        self.wait(2)
        self.play(multiplier.animate.set_value(-1),run_time=0.25)
        self.play(Indicate(num_1,scale_factor=1.5,color=RED))
        
        self.wait(2)
        self.play(p_end.animate.set_value(6),
                  num.animate.set_value(6),
                  multiplier.animate.set_value(1))
        
        self.wait(2)
        self.play(multiplier.animate.set_value(2),
                  ReplacementTransform(f_0,MathTex('\\div').match_updaters(f_0)))
        self.play(Indicate(num_1,scale_factor=1.5,color=RED))
        
        self.wait(2)
        self.play(p_end.animate.set_value(3),
                  num.animate.set_value(3),
                  multiplier.animate.set_value(1))
        self.wait(3)