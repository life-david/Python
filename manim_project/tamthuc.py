from manim import *

class PhanTich_TamThucBacHai(Scene):
    def construct(self):

        self.camera.background_color = BLACK#"ece6e2"

        text_1="4 t^{2} - 8 t - 21"
        text_2="\\left(\\left(2 t\\right)^2-2\\cdot 2 t\\cdot 2+2^2\\right)-2^2-21"
        text_3="\\left(2 t - 2\\right)^2-25"
        text_4="\\left(2 t - 2\\right)^2-5^2"
        text_5="\\left(2 t - 2 - 5\\right)\\left(2 t - 2 + 5\\right)"
        text_6="\\left(2 t - 7\\right)\\left(2 t + 3\\right)"
        a1 = MathTex('%s'%text_1).scale(2)
        a2 = MathTex('%s'%text_2).scale(2)
        a3 = MathTex('%s'%text_3).scale(2)
        a4 = MathTex('%s'%text_4).scale(2)
        a5 = MathTex('%s'%text_5).scale(2)
        a6 = MathTex('%s'%text_6).scale(2)
        text = Tex("factorize a trinomial").scale(2)
        self.play(Write(text))
        #self.play(Transform(text, a1))
        self.play(FadeOut(text))
        self.play(Write(a1))
        for v in (a1,a2,a3,a4,a5,a6):
            self.play(Transform(a1, v), run_time =3)
        self.wait(1)
        
        logo = VGroup(a1,a2,a3,a4,a5,text) #order matters
        hello = Tex("HELLO WORLD").scale(2)
        xinchao = Tex("I am DO VAN DAT").scale(2)
        pythonme = Tex("Let's learn python with me").scale(2)
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)

        self.play(Transform(logo, hello))
        self.play(FadeOut(logo))
        #self.play(ShowCreation(hello))
        self.play(Transform(hello, xinchao))
        self.play(FadeOut(hello))
        #self.play(ShowCreation(xinchao))
        self.play(Transform(xinchao, pythonme))
        self.play(FadeOut(xinchao))
        #self.play(ShowCreation(pythonme))
        self.play(Transform(pythonme,square))
        #self.play(ShowCreation(square))
        self.play(Transform(square,text))
        