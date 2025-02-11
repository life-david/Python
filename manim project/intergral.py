from manim import *
from manim.mobject.three_d.three_dimensions import Arrow3D

class LineIntegralType1(Scene):
    def construct(self):
        # Tạo đường cong và công thức
        curve = ParametricFunction(
            lambda t: np.array([t, t**2, 0]),
            t_range=[-2, 2],
            color=BLUE
        ).set_stroke(width=5)
        
        formula = MathTex(r"\int_C f(x,y) \, ds").to_edge(UP)
        
        # Hiệu ứng animation
        self.play(Create(curve), run_time=2)
        self.play(Write(formula))
        self.wait(2)

class LineIntegralType2(Scene):
    def construct(self):
        # Tạo trường vector và đường cong
        func = lambda p: np.array([-p[1], p[0], 0])
        vector_field = VectorField(func, x_range=[-3,3], y_range=[-3,3])
        
        curve = ParametricFunction(
            lambda t: np.array([2*np.cos(t), 2*np.sin(t), 0]),
            t_range=[0, 2*PI],
            color=RED
        ).set_stroke(width=5)
        
        formula = MathTex(r"\int_C \mathbf{F} \cdot d\mathbf{r}").to_edge(UP)
        
        # Hiệu ứng animation
        self.play(Create(vector_field), run_time=2)
        self.play(Create(curve))
        self.play(Write(formula))
        self.wait(2)

class SurfaceIntegralType1(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
        
        # Tạo bề mặt 3D
        surface = Surface(
            lambda u, v: np.array([u, v, np.sin(u) * np.cos(v)]),
            u_range=[-PI, PI],
            v_range=[-PI/2, PI/2],
            fill_opacity=0.7,
            checkerboard_colors=[BLUE_D, BLUE_E],
        )
        
        formula = MathTex(r"\iint_S f(x,y,z) \, dS").to_corner(UL)
        
        # Hiệu ứng animation
        self.play(Create(surface), run_time=3)
        self.add_fixed_in_frame_mobjects(formula)
        self.play(Write(formula))
        self.wait(2)

class SurfaceIntegralType2(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
        
        # Tạo bề mặt phẳng và vector
        surface = Surface(
            lambda u, v: np.array([u, v, 0]),
            u_range=[-2, 2],
            v_range=[-2, 2],
            fill_opacity=0.5,
            color=GREEN
        )
        
        # Tạo các vector 3D
        vectors = VGroup()
        for x in np.linspace(-2, 2, 4):
            for y in np.linspace(-2, 2, 4):
                arrow = Arrow3D(
                    start=np.array([x, y, 0]),
                    end=np.array([x, y, 1]),
                    color=YELLOW
                )
                vectors.add(arrow)
        
        formula = MathTex(r"\iint_S \mathbf{F} \cdot d\mathbf{S}").to_corner(UL)
        
        # Hiệu ứng animation
        self.play(Create(surface), run_time=2)
        self.play(Create(vectors), run_time=2)
        self.add_fixed_in_frame_mobjects(formula)
        self.play(Write(formula))
        self.wait(2)