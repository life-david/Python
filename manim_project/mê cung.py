from manim import *
import numpy as np
import random

class NormalVsQuantumSearch(Scene):
    def construct(self):
        # Constants for maze size
        rows, cols = 30, 30
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
                             -i*cell_size + (rows*cell_size)/2 - cell_size/2 - 0.5, 0])  # -0.5 to account for title
                maze.add(cell)
                
                # Initialize all walls
                walls[(i, j, "top")] = True
                walls[(i, j, "right")] = True
                walls[(i, j, "bottom")] = True
                walls[(i, j, "left")] = True
        
        # Use modified Prim's algorithm for maze generation
        def generate_maze():
            # Start with a grid full of walls
            visited = set()
            walls_list = []
            
            # Start from top-left
            start_r, start_c = 0, 0
            visited.add((start_r, start_c))
            
            # Add the walls of the starting cell to the wall list
            if start_r > 0:
                walls_list.append((start_r, start_c, start_r-1, start_c, "top", "bottom"))
            if start_c < cols-1:
                walls_list.append((start_r, start_c, start_r, start_c+1, "right", "left"))
            if start_r < rows-1:
                walls_list.append((start_r, start_c, start_r+1, start_c, "bottom", "top"))
            if start_c > 0:
                walls_list.append((start_r, start_c, start_r, start_c-1, "left", "right"))
            
            # While there are walls in the list
            while walls_list:
                # Pick a random wall
                wall_index = random.randint(0, len(walls_list)-1)
                r1, c1, r2, c2, dir1, dir2 = walls_list.pop(wall_index)
                
                # If only one of the cells that the wall divides is visited
                if (r1, c1) in visited and (r2, c2) not in visited:
                    # Remove the wall
                    walls[(r1, c1, dir1)] = False
                    walls[(r2, c2, dir2)] = False
                    
                    # Mark the unvisited cell as visited
                    visited.add((r2, c2))
                    
                    # Add the neighboring walls of the cell to the wall list
                    if r2 > 0 and (r2-1, c2) not in visited:
                        walls_list.append((r2, c2, r2-1, c2, "top", "bottom"))
                    if c2 < cols-1 and (r2, c2+1) not in visited:
                        walls_list.append((r2, c2, r2, c2+1, "right", "left"))
                    if r2 < rows-1 and (r2+1, c2) not in visited:
                        walls_list.append((r2, c2, r2+1, c2, "bottom", "top"))
                    if c2 > 0 and (r2, c2-1) not in visited:
                        walls_list.append((r2, c2, r2, c2-1, "left", "right"))
                
                elif (r2, c2) in visited and (r1, c1) not in visited:
                    # Remove the wall
                    walls[(r1, c1, dir1)] = False
                    walls[(r2, c2, dir2)] = False
                    
                    # Mark the unvisited cell as visited
                    visited.add((r1, c1))
                    
                    # Add the neighboring walls of the cell to the wall list
                    if r1 > 0 and (r1-1, c1) not in visited:
                        walls_list.append((r1, c1, r1-1, c1, "top", "bottom"))
                    if c1 < cols-1 and (r1, c1+1) not in visited:
                        walls_list.append((r1, c1, r1, c1+1, "right", "left"))
                    if r1 < rows-1 and (r1+1, c1) not in visited:
                        walls_list.append((r1, c1, r1+1, c1, "bottom", "top"))
                    if c1 > 0 and (r1, c1-1) not in visited:
                        walls_list.append((r1, c1, r1, c1-1, "left", "right"))
        
        # Generate maze
        generate_maze()
        
        # Define start and end points
        start = (0, 0)  # Top-left
        end = (rows-1, cols-1)  # Bottom-right
        
        # Create entrance and exit
        walls[(start[0], start[1], "top")] = False
        walls[(end[0], end[1], "bottom")] = False
        
        # Add some random walls for more complexity
        for _ in range(rows * cols // 6):
            r = random.randint(1, rows-2)
            c = random.randint(1, cols-2)
            direction = random.choice(["top", "right", "bottom", "left"])
            walls[(r, c, direction)] = True
        
        # Draw the maze walls
        maze_walls = VGroup()
        
        for i in range(rows):
            for j in range(cols):
                # Get the position of the cell
                x = j*cell_size - (cols*cell_size)/2 + cell_size/2
                y = -i*cell_size + (rows*cell_size)/2 - cell_size/2 - 0.5  # -0.5 to account for title
                
                # Draw walls if they exist
                if walls.get((i, j, "top"), False):
                    top_wall = Line(
                        [x - cell_size/2, y + cell_size/2, 0], 
                        [x + cell_size/2, y + cell_size/2, 0],
                        stroke_width=wall_thickness
                    )
                    top_wall.set_stroke(BLUE_D)
                    maze_walls.add(top_wall)
                
                if walls.get((i, j, "right"), False):
                    right_wall = Line(
                        [x + cell_size/2, y + cell_size/2, 0], 
                        [x + cell_size/2, y - cell_size/2, 0],
                        stroke_width=wall_thickness
                    )
                    right_wall.set_stroke(BLUE_D)
                    maze_walls.add(right_wall)
                
                if walls.get((i, j, "bottom"), False):
                    bottom_wall = Line(
                        [x + cell_size/2, y - cell_size/2, 0], 
                        [x - cell_size/2, y - cell_size/2, 0],
                        stroke_width=wall_thickness
                    )
                    bottom_wall.set_stroke(BLUE_D)
                    maze_walls.add(bottom_wall)
                
                if walls.get((i, j, "left"), False):
                    left_wall = Line(
                        [x - cell_size/2, y - cell_size/2, 0], 
                        [x - cell_size/2, y + cell_size/2, 0],
                        stroke_width=wall_thickness
                    )
                    left_wall.set_stroke(BLUE_D)
                    maze_walls.add(left_wall)
        
        # Create the maze border
        maze_border = Rectangle(
            width=cols*cell_size,
            height=rows*cell_size,
            color=BLUE_D,
            stroke_width=wall_thickness
        ).move_to(maze.get_center())
        
        # Create the background
        background = Rectangle(
            width=cols*cell_size + 0.2,
            height=rows*cell_size + 0.2,
            color=BLACK,
            fill_opacity=1
        ).move_to(maze.get_center())
        
        self.play(FadeIn(background))
        self.play(FadeIn(maze_walls), FadeIn(maze_border))
        
        # Normal Search (BFS with visualization of all explored paths)
        def normal_search():
            # BFS
            queue = [(start, [start])]  # (current_position, path_to_current)
            visited = {start}
            all_explored_paths = []
            solution_path = None
            
            # Keep track of all paths explored
            while queue:
                (r, c), path = queue.pop(0)
                
                if (r, c) == end:
                    solution_path = path
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
                        neighbor not in visited):
                        visited.add(neighbor)
                        new_path = path + [neighbor]
                        queue.append((neighbor, new_path))
                        
                        # Save this exploration path
                        all_explored_paths.append(new_path)
            
            # Ensure solution_path is not None (in case no path is found)
            if solution_path is None:
                solution_path = []
                
            return solution_path, all_explored_paths
        
        # Find paths with normal search
        solution_path, all_explored_paths = normal_search()
        
        # Make sure we have a valid solution path
        if not solution_path:
            print("Error: No solution path found!")
            return
        
        # Visualize normal search with orange paths for all explorations
        def create_exploration_animation():
            # Group for all explorations
            explorations = VGroup()
            
            # Create visuals for all explored paths
            for path in all_explored_paths:
                if len(path) < 2:
                    continue
                    
                path_visuals = VGroup()
                
                for i in range(len(path) - 1):
                    r1, c1 = path[i]
                    r2, c2 = path[i + 1]
                    
                    # Calculate positions
                    x1 = c1*cell_size - (cols*cell_size)/2 + cell_size/2
                    y1 = -r1*cell_size + (rows*cell_size)/2 - cell_size/2 - 0.5
                    x2 = c2*cell_size - (cols*cell_size)/2 + cell_size/2
                    y2 = -r2*cell_size + (rows*cell_size)/2 - cell_size/2 - 0.5
                    
                    # Create line
                    line = Line([x1, y1, 0], [x2, y2, 0], color=ORANGE, stroke_width=2)
                    path_visuals.add(line)
                
                if len(path_visuals) > 0:  # Only add non-empty path visuals
                    explorations.add(path_visuals)
            
            return explorations
        
        # Create optimal path visualization
        def create_optimal_path():
            optimal_path = VGroup()
            
            for i in range(len(solution_path) - 1):
                r1, c1 = solution_path[i]
                r2, c2 = solution_path[i + 1]
                
                # Calculate positions
                x1 = c1*cell_size - (cols*cell_size)/2 + cell_size/2
                y1 = -r1*cell_size + (rows*cell_size)/2 - cell_size/2 - 0.5
                x2 = c2*cell_size - (cols*cell_size)/2 + cell_size/2
                y2 = -r2*cell_size + (rows*cell_size)/2 - cell_size/2 - 0.5
                
                # Create line
                line = Line([x1, y1, 0], [x2, y2, 0], color=GREEN_C, stroke_width=4)
                optimal_path.add(line)
            
            # Extend paths outside maze
            # Start extension
            r, c = solution_path[0]
            x = c*cell_size - (cols*cell_size)/2 + cell_size/2
            y = -r*cell_size + (rows*cell_size)/2 - cell_size/2 - 0.5
            entrance_line = Line(
                [x, y, 0],
                [x, y + cell_size/2, 0],
                color=GREEN_C,
                stroke_width=4
            )
            optimal_path.add(entrance_line)
            
            # End extension
            r, c = solution_path[-1]
            x = c*cell_size - (cols*cell_size)/2 + cell_size/2
            y = -r*cell_size + (rows*cell_size)/2 - cell_size/2 - 0.5
            exit_line = Line(
                [x, y, 0],
                [x, y - cell_size/2, 0],
                color=GREEN_C,
                stroke_width=4
            )
            optimal_path.add(exit_line)
            
            return optimal_path
        
        # Animate the search process
        exploration_paths = create_exploration_animation()
        
        # Check if exploration_paths is empty
        if len(exploration_paths) == 0:
            print("Error: No exploration paths to visualize!")
            return
            
        optimal_path = create_optimal_path()
        
        # Add marker for start and end points with green squares
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
        
        # First display normal search with orange paths
        # Create animations list for exploration paths
        exploration_animations = []
        for path in exploration_paths:
            if len(path) > 0:  # Check if path has any elements
                exploration_animations.append(Create(path, run_time=0.05))
        
        # Only play the animation if there are paths to animate
        if exploration_animations:
            self.play(
                *exploration_animations,
                run_time=3
            )
        
        # Then show the optimal (quantum) path with green
        self.play(Create(optimal_path), run_time=2)
        
        # Wait before finishing
        self.wait(2)