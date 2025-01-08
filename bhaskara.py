from manim import *

class BhaskaraProof(Scene):
    def construct(self):
        title = MathTex(r'\text{Demonstração Canônica}', font_size = 50, color = YELLOW)
        title.shift(0.5 * UP)
        self.play(Write(title))

        subtitle = MathTex(r'\text{Fórmula de Bhaskara}', font_size = 40, color = BLUE)
        subtitle.next_to(title, DOWN, buff = 0.75)
        self.play(Write(subtitle))
        self.wait()

        self.play(FadeOut(title), FadeOut(subtitle))

        def equations_sequence(initial, equations):
            self.play(Write(initial))
            self.wait()
            for step in equations:
                if step == equations[0]:
                    current_step = equations[0]
                    self.play(ReplacementTransform(initial, equations[0]))
                    self.wait()
                else:
                    self.play(ReplacementTransform(current_step, step))
                    self.wait()
                    current_step = step
            self.play(Circumscribe(equations[-1]), buff = 1.5)

        equation = MathTex(r'ax^2 + bx + c = 0')
        step1 = MathTex(r'ax^2 + bx  =  -c')
        step2 = MathTex(r'x^2 + \frac{b}{a}x  = -\frac{c}{a}')
        step3 = MathTex(r'x^2 + \frac{b}{a}x + \frac{b^2}{4a^2} = -\frac{c}{a} + \frac{b^2}{4a^2}')
        step4 = MathTex(r'\left(x + \frac{b}{2a} \right)^2 = - \frac{4ac}{4a^2} + \frac{b^2}{4a^2}')
        step5 = MathTex(r'x + \frac{b}{2a} = \pm \frac{\sqrt{b^2 - 4ac}}{2a}')
        step6 = MathTex(r'x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}')

        equations = [step1, step2, step3, step4, step5, step6]

        equations_sequence(equation, equations)

        self.play(FadeOut(step6))