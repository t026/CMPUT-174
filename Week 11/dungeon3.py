MAP_FILE = 'cave_map.txt'
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

def move(direction: str, player_position: list[int, int], grid: list[list[str]]) -> bool:
    """
    Moves the player in the given direction.
    """
    if direction in look_around(grid, player_position):
        if grid[player_position[0]][player_position[1]] == find_start(grid):
            grid[player_position[0]][player_position[1]] = 'S'
        if direction == 'north':
            player_position[0] -= 1
        elif direction == 'south':
            player_position[0] += 1
        elif direction == 'east':
            player_position[1] += 1
        else:
            player_position[1] -= 1
        grid[player_position[0]][player_position[1]] = '@'
        return True
    return False

def main():
    """
    Main entry point for the game.
    """
    grid = load_map('cave_map.txt')
    player_position = find_start(grid)
    while True:
        directions = look_around(grid, player_position)
        print(f"You can go {', '.join(directions)}")
        command = get_command().lower()
        if command == 'escape':
            break
        elif command == 'show map':
            display_map(grid, player_position)
        elif command.split(" ")[1] in ['north', 'south', 'east', 'west']:
            if move(command.split(" ")[1], player_position, grid):
                print(f"You moved {command.split(' ')[1]}")
            else:
                print("There is no way there.")
        else:
            print("I do not understand.")

if __name__ == '__main__':
    main()