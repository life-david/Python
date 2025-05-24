from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_rate = 60

class Sphere3D(ThreeDScene):
    def construct (self):

        title = Text("Volume of a Sphere", font_size=48, color=WHITE).to_edge(UP)

        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        r = 3
        theta = PI/4
        phi = PI/2

        axes = ThreeDAxes(z_range=[-6,6,1], z_length=10.5).rotate(-PI/4, axis = UP)
        spher = Sphere(radius=r).rotate(PI/2, axis = RIGHT)
        spher.set_fill(WHITE, opacity=0.4)

        self.play(Create(spher), Create(axes), run_time = 2)
        self.wait(.5)

        displ = MathTex("Infinites displacement in spherical coordinates", font_size=36).move_to(UP*7)
        math_dis= MathTex(r"\vec{dl} = \begin{pmatrix} dr \\ r d\theta \\ r \sin\theta d\phi \end{pmatrix}").next_to(displ, DOWN)

        self.play(Write(displ), Write(math_dis),spher.animate.move_to(DOWN*4), axes.animate.move_to(DOWN*4))
        self.wait(.7)

        vol = Text("Volume of a Sphere", font_size=36).move_to(UP*7)
        inte = MathTex(r"V_(sphere) = \iiint_V dV").next_to(vol, DOWN*4)
        math_dis2 = MathTex(r"dV = r^2dr sin\theta d\theta d\phi").next_to(vol, DOWN*4)
        
        self.play(Transform(math_dis, inte), Transform(displ, vol))
        self.wait(.5)

        self.play(Transform(math_dis, math_dis2))
        self.wait(.5)

        variation = Tex("Variation of each spherical coordinate: ", font_size = 36).move_to(UP*7)

        limit2 = MathTex(r"\begin{cases} r \in \left[0 ,R \right] \\ \theta \in \left[0 ,\pi \right] \end{cases}").next_to(variation, DOWN*4)
        limit3 = MathTex(r"\begin{cases} r \in \left[0 ,R \right] \\ \theta \in \left[0 ,\pi \right] \\ \phi \in \left[0 ,2\pi \right] \end{cases}").next_to(variation, DOWN*4) 

        axes2D = Axes(x_range=[-5,5,1], y_range=[-5,5,1], axis_config={"color": WHITE}, y_length=10).move_to(DOWN*4)

        xvec = Circle(radius=0.5, color=WHITE).shift(RIGHT*5)
        point_x = Dot3D(point=xvec.get_center(), color=WHITE, radius=0.1)

        x_label = MathTex(r"\vec{x}", color=WHITE, font_size=72).next_to(xvec, DOWN*1)
        y_label = MathTex(r"\vec{y}", color=WHITE, font_size=72).next_to(axes2D.x_axis.get_end(), RIGHT*1)
        z_label = MathTex(r"\vec{z}", color=WHITE, font_size=72).next_to(axes2D.y_axis.get_end(), UP*1)

        origin = axes.c2p(0,0)
        direction = np.array([1,1,0]) / np.sqrt(2)

        norm_tracker = ValueTracker(0)
        r_tracker = ValueTracker(0)

        moving_dot2 = always_redraw(lambda: Dot(point=direction *r_tracker.get_value()+ DOWN*4, color=ORANGE))
        moving_dot = always_redraw(lambda: Dot(point=direction * norm_tracker.get_value()+DOWN*4, color=ORANGE))
        trail_line = always_redraw(lambda: Line(origin, moving_dot.get_center(), color=ORANGE))
        r_val = always_redraw(lambda: MathTex(r"r = %.2f" % r_tracker.get_value(), color=WHITE, font_size = 56).next_to(moving_dot, DOWN*1))

        self.play(Transform(displ, variation), FadeOut(math_dis), Uncreate(spher), Transform(axes, axes2D),
                  Write(x_label), Write(y_label), Write(z_label), Write(point_x), Write(xvec))
        self.add(moving_dot, trail_line, moving_dot2, r_val)
        self.play(norm_tracker.animate.set_value(4), r_tracker.animate.set_value(4), run_time=3, rate_func = smooth)
        self.play(r_tracker.animate.set_value(1), run_time=1, rate_func=smooth)
        self.play(r_tracker.animate.set_value(4), run_time=1, rate_func=smooth)

        self.wait(.2)

        static_r_val = r_val.copy()

        self.remove(r_val)
        self.add(static_r_val)
        self.play(Transform(static_r_val, limit3))

        def create_angle(tracker, origin, phi=False):
            line_length = 3

            if not phi:  # Góc theta
                rotating_line = always_redraw(lambda: Line(
                    start=origin,
                    end=origin + line_length * np.array([
                        np.sin(tracker.get_value()), np.cos(tracker.get_value()), 0
                    ]),
                    color=ORANGE  # Đường thẳng màu cam
                ))

                arc = always_redraw(lambda: Arc(
                    radius=1,
                    start_angle=PI/2,
                    angle=-tracker.get_value(),  # Quay theo chiều kim đồng hồ
                    color=ORANGE,
                    arc_center=origin
                ))

                label = always_redraw(lambda: MathTex(
                    "\\theta = %d^{{o}}" % (180 / PI * tracker.get_value()),
                    color=WHITE,
                    font_size=56
                ).next_to(arc.get_end() + RIGHT))

                return VGroup(rotating_line, arc, label)

            else:  # Góc phi
                rotating_line = always_redraw(lambda: Line(
                    start=origin,
                    end=origin + line_length * np.array([
                        np.cos(tracker.get_value()), np.sin(tracker.get_value()), 0
                    ]),
                    color=ORANGE
                ))

                arc = always_redraw(lambda: Arc(
                    radius=1,
                    start_angle=0,
                    angle=tracker.get_value(),  # Quay ngược chiều kim đồng hồ
                    color=ORANGE,
                    arc_center=origin
                ))

                label = always_redraw(lambda: MathTex(
                    "\\phi = %d^{{o}}" % (180 / PI * tracker.get_value()),
                    color=WHITE,
                    font_size=56
                ).next_to(arc.get_end() + RIGHT))

                return VGroup(rotating_line, arc, label)
            
        z_label_phi = MathTex(r"\vec{z}", color=WHITE, font_size=72).next_to(xvec, DOWN*1)
        x_label_phi = MathTex(r"\vec{x}", color=WHITE, font_size=72).next_to(axes2D.x_axis.get_end(), RIGHT*1)
        y_label_phi = MathTex(r"\vec{y}", color=WHITE, font_size=72).next_to(axes2D.y_axis.get_end(), UP*1)

        self.play(FadeOut(trail_line), FadeOut(moving_dot), FadeOut(moving_dot2))

        theta = ValueTracker(0)

        lig = Line(start=origin, end=origin + 3*UP, color=ORANGE)
        angle_arc = create_angle(theta, origin)

        self.play(FadeIn(angle_arc), FadeIn(lig))
        self.play(theta.animate.set_value(PI), run_time=3, rate_func = linear)

        theta_static = angle_arc[2].copy()

        self.remove (angle_arc[2])
        self.add(theta_static)
        self.wait(.2)

        group = VGroup(static_r_val, theta_static)

        self.play(Transform(group, limit2), FadeOut(lig), FadeOut(angle_arc[:-1]))
        self.wait(.5)

        phi = ValueTracker(0)

        lig2 = Line(start=origin, end=origin + 3*RIGHT, color=ORANGE)

        angle_arc2 = create_angle(phi, origin, True)

        self.play(FadeIn(angle_arc2), FadeIn(lig2), Transform(x_label, z_label_phi), Transform(y_label, x_label_phi), Transform(z_label, y_label_phi))
        self.play(phi.animate.set_value(2*PI), run_time=3, rate_func = linear)

        phi_static = angle_arc2[2].copy()

        self.remove (angle_arc2[2])
        self.add(phi_static)
        self.wait(.2)

        group2 = VGroup(group, phi_static)

        self.wait(.1)
        self.play(Transform(group2, limit3), FadeOut(lig2), FadeOut(angle_arc2[:-1]))
        self.wait(.5)

        inte2 = MathTex(r"V_{sphere} = \int_0^R r^2dr \int_0^\pi \sin(\theta)d\theta \int_0^{2\pi} d\phi").move_to(ORIGIN)
        inte3 = MathTex(r"V_{sphere} = \left[\frac{r^3}{3}\right]_0^R \left[-\cos(\theta)\right]_0^{\pi} \left[\phi\right]_0^{2\pi}").move_to(ORIGIN)
        inte4 = MathTex(r"V_{sphere} = \frac{2\pi}{3}R^3\left[-\cos(0)\right]").move_to(ORIGIN)
        inte5 = MathTex(r"V_{sphere} = \frac{4\pi}{3}R^3").move_to(ORIGIN)

        frame = SurroundingRectangle(inte5, color=PURE_RED, buff=0.2)

        self.play(FadeOut(axes), FadeOut(group2), FadeOut(x_label), FadeOut(y_label), FadeOut(z_label), FadeOut(xvec),
                  FadeOut(point_x), Transform(displ, inte2), run_time=1.3)
        
        self.play(Transform(displ, inte3))
        self.wait(.5)
        self.play(Transform(displ, inte4))
        self.wait(.3)
        self.play(Transform(displ, inte5), run_time =1)
        self.play(Create(frame))
        self.wait(.4)


