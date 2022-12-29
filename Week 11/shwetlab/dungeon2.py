MAP_FILE = 'cave_map.txt'

def load_map(map_file: str) -> list[list[str]]:
    """
    Loads a map from a file as a grid (list of lists)
    """
    file = open(map_file, "r")
    filelist = file.readlines()
    file.close()
    rows = len(filelist)
    cols = len(filelist[0]) - 1
    grid = []
    for i in range(len(filelist)):
        filelist[i] = filelist[i].strip()
    for i in range(rows):
        grid.append([])
        for j in range(cols):
            grid[i].append('')
    for i in range(rows):
        line = filelist[i].strip()
        for j in range(cols):
            grid[i][j] = line[j]
    return grid

def find_start(grid: list[list[str]]) -> list[int, int]:
    """
    Finds the starting position of the player on the map.
    """
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j].upper() == 'S':
                return [i,j]

def get_command() -> str:
    """
    Gets a command from the user.
    """
    command = input("Enter the command-")
    return command

def display_map(grid: list[list[str]], player_position: list[int, int]) -> None:
    """
    Displays the map.
    """
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        row = ''
        for j in range(cols):
            if player_position[0] == i and player_position[1] == j:
                row += '@'
            else:
                row += grid[i][j]
        print(row)

def get_grid_size(grid: list[list[str]]) -> list[int, int]:
    """
    Returns the size of the grid.
    """
    rows = len(grid)
    cols = len(grid[0])
    size = [rows, cols]
    return size

def is_inside_grid(grid: list[list[str]], position: list[int, int]) -> bool:
    """
    Checks if a given position is valid (inside the grid).
    """
    grid_rows, grid_cols = get_grid_size(grid)
    if position[0] < grid_rows and position[0] >= 0:
        if position[1] < grid_cols and position[1] >= 0:
            return True
        else:
            return False
    else:
        return False
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
    if is_inside_grid(grid, [row, col-1]) and grid[row][col-1] in allowed_objects:
        directions.append('west')
    if is_inside_grid(grid, [row+1]) and grid[row+1][col] in allowed_objects:
        directions.append('south')
    if is_inside_grid(grid, [row, col+1]) and grid[row][col+1] in allowed_objects:
        directions.append('east')
    return directions
def main():
    """
    Main entry point for the game.
    """
    # TODO: implement the main() function
    grid = load_map(MAP_FILE)
    start = find_start(grid)
    while True:
        print(is_inside_grid(grid, [0, 4]))
        command = get_command()
        if command == 'escape':
            break
        elif command == 'show map':
            display_map(grid, start)
        else:
            print("I do not understand.")


if __name__ == '__main__':
    main()
