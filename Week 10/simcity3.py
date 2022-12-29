"""
Lab 7 Version 3
Name: Tanishq
Description: Implements a function that finds the gaps in a grid and fills it using the average of its neighbours.
"""

from copy import deepcopy  #imports the deepcopy function from the copy library which will allow us to clone a 2d list without any aliasing.

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
            if i == row and j == col:  #checks if current row and column is equal to the original cell.
                continue  #skips rest of loop
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):  #checks if it is beyond the grid.
                continue  #skips rest of loop 
            neighbours.append(grid[i][j])  #adds neighbour to list.
    return neighbours

def fill_gaps(grid: list[list[int]]) -> list[list[int]]:
    """
    Fill the gaps in the grid
    Creates a new grid with the same dimensions as the original grid
    Calls find_neighbor_values() to find the neighbors of each cell
    Do NOT modify the original grid!
    """
    newgrid = deepcopy(grid) #clones grid without aliasing.
    for i in range(0, len(newgrid)):
        for j in range(0, len(newgrid[0])):
            if newgrid[i][j] == 0:  #checks every single cell if the value is 0
                neighbours = find_neighbor_values(newgrid, i, j)
                newgrid[i][j] = int(sum(neighbours)/len(neighbours))  #the grid is made up of integers
    return newgrid


def main() -> None:
    """
    Main program.
    """
    grid = create_grid("data_4.txt")
    print("Sim City land values:")
    display_grid(grid)
    print("\nCalculated Sim City land values:")
    new_grid = fill_gaps(grid)
    display_grid(new_grid)
    
if __name__ == "__main__":  #calls the main function while also ensuring that the main function does not run if imported into another library
    main()