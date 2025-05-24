from manim import *
import numpy as np

class GaussianWave3D(ThreeDScene):
    def construct(self):
        gamma = 0.2
        omega = 2.0
        t_min, t_max = -3, 3

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        axes = ThreeDAxes(
            x_range=[t_min, t_max, 1],
            y_range=[-1, 1, 0.5],
            z_range=[-1, 1, 0.5],
            x_length=6,
            y_length=6,
            z_length=6,
        )
        
        x_label = axes.get_x_axis_label(MathTex("t"))
        y_label = axes.get_y_axis_label(MathTex(r"\text{Re}\bigl(f_{\omega}(t)\bigr)"))
        z_label = axes.get_z_axis_label(MathTex(r"\text{Im}\bigl(f_{\omega}(t)\bigr)"))
        axis_labels = VGroup(x_label, y_label, z_label)

        def param_func(t):
            return np.array([
                t,
                np.exp(-gamma * t**2) * np.cos(omega * t),
                np.exp(-gamma * t**2) * np.sin(omega * t)
            ])

        spiral_3d = ParametricFunction(
            param_func,
            t_range=[t_min, t_max, 0.01],
            color=YELLOW,
            stroke_width=2
        ).set_shade_in_3d(True)

        real_curve = ParametricFunction(
            lambda t: np.array([
                t, np.exp(-gamma * t**2) * np.cos(omega * t), 0
            ]),
            t_range=[t_min, t_max, 0.01],
            color=BLUE,
            stroke_width=2
        )

        imag_curve = ParametricFunction(
            lambda t: np.array([
                t, 0, np.exp(-gamma * t**2) * np.sin(omega * t)
            ]),
            t_range=[t_min, t_max, 0.01],
            color=RED,
            stroke_width=2
        )

        modulus_curve = ParametricFunction(
            lambda t: np.array([
                t, np.exp(-gamma * t**2), np.exp(-gamma * t**2) * np.sign(np.sin(omega * t))
            ]),
            t_range=[t_min, t_max, 0.01],
            color=GREEN,
            stroke_width=2
        )
        
        formula = MathTex(r"f_{\omega}(t) = e^{-\gamma t^2} \cdot e^{i\omega t}").to_corner(UL).scale(0.7)
        
        self.add(axes, axis_labels)
        self.play(Create(spiral_3d), run_time=5)
        self.wait()
        self.play(Create(real_curve), Create(imag_curve), run_time=4)
        self.wait()
        self.play(Create(modulus_curve), run_time=4)
        self.wait()
        self.play(FadeIn(formula))
        self.wait(2)
        self.play(FadeOut(VGroup(*self.mobjects)))
        self.wait()
