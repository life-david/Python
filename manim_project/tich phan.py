from manim import *

class IntegrationByParts(Scene):
    def construct(self):
        # Initial integral
        int_eq = MathTex(r"\int x^{2}e^{x} \, dx").scale(1.5)
        
        # Integration by parts formula
        ibp_formula = MathTex(r"\int x^{2}e^{x} \, dx = u\,v - \int v\, du").scale(1.5).to_edge(UP)
        
        # Highlight parts of the formula
        ibp_formula[0][8:9].set_color(BLUE)      # u
        ibp_formula[0][9:10].set_color(ORANGE)   # v
        ibp_formula[0][12:13].set_color(ORANGE)  # v
        ibp_formula[0][13:15].set_color(BLUE)    # du
        
        # After substitution
        after_sub = MathTex(r"\int x^{2}e^{x} \, dx = x^{2}e^{x} -\int 2xe^{x} \, dx").scale(1.5).to_edge(UP)
        
        # Highlight parts after substitution
        after_sub[0][8:10].set_color(BLUE)       # x^2
        after_sub[0][10:12].set_color(ORANGE)    # e^x
        after_sub[0][14:16].set_color(BLUE)      # 2x
        after_sub[0][16:18].set_color(ORANGE)    # e^x
        
        # Define u and du/dx
        u_title = MathTex(r"\text{Let }").scale(1.33)
        u_eq = MathTex(r"u = x^2").scale(1.5)
        u_eq[0][0:1].set_color(BLUE)
        
        du_dx = MathTex(r"\frac{du}{dx}=2x").scale(1.5)
        du = MathTex(r"du=2x\,dx").scale(1.5)
        du[0][0:2].set_color(BLUE)
        
        u_group = VGroup(u_title, u_eq, du_dx).arrange(DOWN, buff=0.5).to_edge(LEFT, buff=1)
        
        # Define dv and v
        v_title = MathTex(r"\text{And }").scale(1.33)
        dv_eq = MathTex(r"dv = e^{x}\, dx").scale(1.5)
        
        int_dv = MathTex(r"\int dv = \int e^{x}\, dx").scale(1.5)
        v_eq = MathTex(r"v = e^{x}").scale(1.5)
        v_eq[0][0:1].set_color(ORANGE)
        
        v_group = VGroup(v_title, dv_eq).arrange(DOWN, buff=0.5).to_edge(RIGHT, buff=1)
        
        # Steps of solution
        step1 = MathTex(r"\int x^{2}e^{x} \, dx = x^{2}e^{x} -2\int xe^{x} \, dx").scale(1.5)
        step2 = MathTex(r"\int x^{2}e^{x} \, dx = x^{2}e^{x}-2(xe^{x} - \int e^x \, dx) + C").scale(1.5)
        step3 = MathTex(r"\int x^{2}e^{x} \, dx = x^{2}e^{x}-2xe^{x} + 2e^x + C").scale(1.5)
        step4 = MathTex(r"\int x^{2}e^{x} \, dx = e^x(x^{2}-2x+2) + C").scale(1.5)
        
        # Animations
        self.play(Write(int_eq))
        self.wait()
        
        self.play(ReplacementTransform(int_eq, ibp_formula))
        self.wait()
        
        self.play(
            FadeIn(u_title), 
            FadeIn(v_title)
        )
        self.wait()
        
        self.play(
            TransformFromCopy(ibp_formula[0][8:9], u_eq[0][0:1]),
            Write(u_eq[0][1:])
        )
        self.wait()
        
        self.play(
            TransformFromCopy(int_eq[0][1:3], u_eq[0][2:]),
        )
        self.wait()
        
        self.play(
            Write(dv_eq)
        )
        self.wait()
        
        self.play(
            TransformFromCopy(int_eq[0][3:6], dv_eq[0][3:]),
        )
        self.wait()
        
        # Show differentiation of u
        self.play(
            Write(du_dx)
        )
        self.wait()
        
        self.play(
            ReplacementTransform(du_dx, du)
        )
        self.wait()
        
        # Show integration of dv
        int_dv.next_to(dv_eq, DOWN, buff=0.5)
        self.play(
            Write(int_dv)
        )
        self.wait()
        
        self.play(
            ReplacementTransform(int_dv, v_eq)
        )
        self.wait()
        
        # Transform to substituted form
        self.play(
            ReplacementTransform(ibp_formula, after_sub),
            FadeOut(u_title, u_eq, du, v_title, dv_eq, v_eq)
        )
        self.wait()
        
        # Show solution steps
        self.play(
            ReplacementTransform(after_sub, step1)
        )
        self.wait()
        
        self.play(
            ReplacementTransform(step1, step2)
        )
        self.wait()
        
        self.play(
            ReplacementTransform(step2, step3)
        )
        self.wait()
        
        self.play(
            ReplacementTransform(step3, step4)
        )
        self.wait(2)
        
        # Final message
        final_message = Text("Integration by parts completed!")
        self.play(
            FadeOut(step4),
            Write(final_message)
        )
        self.wait(2)