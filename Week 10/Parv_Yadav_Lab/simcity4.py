#simcity version 4
def create_grid(filename: str) -> list[list[int]]:
    """
    Create a grid of land values from a file
    """
    # TODO: Implement this function
    grid = []
    with open(filename, 'r') as file:  
        lines = file.readlines()
        rows = lines[0] 
        cols = lines[1]
        count = 2
        for i in range(int(rows)):
            a_row = []
            for j in range(int(cols)):
                a_row.append(int(lines[count]))
                count += 1
            grid.append(a_row)
    return grid


def display_grid(grid: list[list[int]]) -> None:
    """
    Display a grid of land values
    """
    # TODO: Implement this function
    for row in grid:
        current_row = ''
        for col in row:
            spaces = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            for i in range(len(str(col))):
                spaces.pop(0)
            current_row += "".join(spaces) + str(col)
        print(current_row)

def find_neighbor_values(grid: list[list[int]], row: int, col: int) -> list[int]:
    """
    Find the neighbors of a cell
    """
    # TODO: Implement this function
    row_length = len(grid)
    col_length = len(grid[0])
    neighbours = []

    for x in range(row-1, row+2):  # x-1, x, x+1
        for y in range(col-1, col+2):  # y-1, y+1
            if x == row and y == col:
                continue  # skip location of ‘E’
            if x < 0 or x >= row_length or y < 0 or y >= col_length:
                continue  # skip if location is outside the grid
            neighbours.append(grid[x][y])
    return neighbours


def fill_gaps(grid: list[list[int]]) -> list[list[int]]:
    """
    Fill the gaps in the grid
    Creates a new grid with the same dimensions as the original grid
    Calls find_neighbor_values() to find the neighbors of each cell
    Do NOT modify the original grid!
    """
    # TODO: Implement this function
    blist = []
    for row in grid:
        a_row = []
        for item in row:
            a_row.append(item)
        blist.append(a_row)
    row_length = len(blist)
    col_length = len(blist[0])
    for row in range(row_length):
        for col in range(col_length):
            if blist[row][col] == 0:
                new_value = int(sum(find_neighbor_values(blist, row, col))/len(find_neighbor_values(blist, row, col)))
                blist[row][col] = new_value
    return blist

def find_max(grid: list[list[int]]) -> int:
    """
    Find the max value in the grid (rounded to the nearest integer)
    """
    # TODO: Get the maximum value in the grid
    row_length = len(grid)
    col_length = len(grid[0])
    max = 0
    for row in range(row_length):
        for col in range(col_length):
            if grid[row][col] > max:
                max = grid[row][col]
    max = round(max)
    return max


def find_average(grid: list[list[int]]) -> int:
    """
    Find the average value in the grid (rounded to the nearest integer)
    """
    # TODO: Get the average value of the grid
    row_length = len(grid)
    col_length = len(grid[0])
    sum = 0
    for row in range(row_length):
        for col in range(col_length):
            sum += grid[row][col]
    average = sum/(row_length*col_length)
    average = round(average)
    return average

def main() -> None:
    """
    Main program.
    """
    grid = create_grid("data_0.txt")
    print("Sim City Land Values:")
    display_grid(grid)
    print("\nCalculated Sim City land values:")
    new_grid = fill_gaps(grid)
    display_grid(new_grid)
    print("\nSTATS")
    print(f"Average land value in this city: {find_average(new_grid)}")
    print(f"Maximum land value in this city: {find_max(new_grid)}")

main()

def findmax(grid):
    maxlist = []
    for x in grid:
        maxlist.append(max(x))
    return max(maxlist)