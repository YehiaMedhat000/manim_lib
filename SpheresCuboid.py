from manim import *

class SpheresCuboid(ThreeDScene):
    def construct(self):

        # Initialize the TexTemplate
        temp = TexTemplate()
        temp.add_to_preamble('\\usepackage{arabtex,utf8} \n\\setcode{utf8}')
        Tex.set_default(tex_template=temp)
        MathTex.set_default(tex_template=temp)

        # Set the camera orientaion
        self.set_camera_orientation(phi=0,theta=0,gamma=90*DEGREES)
        
        # Initialize mobjects
        s_0 = Sphere(fill_opacity=0.5,checkerboard_colors=None,stroke_width=0)
        l_0 = Line(start=LEFT,end=RIGHT,color=RED)
        b_0 = Brace(Line(start=ORIGIN,end=l_0.get_end()),direction=UP)
        t_0 = Tex('\\begin{arabtex}\nنق\n\\end{arabtex}',font_size=30).next_to(b_0,direction=UP,buff=0.2)
        t_0_1 = VGroup(t_0,b_0).copy()
        
        s_1 = s_0.copy().move_to(RIGHT*2)
        l_1 = l_0.copy().move_to(s_1.get_center())
        t_1 = VGroup(t_0,b_0).copy()
        t_1_1 = VGroup(t_0,b_0).copy()
        
        s_2 = s_0.copy().move_to(LEFT*2)
        l_2 = l_0.copy().move_to(s_2.get_center())
        t_2 = VGroup(t_0,b_0).copy()
        t_2_1 = VGroup(t_0,b_0).copy()

        b_all = Brace(Line(start=LEFT*3,end=RIGHT*3),direction=UP)
        t_all = Tex('\\begin{arabtex}\n6نق\n\\end{arabtex}',font_size=60).next_to(b_all,direction=UP)

        small_braces_group = VGroup(b_0,t_0,t_0_1,t_1,t_1_1,t_2,t_2_1)
        big_brace_group = VGroup(b_all,t_all)

        # Play animations
        self.play(Create(s_0))
        self.wait(2)
        
        self.play(Create(l_0),Write(t_0),Write(b_0))
        self.wait() 
        
        t_0_1.save_state(); t_1_1.save_state()

        self.play(t_0_1.animate.shift(np.array([-1,0,0])))
        self.wait()
        
        self.play(Create(s_1),Create(s_2),run_time=0.5)
        self.play(Create(l_1),Create(l_2),run_time=0.5)
        self.play(t_1.animate.shift(RIGHT),
                  t_1_1.animate.shift(RIGHT*2),
                  t_2.animate.shift(LEFT*2),
                  t_2_1.animate.shift(LEFT*3),run_time=0.5)
        self.wait(3)
        
        self.play(ReplacementTransform(small_braces_group,big_brace_group,remover=False))
        self.wait(3)
        
        t_all.save_state()

        self.play(Unwrite(big_brace_group),remover=False)

        t_all.restore()

        self.add_fixed_in_frame_mobjects(t_all.to_corner(DOWN))
        self.play(Write(t_all))

        # TODO:
        # Make another one from the other side after rotation
        # Make these rectangle a base for stretching a prism which will represent the parallelopaipad
        
        # Set camera orientation
        self.move_camera(phi=90*DEGREES,theta=-180*DEGREES,gamma=0)

        # Initialize new mobjects
        t_0_1.restore(); t_1_1.restore()

        def rot_br(mob):
           return (mob.rotate(-90*DEGREES,axis=Z_AXIS,about_point=l_0.get_center())
             .rotate(-90*DEGREES,axis=Y_AXIS,about_point=l_0.get_center()))

        rot_br(t_0_1)
        rot_br(t_1_1)


        s_2.save_state()
        # Playing animations
        self.play(Uncreate(s_2))
        self.play(l_0.animate.rotate(90*DEGREES,axis=Z_AXIS,about_point=l_0.get_center()))
        
        b_two_r = Brace(l_0,direction=OUT)
        text_two_r = Tex('\\begin{arabtex}\n2نق\n\\end{arabtex}',font_size=30).next_to(b_two_r,direction=OUT,buff=0.2)
        two_r = VGroup(b_two_r,text_two_r)

        self.play(Write(t_0_1),t_1_1.animate.shift(UP))
        self.play(ReplacementTransform(VGroup(t_0_1,t_1_1),two_r))
        self.wait()
        #self.play(grp_2r_0.animate.shift(np.array([0,1,0])))
        
        #self.play(ReplacementTransform(VGroup(grp_2r,grp_2r_0),two_r))
        self.play(FadeOut(two_r))
        self.play(text_two_r.animate.move_to(np.array([-3,0,-1])))
        self.add_fixed_orientation_mobjects(two_r)

        self.play(l_0.animate.rotate(90*DEGREES,axis=X_AXIS,about_point=l_0.get_center()))
        
        b_two_r = Brace(l_0,direction=DOWN)
        text_two_r = Tex('\\begin{arabtex}\n2نق\n\\end{arabtex}',font_size=30).next_to(b_two_r,direction=DOWN,buff=0.2)
        two_r = VGroup(b_two_r,text_two_r)
        
        self.play(Write(two_r))

        self.wait()
        
        
        #rec_side = Line(start=np.array([-3,1,1]),end=np.array([3,1,1]),stroke_width=4,color=RED)
        #rec_other_side = rec_side.copy()
        #rec_plan = always_redraw(lambda: Polygon(rec_side.get_start(),rec_side.get_end(),rec_other_side.get_end(),
        #                                    rec_other_side.get_start(),stroke_color=RED,fill_color=PURE_BLUE,fill_opacity=0.3))

        #self.add(rec_plan)
        #self.play(rec_side.animate.move_to(np.array([0,-1,1])))
        #self.wait()