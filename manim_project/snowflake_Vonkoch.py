from manim import *
import numpy as np

def koch_curve(points, order):
    if order == 0:
        return points
    
    new_points = []
    for i in range(len(points) - 1):
        p1, p2 = points[i], points[i + 1]
        delta = p2 - p1
        a, b = p1 + delta / 3, p1 + 2 * delta / 3
        
        # Xoay để tạo đỉnh tam giác đều
        angle = -np.pi / 3
        rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        rotated_vector = np.dot(rotation_matrix, delta[:2] / 3)
        peak = a + np.array([rotated_vector[0], rotated_vector[1], 0])
        
        new_points.extend([p1, a, peak, b])
    
    new_points.append(points[-1])
    return koch_curve(new_points, order - 1)

def create_triangle():
    side = 6
    height = side * np.sqrt(3) / 2
    return [
        np.array([-side/2, -height/3, 0]),
        np.array([side/2, -height/3, 0]),
        np.array([0, 2 * height/3, 0])
    ]

def koch_snowflake(order):
    triangle_points = create_triangle()
    triangle_points.append(triangle_points[0])  # Đóng kín tam giác
    new_points = []
    
    for i in range(len(triangle_points) - 1):
        seg = koch_curve([triangle_points[i], triangle_points[i + 1]], order)
        new_points.extend(seg if i == 0 else seg[1:])  # Tránh trùng điểm
    
    return new_points

def get_koch_mobject(order):
    points = koch_snowflake(order)
    mobject = VMobject()
    mobject.set_points_as_corners(points)
    mobject.set_stroke(WHITE, 2)
    mobject.set_fill(BLUE, opacity=1)  # Tô màu xanh dương
    return mobject

class VonKochSnowflakeOutward(Scene):
    def construct(self):
        orders = [0, 1, 2, 3, 4]
        snowflake = get_koch_mobject(orders[0])
        self.play(Create(snowflake))
        self.wait(1)
        
        for order in orders[1:]:
            new_snowflake = get_koch_mobject(order)
            self.play(Transform(snowflake, new_snowflake), run_time=2)
            self.wait(1)
