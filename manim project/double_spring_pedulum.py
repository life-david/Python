from manim import *
import numpy as np

class Spring(ParametricFunction):
    def __init__(self, start, end, num_coils=10, min_length=0.5, **kwargs):
        self.num_coils = num_coils
        self.start = start
        self.end = end
        self.min_length = min_length
        super().__init__(self.spring_function, **kwargs)
        self.set_color(GREY_B)
        
    def spring_function(self, t):
        direction = self.end - self.start
        actual_distance = np.linalg.norm(direction)
        effective_distance = max(actual_distance, self.min_length)
        unit_vector = direction / actual_distance if actual_distance > 0 else RIGHT
        phase = 2 * PI * self.num_coils * t
        x = effective_distance * t
        y = 0.2 * np.sin(phase) * UP
        return self.start + x * unit_vector + y
    
    def update_end(self, new_end):
        self.end = new_end
        self.become(Spring(self.start, self.end, self.num_coils, min_length=self.min_length))

class DoubleSpringPendulum(Scene):
    def construct(self):
        left_wall = LEFT * 4
        right_wall = RIGHT * 4
        equilibrium = ORIGIN
        omega = 2
        damping_factor = 0.05
        
        spring_min_length = 0.5
        mass_width = 0.8
        amplitude = 2  # Biên độ ban đầu
        
        # Đặt vật nặng ban đầu lệch về bên phải để tạo hiệu ứng một bên dãn, bên còn lại nén
        mass = VGroup(
            Square(mass_width, color=BLUE, fill_opacity=0.5),
            Text("m", font_size=24).move_to(ORIGIN)
        )
        mass.move_to(equilibrium + RIGHT * amplitude)

        left_spring = Spring(left_wall, mass.get_left(), num_coils=8, min_length=spring_min_length)
        right_spring = Spring(right_wall, mass.get_right(), num_coils=8, min_length=spring_min_length)
        
        left_wall_lines = VGroup(
            Line(left_wall + DOWN*0.5, left_wall + UP*1.5, color=GREY, stroke_width=12),
            *[Line(
                left_wall + DOWN*0.5 + UP*(0.2*i),
                left_wall + DOWN*0.5 + UP*(0.2*i) + LEFT*0.3 + UP*0.1,
                color=GREY, stroke_width=4)
              for i in range(11)]
        )
        
        # Sửa phần tường bên phải: các sọc sẽ nằm bên phải
        right_wall_lines = VGroup(
            Line(right_wall + DOWN*0.5, right_wall + UP*1.5, color=GREY, stroke_width=12),
            *[Line(
                right_wall + DOWN*0.5 + UP*(0.2*i),
                right_wall + DOWN*0.5 + UP*(0.2*i) + RIGHT*0.3 + UP*0.1,
                color=GREY, stroke_width=4)
              for i in range(11)]
        )
        
        # Vẽ mặt đất với các sọc trải đều từ tường bên trái đến bên phải,
        # nhưng các sọc được vẽ dưới mặt đất với hướng chéo (45° xuống phải).
        ground_line = Line(left_wall + DOWN*0.5, right_wall + DOWN*0.5, color=GREY, stroke_width=10)
        num_stripes = 20
        ground_stripes = VGroup(*[
            Line(
                left_wall + RIGHT*( (i/num_stripes) * (right_wall[0] - left_wall[0])) + DOWN*0.5,
                left_wall + RIGHT*( (i/num_stripes) * (right_wall[0] - left_wall[0])) + DOWN*0.5 + (RIGHT + DOWN)*0.2,
                color=GREY, stroke_width=5
            )
            for i in range(num_stripes + 1)
        ])
        ground = VGroup(ground_line, ground_stripes)

        self.add(left_wall_lines, right_wall_lines, ground, left_spring, right_spring, mass)

        # Dùng ValueTracker để điều khiển hiệu ứng dao động tắt dần
        time = ValueTracker(0)
        mass.add_updater(lambda m: m.set_x(
            equilibrium[0] + amplitude * np.exp(-damping_factor * time.get_value()) * np.cos(omega * time.get_value())
        ))
        left_spring.add_updater(lambda s: s.update_end(mass.get_left()))
        right_spring.add_updater(lambda s: s.update_end(mass.get_right()))

        self.play(
            time.animate.set_value(10 * PI),
            rate_func=linear,
            run_time=10
        )
        self.wait()
