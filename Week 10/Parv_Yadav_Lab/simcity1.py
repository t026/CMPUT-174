
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
    for row in grid:
        a_row = ''
        for col in row:
            spaces = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            for i in range(len(str(col))):
                spaces.pop(0)
            a_row += "".join(spaces) + str(col)
        print(a_row)

def main() -> None:
    """
    Main program.
    """
    grid = create_grid("data_4.txt")
    print("Sim City Land Values:")
    display_grid(grid)

main()