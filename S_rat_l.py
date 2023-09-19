from manim import *

class S_rat_l(ZoomedScene):
    def construct(self):
        
        # Initializing the Integer-numbers line
        int_l = NumberLine(x_range=[-7,7],include_numbers=True,numbers_with_elongated_ticks=[0],
                           color=BLUE_B,include_tip=True,
                           numbers_to_exclude=[-7],font_size=28)
        
        # Writing the Integer-numbers line
        self.play(Write(int_l))
        self.wait(5)
        self.play(int_l.animate.to_edge(UP))
        self.wait()
        
        # WARNING:  font_size is specified because it makes the line fit to the frame

        # Initializing the raional-numbers line
        rat_l = NumberLine(x_range=[-1,1,0.25],include_numbers=True,include_ticks=True,
                           numbers_with_elongated_ticks=[0,-1.5,1.5],color=BLUE_E,length=13,font_size=28)


        # Rectangles for highlighting boundaries
        rec_int = SurroundingRectangle(VGroup(int_l.get_tick_marks()[6],int_l.get_tick_marks()[8]),
                                       buff=0.1,color=GREY)
        rec = SurroundingRectangle(rat_l,color=GREY)
        l1 = Line(start=rec_int.get_corner(DR),end=rec.get_corner(UR),color=rec.get_color())
        l2 = Line(start=rec_int.get_corner(DL),end=rec.get_corner(UL),color=rec.get_color())

        # Creating the boundaries and the rational line
        self.play(Create(rec_int), run_time=0.2)
        self.play(Create(rec),Create(l1),Create(l2),Write(rat_l),run_time=2)
        self.wait(3)

        # Fading out the unwanted mobjects
        self.play(FadeOut(int_l,rec_int,rec,l1,l2))

        # Moving the old line to the upper edge
        self.play(rat_l.animate.to_edge(UP))
    
        # Creating narrower boundaries of the old rational line
        rec_rat = SurroundingRectangle(VGroup(rat_l.get_tick_marks()[3],rat_l.get_tick_marks()[5]),
                                       buff=0.1,color=GREY)
        
        rat_l_2 = NumberLine(x_range=[-0.25,0.25,.05],include_numbers=True,include_ticks=True,
                             numbers_with_elongated_ticks=[0,-0.25,0.25],color=BLUE_E,length=13,font_size=28)
        
        # Mobjects for highlighting the new line
        rec = SurroundingRectangle(rat_l_2,color=GREY)
        l1 = Line(start=rec_rat.get_corner(DR),end=rec.get_corner(UR),color=rec.get_color())
        l2 = Line(start=rec_rat.get_corner(DL),end=rec.get_corner(UL),color=rec.get_color())

        # Playing the new animations
        self.play(Create(rec_rat),Create(l1),
                  Create(l2),Create(rec))
        
        self.play(Write(rat_l_2))

        # Fading out the unwanted mobjects
        self.play(FadeOut(rat_l,rec_rat,rec,l1,l2))
                
        # moving rat_l_2 to the upper edge
        self.play(rat_l_2.animate.to_edge(UP))

        # Initializing the raional-numbers line
        rat_l_3 = NumberLine(x_range=[-0.1,0.1,0.025],include_numbers=True,include_ticks=True,
                             numbers_with_elongated_ticks=[0,-0.1,0.1],color=BLUE_E,length=13,font_size=28)

        # Creating narrower boundaries of the old rational line
        rec_rat = SurroundingRectangle(VGroup(rat_l_2.get_tick_marks()[3],rat_l_2.get_tick_marks()[7]),buff=0.1,color=GREY)
        
        # Mobjects for highlighting the new line
        rec = SurroundingRectangle(rat_l_3,color=GREY)
        l1 = Line(start=rec_rat.get_corner(DR),end=rec.get_corner(UR),color=rec.get_color())
        l2 = Line(start=rec_rat.get_corner(DL),end=rec.get_corner(UL),color=rec.get_color())

        # Playing the new animations
        self.play(Create(rec_rat),
                  Create(l1),Create(l2),Create(rec))
        
        self.play(Write(rat_l_3))
        self.wait(3)