from manim import *

# First scene: Counting-numbers line50
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


# Second scene: Natural-numbers line
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
        

# Third Scene: Integer-numbers line
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


# Fourth Scene: Rational-numbers line
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

class AnyToFrac(Scene):
    def construct(self):
        
        temp = TexTemplate()
        temp.add_to_preamble('\\usepackage{cancel}')
        MathTex.set_default(tex_template=temp)
        Tex.set_default(tex_template=temp)

        # Initializing Tex template
        p1 = MathTex('\\left|-9\\dfrac{1}{3}\\right|')
        p1_1 = MathTex('9\\dfrac{1}{3}')
        p1_2 = MathTex('\\dfrac{1+9\\times 3}{3}')
        p1_3 = MathTex('\\dfrac{28}{3}')

        p2 = MathTex('0.15')
        p2_1 = MathTex('\\frac{15}{100}')
        p2_2 = MathTex('\\frac{5\\times 3}{5\\times 20}')
        p2_3 = MathTex('\\frac{\\cancel 5\\times 3}{\\cancel 5\\times 20}')
        p2_4 = MathTex('\\frac{3}{20}')

        p3 = MathTex('40\\%')
        p3_1 = MathTex('\\frac{40}{100}')
        p3_2 = MathTex('\\frac{4\\times \\cancel {10}}{10\\times \\cancel {10}}')
        p3_3 = MathTex('\\frac{4}{10}')
        p3_4 = MathTex('\\frac{2\\times 2}{5\\times 2}')
        p3_5 = MathTex('\\frac{2\\times \\cancel 2}{5\\times \\cancel 2}')
        p3_6 = MathTex('\\frac{2}{5}')

        p4 = MathTex('75\\%')
        p4_1 = MathTex('\\frac{75}{100}')
        p4_2 = MathTex('\\frac{25\\times 3}{25 \\times 4}')
        p4_3 = MathTex('\\frac{\\cancel{25} \\times 3}{\\cancel{25} \\times 4}')
        p4_4 = MathTex('\\frac{3}{4}')

        p5 = MathTex('0.1313131313 \dots')
        p5_1 = MathTex('\\frac{13}{99}')

        p6 = MathTex('0.133133133133 \dots')
        p6_1 = MathTex('\\frac{133}{999}')
        p6_2 = MathTex('0.144414441444 \dots')
        p6_3 = MathTex('\\frac{1444}{9999}')

        p7 = MathTex('-\\left|56\\%\\right|')
        p7_1 = MathTex('-56\\%')
        p7_2 = MathTex('-\\frac{56}{100}')
        p7_3 = MathTex('-\\frac{14 \\times 4}{25 \\times 4}')
        p7_4 = MathTex('-\\frac{14 \\times \\cancel{4}}{25 \\times \\cancel{4}}')
        p7_5 = MathTex('-\\frac{14}{25}')

        p8 = MathTex('-\\left(-0.88\\right)')
        p8_1 = MathTex('0.88')
        p8_2 = MathTex('\\frac{88}{100}')
        p8_3 = MathTex('\\frac{4 \\times 22}{4 \\times 25}')
        p8_4 = MathTex('\\frac{\\cancel{4} \\times 22}{\\cancel{4} \\times 25}')
        p8_5 = MathTex('\\frac{22}{25}')

        p9 = MathTex('-\\left|35\\frac{2}{10}\\right|')
        p9_1 = MathTex('-35\\frac{2}{2 \\times 5}')
        p9_2 = MathTex('-35\\frac{\\cancel 2}{\\cancel 2 \\times 5}')
        p9_3 = MathTex('-35\\frac{1}{5}')
        p9_4 = MathTex('-\\frac{1+35 \\times 5}{5}')
        p9_5 = MathTex('-\\frac{1+175}{5}')
        p9_6 = MathTex('-\\frac{176}{5}')

        mobjects = [[p1,p1_1,p1_2,p1_3],
                    [p2,p2_1,p2_2,p2_3,p2_4],
                    [p3,p3_1,p3_2,p3_3,p3_4,p3_5,p3_6],
                    [p4,p4_1,p4_2,p4_3,p4_4],
                    [p5,p5_1],
                    [p6,p6_1,p6_2,p6_3],
                    [p7,p7_1,p7_2,p7_3,p7_4,p7_5],
                    [p8,p8_1,p8_2,p8_3,p8_4,p8_5],
                    [p9,p9_1,p9_2,p9_3,p9_4,p9_5,p9_6]]

        # Playing animations
        for l in mobjects:
            self.play(Write(l[0]))
            self.wait()

            for i in range(len(l)):
                if i == len(l)-1:
                    continue
                
                if i == len(l)-2:
                    self.play(ReplacementTransform(l[i],l[i+1].set_color(GREEN)))

                self.play(ReplacementTransform(l[i],l[i+1]))
                self.wait()
                self.clear()


class FracForms(Scene):
    def construct(self): 

        temp = TexTemplate(post_doc_commands='\\fontsize{35}{0}')
        temp.add_to_preamble('\\usepackage{cancel}')
        MathTex.set_default(tex_template=temp)
        Tex.set_default(tex_template=temp)

        # the ratio form 
        rat_1 = MathTex('\\frac{7}{5} = 1.4')
        rat_1_1 = MathTex('\\frac{7}{5} = \\frac{7\\times2}{5\\times2}')
        rat_1_2 = MathTex('\\frac{7}{5} = \\frac{14}{10}')
        rat_1_b = rat_1.copy()
        
        rat_2 = MathTex('\\frac{3}{4} = 0.75')
        rat_2_1 = MathTex('\\frac{3}{4} = \\frac{3\\times25}{4\\times25}')
        rat_2_2 = MathTex('\\frac{3}{4} = \\frac{75}{100}')
        rat_2_b = rat_2.copy()
        
        # the percentage form 
        per_1 = MathTex('\\frac{7}{5} = 140\\%')
        per_1_1 = MathTex('\\frac{7}{5} = \\frac{140}{100}')
        per_1_2 = MathTex('\\frac{7}{5} = 1.4')
        per_1_b = per_1.copy()

        per_2 = MathTex('\\frac{3}{4} = 75\\%')
        per_2_1 = MathTex('\\frac{3}{4} = \\frac{75}{100}')
        per_2_2 = MathTex('\\frac{3}{4} = 0.75')
        per_2_b = per_2.copy()

        # Inifintely digited numbers or cirular numbers
        circ_1 = MathTex('\\frac{1}{3} = 0. \\dot{3}')
        circ_1_1 = MathTex('\\frac{1}{3} = \\frac{1\\times3}{3\\times3}')
        circ_1_2 = MathTex('\\frac{1}{3} = \\frac{3}{9}')
        circ_1_b = circ_1.copy()

        circ_2 = MathTex('\\frac{2}{11} = 0.\\dot{1}\\dot{8}')
        circ_2_1 = MathTex('\\frac{2}{11} = \\frac{2\\times9}{11\\times9}')
        circ_2_2 = MathTex('\\frac{2}{11} = \\frac{18}{99}')
        circ_2_b = circ_2.copy()

        # Play animations
        mobjects = [[rat_1,rat_1_1,rat_1_2,rat_1_b],
                    [rat_2,rat_2_1,rat_2_2,rat_2_b],
                    [per_1,per_1_1,per_1_2,per_1_b],
                    [per_2,per_2_1,per_2_2,per_2_b],
                    [circ_1,circ_1_1,circ_1_2,circ_1_b],
                    [circ_2,circ_2_1,circ_2_2,circ_2_b]]

        # Play animations
        for l in mobjects:
            self.play(Write(l[0]))
            self.wait(2)
            self.play(ReplacementTransform(l[0],l[1]))
            self.wait()
            self.play(ReplacementTransform(l[1],l[2]))
            self.wait()
            self.play(ReplacementTransform(l[2],l[3].set_color(RED)))
            self.wait()
            self.clear()

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

class SR_Numline(Scene):
    def construct(self):
        
        # Initialize Mobjects
        num_l_0 = NumberLine(x_range=[-10,10],include_numbers=True,include_ticks=True,length=13,color=BLUE)
        num = ValueTracker(3) 
        multiplier = ValueTracker(-2)
        p_end = ValueTracker(3)

        arr_0 = always_redraw(lambda: Arrow(start=num_l_0.n2p(0)+(UP*0.5),
                                            end=num_l_0.n2p(p_end.get_value())+(UP*0.5),color=BLUE,buff=0))

        num_0 = always_redraw(lambda: DecimalNumber(number=num.get_value(),num_decimal_places=0,
                                                    include_sign=True,color=arr_0.get_color()))

        f_0 = always_redraw(lambda: MathTex('\\times').next_to(num_0))

        num_1 = always_redraw(lambda: DecimalNumber(number=multiplier.get_value(),num_decimal_places=0,include_sign=True))

        arr_0.add_updater(lambda mob: mob.set_color(RED) if p_end.get_value() < 0 else mob.set_color(BLUE))
        num_0.add_updater(lambda mob: mob.next_to(arr_0,UP))
        f_0.add_updater(lambda mob: mob.next_to(num_0))
        num_1.add_updater(lambda mob: mob.next_to(f_0))
        
        # Playing animations
        self.play(Write(num_l_0))
        
        self.wait(2)
        self.play(Create(arr_0),Write(num_0))
        
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