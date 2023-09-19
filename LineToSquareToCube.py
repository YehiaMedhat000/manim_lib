from manim import *

class LineToSquareToCube(ThreeDScene):
    def construct(self):

        # MathTex() mobjects        
        st_dim_l = Line(start=DL*2,end=UL*2,color=RED)
        st_dim_r = st_dim_l.copy()
        st_dim_br = Brace(st_dim_l,direction=LEFT)
        st_dim_tex = MathTex('4').next_to(st_dim_br,LEFT).scale(2)
        times = MathTex('\\times').scale(2)        

        # The square
        sq = always_redraw(lambda: 
             Polygon(st_dim_r.get_end(),st_dim_r.get_start(),st_dim_l.get_start(),st_dim_l.get_end(),
                     color=RED,fill_color=BLUE,fill_opacity=0.75,stroke_width=4))
        
        # Some arrows
        arr = Arrow(start=st_dim_l.get_top(),end=UR*2,color=RED,buff=0)
        arrs = [arr.copy().shift(DOWN*(i)) for i in range(5)]
        arr_br = Brace(arr[0],direction=UP)
        arr_br_tex = MathTex('4').next_to(arr_br,UP).scale(2)
        result = MathTex('16').scale(3)

        # Play animations
        self.add(sq)
        self.play(Create(st_dim_l))
        self.play(Write(st_dim_br),Write(st_dim_tex))
        self.wait()
        
        self.play(Write(arr_br_tex),Write(arr_br))
        for i in arrs:
            self.play(GrowArrow(i),run_time=0.5)
        
        self.wait(3)
 
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
        self.play(result.animate.to_corner(DOWN))
        self.add_fixed_in_frame_mobjects(result.to_corner(DOWN))
        
        # Initialize mobjects
        cube = always_redraw(lambda:Cube(side_length=4,color=BLUE,fill_opacity=1,stroke_width=4,stroke_color=RED)
                             .shift(np.array([0,0,2]))
                             .stretch_to_fit_depth(sq.get_center()[2],about_point=ORIGIN))
        
        arr_3d = Arrow3D(start=ORIGIN,end=np.array([0,0,4]),color=RED)

        rd_dim_br = (Brace(Line3D(start=[2,-2,0],end=[2,2,0]),direction=RIGHT))
        rd_dim_tex = (MathTex('4').scale(3).next_to(rd_dim_br))
        rd_dim = VGroup(rd_dim_br,rd_dim_tex).rotate(angle=PI/2,axis=X_AXIS,about_point=np.array([2,-2,0]))

        exp = MathTex('16 \\times 4 = 64').scale(2)

        # Set the camera settings
        self.set_camera_orientation(phi=0)
        self.move_camera(phi=60*DEGREES,theta=-45*DEGREES,focal_distance=20) 
        self.camera.set_zoom(0.75)
        #self.play(Write(result))
        self.wait()
        
        self.play(Create(arr_3d),run_time=0.2)
        self.play(Write(rd_dim))
        self.play(FadeOut(arr_3d))        
        self.wait()
        
        self.add(cube)
        self.play(st_dim_r.animate.move_to(np.array([-2,0,4])),
                  st_dim_l.animate.move_to(np.array([2,0,4])))
        
        self.add_fixed_in_frame_mobjects(exp)
        self.play(TransformMatchingTex(result,exp))     

        #self.begin_ambient_camera_rotation(rate=PI/9)
        self.wait(10)

        # Almost done
        # TODO: would like to pull the 16 from the square to let it be fixed_in_frame, then add
        # the other `times` and `MathTex('64')` mobjects. It will seem better this way