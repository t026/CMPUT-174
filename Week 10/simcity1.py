"""
Lab 7 Version 1
Name: Tanishq
Description: Contains a function that reads a text file and creates a 2d grid from it, and another function that creates
"""
def create_grid(filename: str) -> list[list[int]]:
    """
    Create a grid of land values from a file
    """
    with open(filename, "r") as file:
        file_lines = file.readlines()
    rows = int(file_lines[0])
    columns = int(file_lines[1])
    grid = [[0 for x in range(columns)] for y in range(rows)]  #creates a 2d array made up of 0's.
    index = 2  #starts at 2 because 0 and 1 are for rows and columns
    for i in range(rows):
        for j in range(columns):
            grid[i][j] = int(file_lines[index])
            index += 1
    return grid


def display_grid(grid: list[list[int]]) -> None:
    """
    Display a grid of land values
    """
    for i in range(len(grid)):
        row = ''
        for j in range(len(grid[i])):
            row += f"{str(grid[i][j]):>10}"  #arranges the columns nicely by giving each column a width of 10.
        print(row)

def main() -> None:
    """
    Main program.
    """
    grid = create_grid("data_0.txt")
    print("Sim City Land Values:")
    display_grid(grid)

if __name__ == "__main__":  #calls the main function while also ensuring that the main function does not run if imported into another library
    main()