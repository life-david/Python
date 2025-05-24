from manim import *
import numpy as np
import random

class NormalVsQuantumSearch(Scene):
    def construct(self):
        # Constants for maze size (reduced for performance if needed)
        rows, cols = 20, 20  # Reduced from 30x30 to 20x20 for testing
        cell_size = 0.3
        wall_thickness = 3
        
        # Title
        title = Text("Normal Search VS Quantum Search", font_size=36, color=WHITE).to_edge(UP)
        subtitle = Text("Quantum Search", font_size=44, color=BLUE_B).next_to(title, DOWN)
        self.play(Write(title))
        self.play(Write(subtitle))
        
        # Create maze grid
        maze = VGroup()
        walls = {}
        
        # Initialize the grid with all walls
        for i in range(rows):
            for j in range(cols):
                cell = Square(side_length=cell_size).set_stroke(BLUE_D, 1)
                cell.move_to([j*cell_size - (cols*cell_size)/2 + cell_size/2, 
                             -i*cell_size + (rows*cell_size)/2 - cell_size/2 - 0.5, 0])
                maze.add(cell)
                
                walls[(i, j, "top")] = True
                walls[(i, j, "right")] = True
                walls[(i, j, "bottom")] = True
                walls[(i, j, "left")] = True
        
        # Use modified Prim's algorithm for maze generation
        def generate_maze():
            visited = set()
            walls_list = []
            start_r, start_c = 0, 0
            visited.add((start_r, start_c))
            
            if start_r > 0: walls_list.append((start_r, start_c, start_r-1, start_c, "top", "bottom"))
            if start_c < cols-1: walls_list.append((start_r, start_c, start_r, start_c+1, "right", "left"))
            if start_r < rows-1: walls_list.append((start_r, start_c, start_r+1, start_c, "bottom", "top"))
            if start_c > 0: walls_list.append((start_r, start_c, start_r, start_c-1, "left", "right"))
            
            while walls_list:
                wall_index = random.randint(0, len(walls_list)-1)
                r1, c1, r2, c2, dir1, dir2 = walls_list.pop(wall_index)
                
                if (r1, c1) in visited and (r2, c2) not in visited:
                    walls[(r1, c1, dir1)] = False
                    walls[(r2, c2, dir2)] = False
                    visited.add((r2, c2))
                    if r2 > 0 and (r2-1, c2) not in visited: walls_list.append((r2, c2, r2-1, c2, "top", "bottom"))
                    if c2 < cols-1 and (r2, c2+1) not in visited: walls_list.append((r2, c2, r2, c2+1, "right", "left"))
                    if r2 < rows-1 and (r2+1, c2) not in visited: walls_list.append((r2, c2, r2+1, c2, "bottom", "top"))
                    if c2 > 0 and (r2, c2-1) not in visited: walls_list.append((r2, c2, r2, c2-1, "left", "right"))
                
                elif (r2, c2) in visited and (r1, c1) not in visited:
                    walls[(r1, c1, dir1)] = False
                    walls[(r2, c2, dir2)] = False
                    visited.add((r1, c1))
                    if r1 > 0 and (r1-1, c1) not in visited: walls_list.append((r1, c1, r1-1, c1, "top", "bottom"))
                    if c1 < cols-1 and (r1, c1+1) not in visited: walls_list.append((r1, c1, r1, c1+1, "right", "left"))
                    if r1 < rows-1 and (r1+1, c1) not in visited: walls_list.append((r1, c1, r1+1, c1, "bottom", "top"))
                    if c1 > 0 and (r1, c1-1) not in visited: walls_list.append((r1, c1, r1, c1-1, "left", "right"))
        
        generate_maze()
        
        # Define start and end points
        start = (0, 0)
        end = (rows-1, cols-1)
        
        # Create entrance and exit
        walls[(start[0], start[1], "top")] = False
        walls[(end[0], end[1], "bottom")] = False
        
        # Optimize maze walls drawing
        maze_walls = VGroup()
        for i in range(rows):
            for j in range(cols):
                x = j*cell_size - (cols*cell_size)/2 + cell_size/2
                y = -i*cell_size + (rows*cell_size)/2 - cell_size/2 - 0.5
                
                if walls.get((i, j, "top"), False):
                    maze_walls.add(Line([x - cell_size/2, y + cell_size/2, 0], [x + cell_size/2, y + cell_size/2, 0], stroke_width=wall_thickness, color=BLUE_D))
                if walls.get((i, j, "right"), False):
                    maze_walls.add(Line([x + cell_size/2, y + cell_size/2, 0], [x + cell_size/2, y - cell_size/2, 0], stroke_width=wall_thickness, color=BLUE_D))
                if walls.get((i, j, "bottom"), False):
                    maze_walls.add(Line([x + cell_size/2, y - cell_size/2, 0], [x - cell_size/2, y - cell_size/2, 0], stroke_width=wall_thickness, color=BLUE_D))
                if walls.get((i, j, "left"), False):
                    maze_walls.add(Line([x - cell_size/2, y - cell_size/2, 0], [x - cell_size/2, y + cell_size/2, 0], stroke_width=wall_thickness, color=BLUE_D))
        
        # Use a single Rectangle for the border to reduce sub-mobjects
        maze_border = Rectangle(width=cols*cell_size, height=rows*cell_size, color=BLUE_D, stroke_width=wall_thickness).move_to(maze.get_center())
        background = Rectangle(width=cols*cell_size + 0.2, height=rows*cell_size + 0.2, color=BLACK, fill_opacity=1).move_to(maze.get_center())
        
        self.play(FadeIn(background))
        self.play(FadeIn(maze_walls), FadeIn(maze_border))
        
        # Normal Search with branching visualization
        def normal_search_with_branching():
            queue = [(start, [start])]  # (current_position, path_to_current)
            visited = set()
            all_explored_paths = []
            solution_path = None
            
            while queue:
                (r, c), path = queue.pop(0)
                
                if (r, c) == end:
                    solution_path = path
                    break
                
                if (r, c) in visited:
                    continue
                
                visited.add((r, c))
                all_explored_paths.append(path.copy())
                
                # Check neighbors (up, right, down, left)
                directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
                direction_names = ["top", "right", "bottom", "left"]
                
                neighbors = []
                for i, (dr, dc) in enumerate(directions):
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols and not walls.get((r, c, direction_names[i]), True)):
                        neighbors.append((nr, nc))
                
                # Branch out to all unvisited neighbors
                for nr, nc in neighbors:
                    if (nr, nc) not in visited:
                        new_path = path + [(nr, nc)]
                        queue.append(( (nr, nc), new_path ))
            
            return solution_path, all_explored_paths
        
        # Find paths
        solution_path, all_explored_paths = normal_search_with_branching()
        
        if not solution_path:
            print("Error: No solution path found!")
            return
        
        # Visualize exploration with branching
        def create_exploration_animation():
            explorations = VGroup()
            for path in all_explored_paths[:100]:  # Limit to 100 paths to reduce sub-mobjects
                if len(path) < 2:
                    continue
                path_visuals = VGroup()
                for i in range(len(path) - 1):
                    r1, c1 = path[i]
                    r2, c2 = path[i + 1]
                    x1 = c1*cell_size - (cols*cell_size)/2 + cell_size/2
                    y1 = -r1*cell_size + (rows*cell_size)/2 - cell_size/2 - 0.5
                    x2 = c2*cell_size - (cols*cell_size)/2 + cell_size/2
                    y2 = -r2*cell_size + (rows*cell_size)/2 - cell_size/2 - 0.5
                    line = Line([x1, y1, 0], [x2, y2, 0], color=ORANGE, stroke_width=2)
                    path_visuals.add(line)
                if len(path_visuals) > 0:
                    explorations.add(path_visuals)
            return explorations
        
        # Create optimal path
        def create_optimal_path():
            optimal_path = VGroup()
            for i in range(len(solution_path) - 1):
                r1, c1 = solution_path[i]
                r2, c2 = solution_path[i + 1]
                x1 = c1*cell_size - (cols*cell_size)/2 + cell_size/2
                y1 = -r1*cell_size + (rows*cell_size)/2 - cell_size/2 - 0.5
                x2 = c2*cell_size - (cols*cell_size)/2 + cell_size/2
                y2 = -r2*cell_size + (rows*cell_size)/2 - cell_size/2 - 0.5
                line = Line([x1, y1, 0], [x2, y2, 0], color=GREEN_C, stroke_width=4)
                optimal_path.add(line)
            # Start extension
            r, c = solution_path[0]
            x = c*cell_size - (cols*cell_size)/2 + cell_size/2
            y = -r*cell_size + (rows*cell_size)/2 - cell_size/2 - 0.5
            optimal_path.add(Line([x, y, 0], [x, y + cell_size/2, 0], color=GREEN_C, stroke_width=4))
            # End extension
            r, c = solution_path[-1]
            x = c*cell_size - (cols*cell_size)/2 + cell_size/2
            y = -r*cell_size + (rows*cell_size)/2 - cell_size/2 - 0.5
            optimal_path.add(Line([x, y, 0], [x, y - cell_size/2, 0], color=GREEN_C, stroke_width=4))
            return optimal_path
        
        # Animate
        exploration_paths = create_exploration_animation()
        optimal_path = create_optimal_path()
        
        start_point = Square(side_length=cell_size/3, color=GREEN_C, fill_opacity=1).move_to([
            start[1]*cell_size - (cols*cell_size)/2 + cell_size/2,
            -start[0]*cell_size + (rows*cell_size)/2 - cell_size/2 - 0.5 + cell_size/2,
            0
        ])
        end_point = Square(side_length=cell_size/3, color=GREEN_C, fill_opacity=1).move_to([
            end[1]*cell_size - (cols*cell_size)/2 + cell_size/2,
            -end[0]*cell_size + (rows*cell_size)/2 - cell_size/2 - 0.5 - cell_size/2,
            0
        ])
        
        self.play(FadeIn(start_point), FadeIn(end_point))
        
        # Animate exploration paths with branching
        exploration_animations = [Create(path, run_time=0.05) for path in exploration_paths if len(path) > 0]
        if exploration_animations:
            self.play(*exploration_animations, run_time=5)
        
        # Animate optimal path
        self.play(Create(optimal_path), run_time=2)
        
        self.wait(2)

# To run this, use: manim -pql --disable_caching your_script.py NormalVsQuantumSearch