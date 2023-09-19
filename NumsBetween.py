from manim import *

class NumsBetween_stSol(ZoomedScene):
    def construct(self):
        
        # Initializing the Integer-numbers line
        num_l_0 = NumberLine(x_range=[-3,4],include_numbers=True,numbers_with_elongated_ticks=[0],color=BLUE_B,include_tip=True,
                             numbers_to_exclude=[-7],tip_width=0.35/2).scale_to_fit_width(self.camera.frame_width-1)
        
        # Writing the Integer-numbers line
        self.play(Write(num_l_0))
        self.wait()
        self.play(num_l_0.animate.to_edge(UP))
        self.wait()
        
        # Initializing the rational-numbers line
        num_l_1 = NumberLine(x_range=[0,1,0.1],include_ticks=True,
                             color=BLUE_E,length=num_l_0.get_length())
        
        labels = {round(i*0.1,1): f'$\\frac{{{i}}}{{10}}$' for i in range(0,11)}
        labels.update({2.0/3.0:'$\\frac{2}{3}$',                                                                        
                       4.0/5.0:'$\\frac{4}{5}$'})
        
        num_l_1.match_style(num_l_0)
        num_l_1.add_labels(labels)

        # Rectangles for highlighting boundaries
        rec_0 = SurroundingRectangle(VGroup(num_l_0.get_tick_marks()[3],num_l_0.get_tick_marks()[4]),
                                       buff=0.1,color=RED)
        rec_1 = SurroundingRectangle(num_l_1,color=RED).set_fill(GREY); rec_1.set_opacity(0.5)
        l1 = Line(start=rec_0.get_corner(DR),end=rec_1.get_corner(UR),color=rec_1.get_color())
        l2 = Line(start=rec_0.get_corner(DL),end=rec_1.get_corner(UL),color=rec_1.get_color())
        rec_1_1 = SurroundingRectangle(Line(start=num_l_1.n2p(2.0/3.0),end=num_l_1.n2p(0.8)),buff=0.2).match_style(rec_1)

        # Creating the boundaries and the rational line
        self.play(Create(rec_0))
        self.wait()
        self.play(Create(rec_1),Create(l1),Create(l2),Write(num_l_1))
        self.wait()
        self.play(FadeOut(l2,l1),rec_1.animate.become(rec_1_1))
        self.wait()
        self.remove(*self.mobjects)
        self.play(VGroup(num_l_1,rec_1_1).animate.to_edge(UP))
        self.wait()

        num_l_2 = NumberLine(x_range=[0,0.7,0.1],include_ticks=True,length=num_l_0.get_length())
        labels = {0:'$0.666\\dots$',0.1:'$\\frac{67}{100}$',0.2:'$\\frac{68}{100}$',0.3:'$\\frac{69}{100}$',0.4:'$\\dots$',
                  0.5:'$\\frac{78}{100}$',0.6:'$\\frac{79}{100}$',0.7:'$\\frac{80}{100}$'}
        num_l_2.match_style(num_l_0)
        num_l_2.add_labels(labels)

        rec_2 = SurroundingRectangle(num_l_2,color=RED).set_fill(GREY); rec_2.set_opacity(0.5)
        l1 = Line(start=rec_1_1.get_corner(DR),end=rec_2.get_corner(UR),color=rec_1.get_color())
        l2 = Line(start=rec_1_1.get_corner(DL),end=rec_2.get_corner(UL),color=rec_1.get_color())

        self.play(Write(num_l_2),Create(rec_2),Create(l1),Create(l2))
        self.wait()
        self.play(FadeOut(l1,l2,rec_1_1),rec_2.animate.become(SurroundingRectangle(num_l_2.labels[1:7],color=RED).set_fill(GREY).set_opacity(0.5)))
        self.wait(3)

class NumsBetween_ndSol(MovingCameraScene): # Failed to get the needed animations.
    def construct(self):
        
        # Initializing the Integer-numbers line
        num_l_0 = NumberLine(x_range=[-3,4],include_numbers=True,numbers_with_elongated_ticks=[0],color=BLUE_B,include_tip=True,
                             numbers_to_exclude=[-7],tip_width=0.35/2).scale_to_fit_width(self.camera.frame_width-1)
        
        # Writing the Integer-numbers line
        self.play(Write(num_l_0))
        self.wait()
        self.play(num_l_0.animate.to_edge(UP))
        self.wait()
        
        # Initializing the rational-numbers line
        num_l_1 = NumberLine(x_range=[0,1,0.1],include_ticks=True,
                             color=BLUE_E,length=num_l_0.get_length())
        
        labels = {round(i*0.1,1): f'$\\frac{{{i}}}{{10}}$' for i in range(0,11)}
        labels.update({2.0/3.0:'$\\frac{2}{3}$',                                                                        
                       4.0/5.0:'$\\frac{4}{5}$'})
        
        num_l_1.match_style(num_l_0)
        num_l_1.add_labels(labels)

        # Rectangles for highlighting boundaries
        rec_0 = SurroundingRectangle(VGroup(num_l_0.get_tick_marks()[3],num_l_0.get_tick_marks()[4]),
                                       buff=0.1,color=RED)
        rec_1 = SurroundingRectangle(num_l_1,color=RED).set_fill(GREY); rec_1.set_opacity(0.5)
        l1 = Line(start=rec_0.get_corner(DR),end=rec_1.get_corner(UR),color=rec_1.get_color())
        l2 = Line(start=rec_0.get_corner(DL),end=rec_1.get_corner(UL),color=rec_1.get_color())
        rec_1_1 = SurroundingRectangle(Line(start=num_l_1.n2p(2.0/3.0),end=num_l_1.n2p(0.8)),buff=0.2).match_style(rec_1)

        # Creating the boundaries and the rational line
        self.play(Create(rec_0))
        self.wait()
        self.play(Create(rec_1),Create(l1),Create(l2),Write(num_l_1))
        self.wait()
        self.play(FadeOut(l2,l1),rec_1.animate.become(rec_1_1))
        self.wait()
        self.remove(*self.mobjects)
        self.play(VGroup(num_l_1,rec_1_1).animate.to_edge(UP))
        self.wait()

        num_l_2 = NumberLine(x_range=[0,0.4,0.1],include_ticks=True,length=num_l_0.get_length())
        labels = {0:'$\\frac{20}{30}$',0.1:'$\\frac{21}{30}$',0.2:'$\\frac{22}{30}$',0.3:'$\\frac{23}{30}$',0.4:'$\\frac{24}{30}$'}
        num_l_2.match_style(num_l_0)
        num_l_2.add_labels(labels)

        rec_2 = SurroundingRectangle(num_l_2,color=RED).set_fill(GREY); rec_2.set_opacity(0.5)
        l1 = Line(start=rec_1_1.get_corner(DR),end=rec_2.get_corner(UR),color=rec_1.get_color())
        l2 = Line(start=rec_1_1.get_corner(DL),end=rec_2.get_corner(UL),color=rec_1.get_color())

        self.play(Write(num_l_2),Create(rec_2),Create(l1),Create(l2))
        self.wait()
        self.play(FadeOut(l1,l2,rec_1_1),rec_2.animate.become(SurroundingRectangle(num_l_2.labels[1:4],color=RED).set_fill(GREY).set_opacity(0.5)))
        self.wait(3)

class NumsBetween_rdSol(MovingCameraScene): # Failed to get the needed animations.
    def construct(self):
        
        # Initializing the Integer-numbers line
        num_l_0 = NumberLine(x_range=[-3,4],include_numbers=True,numbers_with_elongated_ticks=[0],color=BLUE_B,include_tip=True,
                             numbers_to_exclude=[-7],tip_width=0.35/2).scale_to_fit_width(self.camera.frame_width-1)
        
        # Writing the Integer-numbers line
        self.play(Write(num_l_0))
        self.wait()
        self.play(num_l_0.animate.to_edge(UP))
        self.wait()
        
        # Initializing the rational-numbers line
        num_l_1 = NumberLine(x_range=[0,1,0.1],include_ticks=True,
                             color=BLUE_E,length=num_l_0.get_length())
        
        labels = {round(i*0.1,1): f'$\\frac{{{i}}}{{10}}$' for i in range(0,11)}
        labels.update({2.0/3.0:'$\\frac{2}{3}$',                                                                        
                       4.0/5.0:'$\\frac{4}{5}$'})
        
        num_l_1.match_style(num_l_0)
        num_l_1.add_labels(labels)

        # Rectangles for highlighting boundaries
        rec_0 = SurroundingRectangle(VGroup(num_l_0.get_tick_marks()[3],num_l_0.get_tick_marks()[4]),
                                       buff=0.1,color=RED)
        rec_1 = SurroundingRectangle(num_l_1,color=RED).set_fill(GREY); rec_1.set_opacity(0.5)
        l1 = Line(start=rec_0.get_corner(DR),end=rec_1.get_corner(UR),color=rec_1.get_color())
        l2 = Line(start=rec_0.get_corner(DL),end=rec_1.get_corner(UL),color=rec_1.get_color())
        rec_1_1 = SurroundingRectangle(Line(start=num_l_1.n2p(2.0/3.0),end=num_l_1.n2p(0.8)),buff=0.2).match_style(rec_1)

        # Creating the boundaries and the rational line
        self.play(Create(rec_0))
        self.wait()
        self.play(Create(rec_1),Create(l1),Create(l2),Write(num_l_1))
        self.wait()
        self.play(FadeOut(l2,l1),rec_1.animate.become(rec_1_1))
        self.wait()
        self.remove(*self.mobjects)
        self.play(VGroup(num_l_1,rec_1_1).animate.to_edge(UP))
        self.wait()

        num_l_2 = NumberLine(x_range=[0,8],include_ticks=True,length=num_l_0.get_length())
        labels = {0:'$\\frac{40}{60}$',1:'$\\frac{41}{60}$',2:'$\\frac{42}{60}$',3:'$\\frac{43}{60}$',4:'$\\frac{44}{60}$',
                  5:'$\\frac{45}{60}$',6:'$\\frac{46}{60}$',7:'$\\frac{47}{60}$',8:'$\\frac{48}{60}$'}
        num_l_2.match_style(num_l_0)
        num_l_2.add_labels(labels)

        rec_2 = SurroundingRectangle(num_l_2,color=RED).set_fill(GREY); rec_2.set_opacity(0.5)
        l1 = Line(start=rec_1_1.get_corner(DR),end=rec_2.get_corner(UR),color=rec_1.get_color())
        l2 = Line(start=rec_1_1.get_corner(DL),end=rec_2.get_corner(UL),color=rec_1.get_color())

        self.play(Write(num_l_2),Create(rec_2),Create(l1),Create(l2))
        self.wait()
        self.play(FadeOut(l1,l2,rec_1_1),rec_2.animate.become(SurroundingRectangle(num_l_2.labels[1:8],color=RED).set_fill(GREY).set_opacity(0.5)))
        self.wait(3)