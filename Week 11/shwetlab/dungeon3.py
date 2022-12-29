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
    if is_inside_grid(grid, [row+1, col]) and grid[row+1][col] in allowed_objects:
        directions.append('south')
    if is_inside_grid(grid, [row, col+1]) and grid[row][col+1] in allowed_objects:
        directions.append('east')
    return directions

def move(direction: str, player_position: list[int, int], grid: list[list[str]]) -> bool:
    """
    Moves the player in the given direction.
    """
    directions = look_around(grid, player_position)
    returnbool = False
    for i in directions:
        if direction == i:
            if direction.lower() == "north":
                player_position[0] = player_position[0] - 1
            elif direction.lower() == "south":
                player_position[0] = player_position[0] + 1
            elif direction.lower() == "east":
                player_position[1] = player_position[1] + 1
            elif direction.lower() == "west":
                player_position[1] = player_position[1] - 1
            returnbool = True
    return returnbool
def main():
    """
    Main entry point for the game.
    """
    # TODO: implement the main() function
    grid = load_map(MAP_FILE)
    player_position = find_start(grid)
    while True:
        allowed_directions = look_around(grid, player_position)
        print("Valid Directions:")
        for i in allowed_directions:
            print(i)
        command = get_command()
        if command == 'escape':
            break
        elif command == 'show map':
            display_map(grid, player_position)
        elif command == "go north" or command == "go south" or command == "go east" or command == "go west":
            direction = command.split(" ")[1]
            if move(direction, player_position, grid):
                print(f"You moved {direction}")
            else:
                print("There is no way there")
        else:
            print("I do not understand")


if __name__ == '__main__':
    main()
