from manim import *
import numpy as np

class DampedPendulum(Scene):
    def construct(self):
        # Tham số hệ thống
        ceiling_y = 2  # Trần nhà thấp hơn
        length = 5     # Dây con lắc dài hơn
        g = 9.8
        omega = np.sqrt(g / length)
        damping_factor = 0.1  # Giảm damping để dao động kéo dài hơn
        initial_angle = 30 * DEGREES

        # Tạo trần nhà ngắn với sọc chéo phía trên
        ceiling_line = Line(LEFT * 2, RIGHT * 2, color=GREY, stroke_width=10).shift(UP * ceiling_y)
        num_stripes = 6
        ceiling_stripes = VGroup(*[
            Line(
                LEFT * 2 + RIGHT * ((i / num_stripes) * 4) + UP * ceiling_y,
                LEFT * 2 + RIGHT * ((i / num_stripes) * 4) + UP * ceiling_y + (RIGHT + UP) * 0.3,
                color=GREY, stroke_width=5
            )
            for i in range(num_stripes + 1)
        ])
        ceiling = VGroup(ceiling_line, ceiling_stripes)

        # Tạo con lắc
        pivot = UP * ceiling_y
        bob = Circle(0.3, color=BLUE, fill_opacity=0.8).move_to(pivot + DOWN * length)
        rod = Line(pivot, bob.get_center(), color=GREY_B)
        
        # Gom các đối tượng con lắc
        pendulum = VGroup(rod, bob)
        
        # Thêm nhãn
        mass_label = Text("m", font_size=24).next_to(bob, DOWN)

        self.add(ceiling, pendulum, mass_label)

        # Thiết lập chuyển động
        time = ValueTracker(0)
        bob.add_updater(lambda m: m.move_to(
            pivot + length * np.array([
                np.sin(initial_angle * np.exp(-damping_factor * time.get_value()) * np.cos(omega * time.get_value())),
                -np.cos(initial_angle * np.exp(-damping_factor * time.get_value()) * np.cos(omega * time.get_value())),
                0
            ])
        ))
        
        rod.add_updater(lambda r: r.become(
            Line(pivot, bob.get_center(), color=GREY_B)
        ))

        # Chạy animation: kéo dài thời gian để con lắc dao động lâu hơn
        self.play(
            time.animate.set_value(15),
            rate_func=linear,
            run_time=15
        )
        self.wait(2)
