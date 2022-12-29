def load_map(map_file: str) -> list[list[str]]:
    """
    Loads a map from a file as a grid (list of lists)
    """
    with open(map_file, "r") as f:
        lines = f.readlines()
    grid = [[0 for i in range(len(lines[0].rstrip()))] for j in range(len(lines))]
    for i in range(len(lines)):
        word = lines[i].rstrip()
        for j in range(len(lines[i].rstrip())):
            grid[i][j] = word[j]
    return grid

def find_start(grid: list[list[str]]) -> list[int, int]:
    """
    Finds the starting position of the player on the map.
    """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                return [i,j]

def get_command() -> str:
    """
    Gets a command from the user.
    """
    return input("Enter your command:")
    
def display_map(grid: list[list[str]], player_position: list[int, int]) -> None:
    """
    Displays the map.
    """
    for i in range(len(grid)):
        row = ''
        for j in range(len(grid[i])):
            if [i,j] == player_position:
                row += "@"
            else:
                row += grid[i][j]
        print(row)

def get_grid_size(grid: list[list[str]]) -> list[int, int]:
    """
    Returns the size of the grid.
    """
    # TODO: implement this function
    return [len(grid), len(grid[0])]

def is_inside_grid(grid: list[list[str]], position: list[int, int]) -> bool:
    """
    Checks if a given position is valid (inside the grid).
    """
    grid_rows, grid_cols = get_grid_size(grid)
    return position[0] < grid_rows and position[0] >= 0 and position[1] < grid_cols and position[1] >= 0

def look_around(grid: list[list[str]], player_position: list[int, int]) -> list:
    """
    Returns the allowed directions.
    """
    allowed_objects = ('S', 'F', '*')
    row = player_position[0]
    col = player_position[1]
    directions = []
    if is_inside_grid(grid, [row - 1, col]) and grid[row - 1][col] in allowed_objects:
        directions.append('north')
    # TODO: implement the rest of the function
    if is_inside_grid(grid, [row + 1, col]) and grid[row + 1][col] in allowed_objects:
        directions.append('south')
    if is_inside_grid(grid, [row, col-1]) and grid[row][col-1] in allowed_objects:
        directions.append('west')
    if is_inside_grid(grid, [row, col+1]) and grid[row][col+1] in allowed_objects:
        directions.append('east')
    return directions

def main():
    """
    Main entry point for the game.
    """
    grid = load_map('cave_map.txt')
    player_position = find_start(grid)
    while True:
        directions = look_around(grid, player_position)
        for i in directions:
            print(f"You can go {i}")
        command = get_command().lower()
        if command == 'escape':
            break
        elif command == 'show map':
            display_map(grid, player_position)
        else:
            print("I do not understand.")

if __name__ == '__main__':
    main()