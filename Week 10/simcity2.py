"""
Lab 7 Version 2
Name: Tanishq
Description: Implements a function that finds the neighbouring cells of a cell in the grid.
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

def find_neighbor_values(grid: list[list[int]], row: int, col: int) -> list[int]:
    """
    Find the neighbors of a cell
    """
    neighbours = []
    for i in range(row-1, row+2): 
        for j in range(col-1, col+2):  
            if i == row and j == col:
                continue
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
                continue
            neighbours.append(grid[i][j])
    return neighbours

def main() -> None:
    """
    Main program.
    """
    grid = create_grid("data_0.txt")
    print("Sim City Land Values:")
    display_grid(grid)

if __name__ == "__main__":  #calls the main function while also ensuring that the main function does not run if imported into another library
    main()