import random

def create_maze(size):
    # Initialize the maze with walls ('O') and paths ('-')
    maze = [['O' for _ in range(size)] for _ in range(size)]

    # Directions for moving in the maze: (dy, dx)
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
    
    def carve_path(y, x):
        maze[y][x] = '-'  # Mark the current cell as a path
        random.shuffle(directions)  # Randomize the direction order
        
        for dy, dx in directions:
            ny, nx = y + dy, x + dx  # New coordinates
            
            if 0 <= ny < size and 0 <= nx < size and maze[ny][nx] == 'O':
                # Carve a path between the current cell and the new cell
                maze[y + dy // 2][x + dx // 2] = '-'
                carve_path(ny, nx)  # Recursively carve from the new cell

    # Start the maze generation from the top-left corner
    carve_path(1, 1)

    # Return the generated maze
    return maze

def print_maze(maze):
    for row in maze:
        print(' '.join(row))

# Define the size of the maze
size = 11  # Must be an odd number to ensure proper maze structure
maze = create_maze(size)
print_maze(maze)
