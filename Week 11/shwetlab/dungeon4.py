MAP_FILE = 'midgard_map.txt'
HELP_FILE = 'help.txt'

def load_map(map_file: str) -> list[list[str]]:
    """
    Loads a map from a file as a grid (list of lists)
    """
    file = open(map_file, "r")
    filelist = file.readlines()
    file.close()  #creates a list of lines from the file.
    rows = len(filelist)  #finds the number of rows in the list
    cols = len(filelist[0].strip())  #finds the number of columns in the list.
    grid = []
    for i in range(len(filelist)):
        filelist[i] = filelist[i].strip()  #removes /n from each line in the list.
    for i in range(rows):
        grid.append([])
        for j in range(cols):
            grid[i].append('')  #creates an empty grid of size row x col
    for i in range(rows):
        line = filelist[i].strip()
        for j in range(cols):
            grid[i][j] = line[j]  #fills the grid with the correct values.
    return grid  

def find_start(grid: list[list[str]]) -> list[int, int]:
    """
    Finds the starting position of the player on the map.
    """
    print(grid)
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j].upper() == 'S':
                return [i,j]  #returns a list with the grid position of the letter 'S'

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
                row += '🧝'  #adds this emoji for the player position
            else:
                if grid[i][j] == 'S':
                    row += '🏠' 
                elif grid[i][j] == 'F':
                    row += '🏺'
                elif grid[i][j] == '-':
                    row += '🧱'
                elif grid[i][j] == '*':
                    row += '🟢'  #adds the correct emoji the row sentence
        print(row)  #prints each row one by one

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
    if position[0] < grid_rows and position[0] >= 0:  #checks if the row position is between 0 and the num of rows
        if position[1] < grid_cols and position[1] >= 0:  #checks if the column position is between 0 and the num of cols
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
    if is_inside_grid(grid, [row, col-1]) and grid[row][col-1] in allowed_objects:  #checks if the grid is valid and then adds the direction to the list.
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
    returnbool = False  #this is the return value
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
            returnbool = True  #returns True if the player moves.
    return returnbool

def check_finish(grid: list[list[str]], player_position: list[int, int]) -> bool:
    """
    Checks if the player has reached the exit.
    """
    rows = len(grid)
    cols = len(grid[0])
    finish_position = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'F':
                finish_position = [i, j]
    return finish_position == player_position  #finds the finish position on the grid and compares it to the player position

def display_help() -> None:
    """
    Displays a list of commands.
    """
    # TODO: implement this function
    file = open(HELP_FILE, "r")
    filelines = file.readlines()
    file.close()
    for i in filelines:
        print(i.strip())  #prints every line in the file without /n

def main():
    """
    Main entry point for the game.
    """
    # TODO: implement the main() function
    grid = load_map(MAP_FILE)
    player_position = find_start(grid)
    while True:
        if check_finish(grid, player_position):
            print("You have reached the exit")
            break  #checks if the player reaches the finish line first.
        allowed_directions = look_around(grid, player_position)
        print("Valid Directions:")
        for i in allowed_directions:
            print(i)  #prints the directions
        command = get_command()  #gets a command
        if command == 'escape':
            print("You quit the game")
            break  #quits the game if the command is escape
        elif command == 'show map':
            display_map(grid, player_position)
        elif command == "go north" or command == "go south" or command == "go east" or command == "go west":
            direction = command.split(" ")[1]
            if move(direction, player_position, grid):
                print(f"You moved {direction}")
            else:
                print("There is no way there")
        elif command == 'help':
            display_help()
        else:
            print("I do not understand")


if __name__ == '__main__':
    main()
