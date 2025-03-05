from manim import *
import numpy as np
from PIL import Image

# Định nghĩa lớp Maze và Node giống như code của bạn, nhưng tối ưu cho ManimCE
class Maze:
    class Node:
        def __init__(self, position):
            self.position = position  # (y, x)
            self.neighbours = [None, None, None, None]  # [up, right, down, left]

    def __init__(self, image_path):
        # Mở và xử lý hình ảnh
        im = Image.open(image_path).convert('L')  # Chuyển sang ảnh xám
        width, height = im.size
        
        # Chuyển dữ liệu pixel thành mảng numpy
        data = np.array(im).flatten() > 128  # Ngưỡng để phân biệt đường đi (True) và tường (False)

        self.start = None
        self.end = None
        self.nodes = []  # Lưu tất cả các node
        self.width = width
        self.height = height

        # Buffer cho hàng trên
        top_nodes = [None] * width
        node_count = 0

        # Xử lý hàng đầu tiên
        for x in range(1, width - 1):
            if data[x]:
                self.start = self.Node((0, x))
                top_nodes[x] = self.start
                self.nodes.append(self.start)
                node_count += 1
                break

        # Xử lý các hàng còn lại
        for y in range(1, height - 1):
            row_offset = y * width
            row_above_offset = row_offset - width
            row_below_offset = row_offset + width

            prev = False
            curr = False
            next_val = data[row_offset + 1]

            left_node = None

            for x in range(1, width - 1):
                prev = curr
                curr = next_val
                next_val = data[row_offset + x + 1]

                node = None

                if not curr:
                    continue

                if prev:
                    if next_val:
                        if data[row_above_offset + x] or data[row_below_offset + x]:
                            node = self.Node((y, x))
                            if left_node:
                                left_node.neighbours[1] = node
                                node.neighbours[3] = left_node
                            left_node = node
                    else:
                        node = self.Node((y, x))
                        if left_node:
                            left_node.neighbours[1] = node
                            node.neighbours[3] = left_node
                        left_node = None
                else:
                    if next_val:
                        node = self.Node((y, x))
                        left_node = node
                    else:
                        if not (data[row_above_offset + x] or data[row_below_offset + x]):
                            node = self.Node((y, x))

                if node:
                    if data[row_above_offset + x]:
                        top_node = top_nodes[x]
                        if top_node:
                            top_node.neighbours[2] = node
                            node.neighbours[0] = top_node

                    if data[row_below_offset + x]:
                        top_nodes[x] = node
                    else:
                        top_nodes[x] = None

                    self.nodes.append(node)
                    node_count += 1

        # Xử lý hàng cuối cùng
        row_offset = (height - 1) * width
        for x in range(1, width - 1):
            if data[row_offset + x]:
                self.end = self.Node((height - 1, x))
                top_node = top_nodes[x]
                if top_node:
                    top_node.neighbours[2] = self.end
                    self.end.neighbours[0] = top_node
                self.nodes.append(self.end)
                node_count += 1
                break

        self.count = node_count

    def find_path(self):
        if not self.start or not self.end:
            return []

        from collections import deque
        queue = deque([(self.start, [self.start])])
        visited = {self.start}

        while queue:
            current_node, path = queue.popleft()
            if current_node == self.end:
                return path

            for next_node in current_node.neighbours:
                if next_node and next_node not in visited:
                    visited.add(next_node)
                    queue.append((next_node, path + [next_node]))

        return []

# Lớp ManimCE để tạo animation mê cung
class QuantumMazeAnimation(Scene):
    def construct(self):
        # Tạo mê cung từ hình ảnh
        maze = Maze('quantum_search.png')  # Thay bằng đường dẫn hình ảnh của bạn
        path = maze.find_path()

        # Tạo các đối tượng Manim để vẽ mê cung
        maze_group = VGroup()
        cell_size = 0.2  # Kích thước ô nhỏ để phù hợp với mê cung lớn
        offset_x = -maze.width * cell_size / 2
        offset_y = maze.height * cell_size / 2

        # Vẽ các node và cạnh của mê cung
        for node in maze.nodes:
            y, x = node.position
            # Vẽ node như một điểm nhỏ
            dot = Dot(point=[x * cell_size + offset_x, y * cell_size + offset_y, 0], color=BLUE_D)
            maze_group.add(dot)

            # Vẽ các cạnh nối với neighbours
            for i, neighbour in enumerate(node.neighbours):
                if neighbour:
                    ny, nx = neighbour.position
                    start = [x * cell_size + offset_x, y * cell_size + offset_y, 0]
                    end = [nx * cell_size + offset_x, ny * cell_size + offset_y, 0]
                    if i == 0:  # Up
                        end[1] += cell_size / 2
                        start[1] -= cell_size / 2
                    elif i == 1:  # Right
                        end[0] += cell_size / 2
                        start[0] -= cell_size / 2
                    elif i == 2:  # Down
                        end[1] -= cell_size / 2
                        start[1] += cell_size / 2
                    elif i == 3:  # Left
                        end[0] -= cell_size / 2
                        start[0] += cell_size / 2
                    line = Line(start=start, end=end, color=BLUE_D, stroke_width=1)
                    maze_group.add(line)

        # Vẽ đường đi màu xanh lá
        path_group = VGroup()
        if path:
            for i in range(len(path) - 1):
                current = path[i]
                next_node = path[i + 1]
                y1, x1 = current.position
                y2, x2 = next_node.position
                start = [x1 * cell_size + offset_x, y1 * cell_size + offset_y, 0]
                end = [x2 * cell_size + offset_x, y2 * cell_size + offset_y, 0]
                path_line = Line(start=start, end=end, color=GREEN, stroke_width=3)
                path_group.add(path_line)

        # Thêm tiêu đề
        title = Tex("Quantum Search", color=BLUE).scale(1.5).to_edge(UP)

        # Hiển thị animation
        self.play(Create(maze_group), run_time=2)
        self.play(Create(path_group), run_time=2)
        self.play(Write(title))
        self.wait(2)

if __name__ == "__main__":
    scene = QuantumMazeAnimation()
    scene.render()