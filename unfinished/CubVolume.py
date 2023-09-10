from manim import *

class CubeVolume(ThreeDScene):
    def construct(self):
        
        # Set the camera initial position
        self.set_camera_orientation(phi=0)

        # Initialize the mobjects
        # TODO, keep track of the numbers so they always show up clearly on the screen.
        axes = ThreeDAxes(x_length=12,y_length=10,z_length=8)

        st_dim_l = Line(start=DL*2,end=UL*2,color=RED)
        st_dim_r = st_dim_l.copy()
        st_dim_br = Brace(st_dim_l,direction=LEFT)

        st_dim_tex = MathTex('4').next_to(st_dim_br,LEFT).scale(2)
        
        times = MathTex('\\times').scale(2)        

        sq = always_redraw(lambda: 
             Polygon(st_dim_r.get_end(),st_dim_r.get_start(),st_dim_l.get_start(),st_dim_l.get_end(),
                     color=RED,fill_color=BLUE,fill_opacity=0.75,stroke_width=4))
        
        arr = Arrow(start=st_dim_l.get_top(),end=UR*2,color=RED)
        arr_br = Brace(arr,direction=UP)
        arrs = [arr.copy().shift(DOWN*(i+1)) for i in range(4)]
        
        arr_br_tex = MathTex('4').next_to(arr_br,UP).scale(2)

        result = MathTex('16').scale(2.5)

        cube = always_redraw(lambda:Cube(side_length=4,color=BLUE,fill_opacity=1,stroke_width=4,stroke_color=RED)
                             .shift(np.array([0,0,2]))
                             .stretch_to_fit_depth(sq.get_center()[2],about_point=axes.c2p(0,0,0)))
        
        rd_0_arr_dim = Arrow3D(start=np.array([2,-2,0]),end=np.array([2,-2,4]),color=RED)
        rd_1_arr_dim = rd_0_arr_dim.copy().move_to(np.array([2,2,2]))
        rd_2_arr_dim = rd_0_arr_dim.copy().move_to(np.array([-2,2,2]))
        rd_3_arr_dim = rd_0_arr_dim.copy().move_to(np.array([-2,-2,2]))

        arrs_3d = [rd_0_arr_dim,rd_1_arr_dim,rd_2_arr_dim,rd_3_arr_dim]

        rd_dim_br = (Brace(Line3D(start=[2,-2,0],end=[2,2,0]),direction=RIGHT))
        rd_dim_tex = (MathTex('4').scale(2.5).next_to(rd_dim_br))
    
        rd_dim = VGroup(rd_dim_br,rd_dim_tex).rotate(angle=PI/2,axis=X_AXIS,about_point=np.array([2,-2,0]))

        result_3d = MathTex('64').scale(2)
        grp_3d = VGroup(result_3d,times,result).to_corner(DOWN)
        grp_3d.arrange()

        # Play animations
        self.add(sq)
        self.play(Create(st_dim_l))
        self.play(Write(st_dim_br),Write(st_dim_tex))
        self.wait()
        self.play(GrowArrow(arr),run_time=0.5)
        self.play(Write(arr_br_tex),Write(arr_br))
        
        for i in arrs:
            self.play(GrowArrow(i),run_time=0.5)
        
        self.wait(3)
        self.play(FadeOut(arr),run_time=0.25)
        
        for i in arrs:
            self.play(FadeOut(i),run_time=0.25)

        self.wait(3)
        self.play(st_dim_l.animate.move_to(np.array([2,0,0])))
        self.wait()
        self.play(Write(times.set_color(RED)),
                  st_dim_tex.animate.next_to(times,LEFT),
                  arr_br_tex.animate.next_to(times,RIGHT))
        self.wait()
        self.play(ReplacementTransform(VGroup(st_dim_tex,arr_br_tex,times),result))
        self.play(FadeOut(st_dim_br,st_dim_tex,arr_br_tex,arr_br))
        
        self.move_camera(phi=60*DEGREES,theta=-45*DEGREES,
                         focal_distance=20)
        
        self.remove(result)

        self.camera.set_zoom(0.75)
        self.wait()
        
        for arr in arrs_3d:
            self.play(Create(arr),run_time=0.2)
        
        self.play(Write(rd_dim))
        
        for arr in arrs_3d:
            self.play(FadeOut(arr))
        

        self.wait()
        self.add(cube)
        
        self.add_fixed_in_frame_mobjects(grp_3d)

        self.play(st_dim_r.animate.move_to(np.array([-2,0,4])),
                  st_dim_l.animate.move_to(np.array([2,0,4])))

        self.play(Write(grp_3d))        
        self.begin_ambient_camera_rotation(rate=PI/9)
        self.wait(5)
        # TODO, not completed; needs more clarifications with LaTeX and formulae.