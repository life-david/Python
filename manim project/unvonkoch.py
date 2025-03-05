from manim import *
import numpy as np

def koch_curve(points, order):
    """
    Hàm đệ quy tạo các điểm theo quy tắc Koch.
    points: danh sách các điểm (np.array) của đoạn thẳng.
    order: số lần lặp quy tắc.
    """
    if order == 0:
        return points
    
    new_points = []
    for i in range(len(points) - 1):
        p1 = points[i]
        p2 = points[i + 1]
        delta = p2 - p1
        
        # Chia đoạn thẳng thành 3 phần
        a = p1 + delta / 3
        b = p1 + 2 * delta / 3
        
        # Tính điểm "đỉnh" của tam giác đều lồi ra
        angle = np.pi / 3  # 60 độ
        rotation_matrix = np.array([
            [np.cos(angle), -np.sin(angle)],
            [np.sin(angle),  np.cos(angle)]
        ])
        rotated_vector = np.dot(rotation_matrix, (delta[:2] / 3))
        peak = p1 + np.array([rotated_vector[0], rotated_vector[1], 0]) + delta / 3
        
        # Thêm các điểm mới vào danh sách
        new_points.extend([p1, a, peak, b])
    
    new_points.append(points[-1])  # Thêm điểm cuối cùng
    return koch_curve(new_points, order - 1)

def create_triangle():
    """
    Tạo 3 đỉnh của tam giác đều với cạnh có độ dài nhất định.
    """
    side = 6
    height = side * np.sqrt(3) / 2
    p1 = np.array([-side/2, -height/3, 0])
    p2 = np.array([side/2, -height/3, 0])
    p3 = np.array([0, 2 * height/3, 0])
    return [p1, p2, p3]

def koch_snowflake(order):
    """
    Tạo dãy điểm của bông tuyết Koch bằng cách áp dụng quy tắc Koch cho từng cạnh của tam giác.
    """
    triangle_points = create_triangle()
    # Đóng hình tam giác lại thành đường viền kín
    triangle_points.append(triangle_points[0])
    new_points = []
    for i in range(len(triangle_points) - 1):
        seg = [triangle_points[i], triangle_points[i + 1]]
        seg = koch_curve(seg, order)
        if i == 0:
            new_points = seg
        else:
            new_points.extend(seg[1:])  # Tránh trùng lặp điểm cuối của đoạn trước
    return new_points

def get_koch_mobject(order):
    """
    Tạo VMobject từ dãy điểm của bông tuyết Koch.
    """
    points = koch_snowflake(order)
    mobject = VMobject()
    mobject.set_points_as_corners(points)
    return mobject

class VonKochSnowflake(Scene):
    def construct(self):
        # Danh sách các mức độ (order) của bông tuyết
        orders = [0, 1, 2, 3, 4]
        
        # Bắt đầu với tam giác đều (order 0)
        snowflake = get_koch_mobject(orders[0])
        snowflake.set_stroke(WHITE, 2)
        self.play(Create(snowflake))
        self.wait(1)
        
        # Biến đổi dần qua các mức order tăng dần
        for order in orders[1:]:
            new_snowflake = get_koch_mobject(order)
            new_snowflake.set_stroke(WHITE, 2)
            self.play(Transform(snowflake, new_snowflake), run_time=2)
            self.wait(1)