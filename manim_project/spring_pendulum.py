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

class HorizontalSpringPendulum(Scene):
    def construct(self):
        # Thiết lập hệ tọa độ
        left_wall = LEFT * 3
        equilibrium = left_wall + RIGHT * 3.5  # Điều chỉnh vị trí cân bằng xa hơn
        omega = 1

        # Tính toán biên độ chính xác
        spring_min_length = 0.5
        mass_width = 0.8
        left_limit = left_wall[0] + spring_min_length + mass_width/2
        amplitude = equilibrium[0] - left_limit  # Biên độ tự nhiên

        # Tạo vật nặng
        mass = VGroup(
            Square(mass_width, color=BLUE, fill_opacity=0.5),
            Text("m", font_size=24).move_to(ORIGIN))
        mass.move_to(equilibrium)

        # Tạo lò xo
        spring = Spring(left_wall, mass.get_left(), num_coils=8, min_length=spring_min_length)

        # Tạo tường với sọc chéo dài tới mặt đất
        wall = VGroup(
            Line(left_wall + DOWN*0.5, left_wall + UP*1.5, color=GREY, stroke_width=12),  # Tường dài tới mặt đất
            *[Line(
                left_wall + DOWN*0.5 + UP*(0.2*i),
                left_wall + DOWN*0.5 + UP*(0.2*i) + LEFT*0.3 + UP*0.1,
                color=GREY,
                stroke_width=4)
              for i in range(11)]  # Thêm sọc cho toàn bộ chiều cao tường
        )

        # Tạo mặt đất dài hơn
        ground = VGroup(
            Line(left_wall + DOWN*0.5, left_wall + RIGHT*9 + DOWN*0.5,  # Mặt đất dài tới RIGHT*9
                 color=GREY, stroke_width=10),
            *[Line(
                left_wall + RIGHT*i*0.3 + DOWN*0.5,
                left_wall + RIGHT*(i*0.3 + 0.2) + DOWN*0.7,
                color=GREY,
                stroke_width=5)
              for i in range(30)]  # Tăng số sọc cho phù hợp
        )

        self.add(wall, ground, spring, mass)

        # Animation mượt mà
        time = ValueTracker(0)
        mass.add_updater(lambda m: m.set_x(
            equilibrium[0] + amplitude * np.cos(omega * time.get_value())
        ))
        spring.add_updater(lambda s: s.update_end(mass.get_left()))
        

        self.play(
            time.animate.set_value(4*PI),
            rate_func=linear,
            run_time=8
        )
        self.wait()