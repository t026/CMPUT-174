"""
Lab 8 Version 4
Name: Tanishq
Description: Changes the symbols on the map and finishes the rest of the game and functions.
"""
MAP_FILE = 'cave_map.txt'
HELP_FILE = 'help.txt'

def load_map(map_file: str) -> list[list[str]]:
    """
    Loads a map from a file as a grid (list of lists)
    """
    with open(map_file, "r") as f:  #reads all the lines in the file and stores in a list
        lines = f.readlines()
    grid = [[0 for i in range(len(lines[0].rstrip()))] for j in range(len(lines))]  #creates an empty string
    for i in range(len(lines)):
        word = lines[i].rstrip()
        for j in range(len(lines[i].rstrip())):
            grid[i][j] = word[j]  #replaces the empty cells in the string with the symbol on the map
    return grid

def find_start(grid: list[list[str]]) -> list[int, int]:
    """
    Finds the starting position of the player on the map.
    """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                return [i,j]  #looks for the S in the grid and returns the location

def get_command() -> str:
    """
    Gets a command from the user.
    """
    return input("Enter your command:")  #returns a command from the user
    
def display_map(grid: list[list[str]], player_position: list[int, int]) -> None:
    """
    Displays the map.
    """
    symbols = {'S':'🏠', 'F':'🏺', '-':'🧱', '*':'🟢', '@':'🧝'}  #stores the emojis in a dictionary with the original symbols.
    for i in range(len(grid)):
        row = ''
        for j in range(len(grid[i])):
            if [i,j] == player_position:
                row += symbols['@']
            else:
                row += symbols[grid[i][j]]
        print(row)  #adds the player and the map to each row and prints it out

def get_grid_size(grid: list[list[str]]) -> list[int, int]:
    """
    Returns the size of the grid.
    """
    return [len(grid), len(grid[0])]  #returns the size of the grid

def is_inside_grid(grid: list[list[str]], position: list[int, int]) -> bool:
    """
    Checks if a given position is valid (inside the grid).
    """
    grid_rows, grid_cols = get_grid_size(grid)
    return position[0] < grid_rows and position[0] >= 0 and position[1] < grid_cols and position[1] >= 0  #checks if the position is between 0 and the length of the grid

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
    return directions  #returns a list of valid directions

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
        return True  #returns True if moved
    return False  #returns False if didn't move.

def check_finish(grid: list[list[str]], player_position: list[int, int]) -> bool:
    """
    Checks if the player has reached the exit.
    """
    return grid[player_position[0]][player_position[1]] == 'F' #checks if the player is at the finish position

def display_help() -> None:
    """
    Displays a list of commands.
    """
    with open (HELP_FILE, "r") as f:
        for line in f:
            print(line.strip())

def main():
    """
    Main entry point for the game.
    """
    grid = load_map(MAP_FILE)
    player_position = find_start(grid)
    while not check_finish(grid, player_position):  #runs until it reaches the finish line.
        directions = look_around(grid, player_position)
        print(f"You can go {', '.join(directions)}")
        command = get_command().lower()
        if command == 'escape':
            print("You quit the game.")
            break
        elif command == 'show map':
            display_map(grid, player_position)
        elif command == 'help':
            display_help()
        elif 'go ' in command:  #checks if it has go in the command
            if command.split(" ")[1] in ['north', 'south', 'east', 'west']:
                if move(command.split(" ")[1], player_position, grid):
                    print(f"You moved {command.split(' ')[1]}.")
                else:
                    print("There is no way there.")  #prints if could not move
            else:
                print("I do not understand.")
        else:
            print("I do not understand.")
    if check_finish(grid, player_position):
        print('Congratulations! You have reached the exit!')  #prints if game won.

if __name__ == '__main__':
    main()