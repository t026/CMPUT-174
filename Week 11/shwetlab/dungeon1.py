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


def main():
    """
    Main entry point for the game.
    """
    # TODO: implement the main() function
    grid = load_map(MAP_FILE)
    print(grid)
    start = find_start(grid)
    print(start)
    while True:
        command = get_command()
        if command == 'escape':
            break
        else:
            print("I do not understand.")


if __name__ == '__main__':
    main()
