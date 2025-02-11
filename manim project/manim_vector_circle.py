from manim import *
import numpy as np

class PlotPoints(Scene):
    def construct(self):
        # Tạo lưới tọa độ
        grid = NumberPlane()
        self.add(grid)
        
        # Vẽ điểm tâm (0,0) và nhãn của nó
        center_dot = Dot(ORIGIN, color=WHITE)
        center_label = MathTex("(0, 0)").next_to(center_dot, DOWN, buff=0.1)
        self.add(center_dot, center_label)
        
        # Khởi tạo mũi tên nối từ (0,0) đến (2,2) nhưng chưa add vào cảnh ngay
        arrow = Arrow(ORIGIN, [2, 2, 0], buff=0, stroke_width=8, color=WHITE)
        # Khởi tạo điểm (2,2) và nhãn của nó (cố định)
        fixed_dot = Dot([2, 2, 0], color=RED)
        fixed_label = MathTex("(2, 2)").next_to(fixed_dot, UR, buff=0.1)
        
        # Animation: Xuất hiện dần mũi tên
        self.play(Create(arrow), run_time=2)
        self.wait(0.5)
        
        # Animation: Xuất hiện dần điểm (2,2) và nhãn của nó
        self.play(FadeIn(fixed_dot), Write(fixed_label), run_time=2)
        self.wait(0.5)
        
        # Tạo traced path cho đầu mũi tên khi quay (với nét dày, màu đỏ)
        traced_path = TracedPath(arrow.get_end, stroke_color=RED, stroke_width=8)
        self.add(traced_path)
        
        # Animation: Quay mũi tên 360° quanh tâm (0,0)
        self.play(
            Rotate(arrow, angle=TAU, about_point=ORIGIN, run_time=4, rate_func=linear)
        )
        self.wait(2)

if __name__ == "__main__":
    from manim_vector_circle import config
    config.pixel_width = 1920
    config.pixel_height = 1080
    config.frame_rate = 60
    scene = PlotPoints()
    scene.render()
