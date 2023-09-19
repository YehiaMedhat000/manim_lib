from manim import *

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
