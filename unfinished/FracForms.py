from manim import *

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