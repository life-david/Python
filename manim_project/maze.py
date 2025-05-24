from manim import *
import numpy as np
import random

class MazePathfinding(Scene):
    def construct(self):
        # Constants for maze size
        rows, cols = 20, 20
        cell_size = 0.4
        
        # Title
        title = Text("Quantum Search", font_size=48, color=BLUE_B).to_edge(UP)
        self.play(Write(title))
        
        # Create maze grid - First create a blank grid
        maze = VGroup()
        walls = {}
        
        # Initialize the grid with all walls
        for i in range(rows):
            for j in range(cols):
                cell = Square(side_length=cell_size).set_stroke(BLUE_D, 1)
                cell.move_to([j*cell_size - (cols*cell_size)/2 + cell_size/2, 
                             -i*cell_size + (rows*cell_size)/2 - cell_size/2, 0])
                maze.add(cell)
                
                # Initialize all walls
                # Top, right, bottom, left walls for each cell
                walls[(i, j, "top")] = True
                walls[(i, j, "right")] = True
                walls[(i, j, "bottom")] = True
                walls[(i, j, "left")] = True
        
        # Use Depth-First Search to generate the maze
        visited = set()
        stack = [(0, 0)]  # Start at top-left
        
        # Maze generation with depth-first search
        while stack:
            current = stack[-1]
            r, c = current
            visited.add(current)
            
            # Get unvisited neighbors
            neighbors = []
            # Up, Right, Down, Left
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            direction_names = ["top", "right", "bottom", "left"]
            opposite_walls = ["bottom", "left", "top", "right"]
            
            for i, (dr, dc) in enumerate(directions):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    neighbors.append((nr, nc, direction_names[i], opposite_walls[i]))
            
            if neighbors:
                # Choose a random neighbor
                next_r, next_c, wall_to_remove, opposite_wall = random.choice(neighbors)
                
                # Remove walls between current cell and next cell
                walls[(r, c, wall_to_remove)] = False
                walls[(next_r, next_c, opposite_wall)] = False
                
                # Push the next cell to the stack
                stack.append((next_r, next_c))
            else:
                # Backtrack
                stack.pop()
        
        # Define start and end points
        start = (0, 0)  # Top-left
        end = (rows-1, cols-1)  # Bottom-right
        
        # Create entrance and exit by removing outer walls
        walls[(start[0], start[1], "top")] = False  # Remove top wall at start
        walls[(end[0], end[1], "bottom")] = False  # Remove bottom wall at end
        
        # Draw the maze walls
        maze_walls = VGroup()
        
        for i in range(rows):
            for j in range(cols):
                # Get the position of the cell
                x = j*cell_size - (cols*cell_size)/2 + cell_size/2
                y = -i*cell_size + (rows*cell_size)/2 - cell_size/2
                
                # Draw walls if they exist
                if walls.get((i, j, "top"), False):
                    top_wall = Line([x - cell_size/2, y + cell_size/2, 0], 
                                   [x + cell_size/2, y + cell_size/2, 0])
                    top_wall.set_stroke(BLUE_D, 2)
                    maze_walls.add(top_wall)
                
                if walls.get((i, j, "right"), False):
                    right_wall = Line([x + cell_size/2, y + cell_size/2, 0], 
                                     [x + cell_size/2, y - cell_size/2, 0])
                    right_wall.set_stroke(BLUE_D, 2)
                    maze_walls.add(right_wall)
                
                if walls.get((i, j, "bottom"), False):
                    bottom_wall = Line([x + cell_size/2, y - cell_size/2, 0], 
                                      [x - cell_size/2, y - cell_size/2, 0])
                    bottom_wall.set_stroke(BLUE_D, 2)
                    maze_walls.add(bottom_wall)
                
                if walls.get((i, j, "left"), False):
                    left_wall = Line([x - cell_size/2, y - cell_size/2, 0], 
                                    [x - cell_size/2, y + cell_size/2, 0])
                    left_wall.set_stroke(BLUE_D, 2)
                    maze_walls.add(left_wall)
        
        # Create the background
        background = Rectangle(
            width=cols*cell_size + 0.2,
            height=rows*cell_size + 0.2,
            color=BLACK,
            fill_opacity=1
        ).move_to(maze.get_center())
        
        self.play(FadeIn(background))
        self.play(FadeIn(maze_walls))
        
        # Solve the maze using BFS
        def solve_maze():
            queue = [start]
            came_from = {start: None}
            
            while queue:
                current = queue.pop(0)
                r, c = current
                
                if current == end:
                    break
                
                # Check neighbors (up, right, down, left)
                directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                direction_names = ["top", "right", "bottom", "left"]
                
                for i, (dr, dc) in enumerate(directions):
                    nr, nc = r + dr, c + dc
                    neighbor = (nr, nc)
                    
                    # If there's no wall between current and neighbor, and neighbor hasn't been visited
                    if (0 <= nr < rows and 0 <= nc < cols and 
                        not walls.get((r, c, direction_names[i]), True) and 
                        neighbor not in came_from):
                        queue.append(neighbor)
                        came_from[neighbor] = current
            
            # Reconstruct path
            path = []
            current = end
            while current != start:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            
            return path
        
        # Get solution path
        solution_path = solve_maze()
        
        # Create visual path
        path_lines = VGroup()
        for i in range(len(solution_path) - 1):
            r1, c1 = solution_path[i]
            r2, c2 = solution_path[i + 1]
            
            # Calculate positions
            x1 = c1*cell_size - (cols*cell_size)/2 + cell_size/2
            y1 = -r1*cell_size + (rows*cell_size)/2 - cell_size/2
            x2 = c2*cell_size - (cols*cell_size)/2 + cell_size/2
            y2 = -r2*cell_size + (rows*cell_size)/2 - cell_size/2
            
            # Draw line segment between centers of cells
            line = Line([x1, y1, 0], [x2, y2, 0], color=GREEN_C, stroke_width=4)
            path_lines.add(line)
        
        # Extend the path outside the maze for entrance and exit
        # Start point extension
        r, c = solution_path[0]
        x = c*cell_size - (cols*cell_size)/2 + cell_size/2
        y = -r*cell_size + (rows*cell_size)/2 - cell_size/2
        entrance_line = Line(
            [x, y, 0],
            [x, y + cell_size/2, 0],
            color=GREEN_C,
            stroke_width=4
        )
        path_lines.add(entrance_line)
        
        # End point extension
        r, c = solution_path[-1]
        x = c*cell_size - (cols*cell_size)/2 + cell_size/2
        y = -r*cell_size + (rows*cell_size)/2 - cell_size/2
        exit_line = Line(
            [x, y, 0],
            [x, y - cell_size/2, 0],
            color=GREEN_C,
            stroke_width=4
        )
        path_lines.add(exit_line)
        
        # Animate drawing the solution path
        self.play(Create(path_lines), run_time=3)
        
        # Highlight start and end points with green dots
        start_point = Dot(
            point=[
                start[1]*cell_size - (cols*cell_size)/2 + cell_size/2,
                -start[0]*cell_size + (rows*cell_size)/2 - cell_size/2 + cell_size/2,  # Moved up to entrance
                0
            ],
            color=GREEN_C,
            radius=0.1
        )
        
        end_point = Dot(
            point=[
                end[1]*cell_size - (cols*cell_size)/2 + cell_size/2,
                -end[0]*cell_size + (rows*cell_size)/2 - cell_size/2 - cell_size/2,  # Moved down to exit
                0
            ],
            color=GREEN_C,
            radius=0.1
        )
        
        self.play(FadeIn(start_point), FadeIn(end_point))
        
        # Final pause
        self.wait(2)