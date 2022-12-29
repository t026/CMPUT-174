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

def main():
    """
    Main entry point for the game.
    """
    grid = load_map('cave_map.txt')
    player_position = find_start(grid)
    print(grid)
    print(find_start(grid))
    while True:
        command = get_command().lower()
        if command == 'escape':
            break
        else:
            print("I do not understand.")

if __name__ == '__main__':
    main()