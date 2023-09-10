from manim import *

class SpheresCuboid(ThreeDScene):
    def construct(self):
        
        # Initialize the TexTemplate
        temp = TexTemplate()
        temp.add_to_preamble('\\usepackage{arabtex,utf8} \n\\setcode{utf8}')
        Tex.set_default(tex_template=temp)
        MathTex.set_default(tex_template=temp)

        # Set camera Orientation
        self.set_camera_orientation(phi=0)

        # Initialize mobjects
        s_0 = Sphere(fill_opacity=0.5,checkerboard_colors=None,stroke_width=0)
        l_0 = Line3D(start=np.array([-1,0,0]),end=np.array([1,0,0]),color=RED)
        b_0 = Brace(Line3D(start=ORIGIN,end=np.array([1,0,0])),direction=UP)
        t_0 = Tex('\\begin{arabtex}\nنق\n\\end{arabtex}',font_size=30).next_to(b_0,direction=UP,buff=0.2)
        t_0_1 = VGroup(t_0,b_0).copy()
        
        s_1 = s_0.copy().move_to(np.array([2,0,0]))
        l_1 = l_0.copy().move_to(s_1.get_center())
        t_1 = VGroup(t_0,b_0).copy()
        t_1_1 = VGroup(t_0,b_0).copy()
        
        s_2 = s_0.copy().move_to(np.array([-2,0,0]))
        l_2 = l_0.copy().move_to(s_2.get_center())
        t_2 = VGroup(t_0,b_0).copy()
        t_2_1 = VGroup(t_0,b_0).copy()

        b_all = Brace(Line3D(start=np.array([-3,0,0]),end=np.array([3,0,0])),direction=UP)
        t_all = Tex('\\begin{arabtex}\n6نق\n\\end{arabtex}',font_size=60).next_to(b_all,direction=UP)

        # Play animations
        self.play(Create(s_0))
        self.wait(2)
        
        self.play(Create(l_0),Write(t_0),Write(b_0))
        self.wait() 
        
        self.play(t_0_1.animate.shift(np.array([-1,0,0])))
        self.wait()
        
        self.play(Create(s_1),Create(s_2),run_time=0.5)
        self.play(Create(l_1),Create(l_2),run_time=0.5)
        self.play(t_1.animate.shift(np.array([1,0,0])),
                  t_1_1.animate.shift(np.array([2,0,0])),
                  t_2.animate.shift(np.array([-2,0,0])),
                  t_2_1.animate.shift(np.array([-3,0,0])),run_time=0.5)
        self.wait()
        # TODO, the remaining brace behind at [0.5,0,0] has to be removed
        # you have to think or find a way to make less redundant variables instead
        self.play(ReplacementTransform(Group(t_0,t_0_1,
                                              t_1,t_1_1,
                                              t_2,t_2_1),VGroup(b_all,t_all),
                                              replace_with_target_in_scene=True))
        self.wait()
        
        #self.play()
        #self.wait()
