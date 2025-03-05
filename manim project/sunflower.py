from manim import *
import numpy as np

class SunflowerPattern(Scene):
    def construct(self):
        num_layers = 8  # Số vòng của hoa văn
        num_petals = 12  # Số cánh hoa trên mỗi vòng
        radius_step = 0.3  # Khoảng cách giữa các vòng
        base_petal_size = 0.2  # Kích thước cơ bản của cánh hoa
        
        petals = VGroup()
        
        for layer in range(num_layers):
            for i in range(num_petals):
                angle = i * (TAU / num_petals) + (layer % 2) * (TAU / (2 * num_petals))  # Xoay lệch từng lớp
                radius = layer * radius_step + base_petal_size * (1 + (layer - 1) * 0.3) / 2  # Điều chỉnh vị trí để các lớp xen kẽ
                
                x = radius * np.cos(angle)
                y = radius * np.sin(angle)
                
                petal_size = base_petal_size * (1 + layer * 0.3)  # Cánh càng xa càng to
                petal = Triangle()
                petal.set_height(petal_size)
                petal.set_fill(WHITE, opacity=1)
                petal.set_stroke(BLACK, width=1)
                petal.move_to([x, y, 0])
                petal.rotate(angle)  # Xoay để tạo hiệu ứng cánh hoa hướng ra ngoài
                
                petals.add(petal)
        
        self.add(petals)
