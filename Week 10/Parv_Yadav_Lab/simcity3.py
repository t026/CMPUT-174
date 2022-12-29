
def create_grid(filename: str) -> list[list[int]]:
    """
    Create a grid of land values from a file
    """
    # TODO: Implement this function
    matrix = []
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
            matrix.append(a_row)
    return matrix


def display_grid(grid: list[list[int]]) -> None:
    """
    Display a grid of land values
    """
    # TODO: Implement this function
    for row in grid:
        a_row = ''
        for col in row:
            spaces = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            for i in range(len(str(col))):
                spaces.pop(0)
            a_row += "".join(spaces) + str(col)
        print(a_row)

def find_neighbor_values(grid: list[list[int]], row: int, col: int) -> list[int]:
    """
    Find the neighbors of a cell
    """
    # TODO: Implement this function
    rows = len(grid)
    cols = len(grid[0])
    neighbours = []

    for i in range(row-1, row+2):  # x-1, x, x+1
        for j in range(col-1, col+2):  # y-1, y+1
            if i == row and j == col:
                continue  # skip location of ‘E’
            if i < 0 or i >= rows or j < 0 or j >= cols:
                continue  # skip if location is outside the grid
            neighbours.append(grid[i][j])
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
                blist[row][col] = int(sum(find_neighbor_values(blist, row, col))/len(find_neighbor_values(blist, row, col)))
    return blist
def main() -> None:
    """
    Main program.
    """
    grid = create_grid("data_0.txt")
    print("Sim City land values:")
    display_grid(grid)
    print("\nCalculated Sim City land values:")
    new_grid = fill_gaps(grid)
    display_grid(new_grid)

main()