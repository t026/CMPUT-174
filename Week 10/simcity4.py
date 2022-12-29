"""
Lab 7 Version 4
Name: Tanishq
Description: Implements 2 functions that find the maximum value in a grid and the average value of the grid.
"""

from copy import deepcopy  #imports the deepcopy function from the copy library which will allow us to clone a 2d list without any aliasing.

def create_grid(filename: str) -> list[list[int]]:
    """
    Create a grid of land values from a file
    """
    with open(filename, "r") as file:
        file_lines = file.readlines()
    num_of_rows = int(file_lines[0])
    num_of_columns = int(file_lines[1])
    grid = [[0 for x in range(num_of_columns)] for y in range(num_of_rows)]  #creates a 2d array made up of 0's.
    index = 2  #starts at 2 because 0 and 1 are for rows and columns
    for i in range(num_of_rows):
        for j in range(num_of_columns):
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
    neighbours_list = []
    for i in range(row-1, row+2): 
        for j in range(col-1, col+2):  
            if i == row and j == col:  #checks if current row and column is equal to the original cell.
                continue  #skips rest of loop
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):  #checks if it is beyond the grid.
                continue  #skips rest of loop 
            neighbours_list.append(grid[i][j])  #adds neighbour to list.
    return neighbours_list

def fill_gaps(grid: list[list[int]]) -> list[list[int]]:
    """
    Fill the gaps in the grid
    Creates a new grid with the same dimensions as the original grid
    Calls find_neighbor_values() to find the neighbors of each cell
    Do NOT modify the original grid!
    """
    newgrid = deepcopy(grid) #clones grid without aliasing.
    for i in range(0, len(newgrid)):
        for j in range(0, len(newgrid[i])):
            if newgrid[i][j] == 0:  #checks every single cell if the value is 0
                neighbours_list = find_neighbor_values(newgrid, i, j)
                newgrid[i][j] = int(sum(neighbours_list)/len(neighbours_list))  #the grid is made up of integers
    return newgrid

def find_max(grid: list[list[int]]) -> int:
    """
    Find the max value in the grid (rounded to the nearest integer)
    """
    return max(max(x) for x in grid)  #inside the brackets is a for loop that loops through each row and finds the max and stores it in the list
    #Then return the max of the max values to find the maximum of all of the lists in the 2d list.

def find_average(grid: list[list[int]]) -> int:
    """
    Find the average value in the grid (rounded to the nearest integer)
    """
    return int(round((sum(sum(x) for x in grid))/(len(grid)*len(grid[0]))))  #same method as max, but uses sum and divides by the product of the row length and column length
    #round function used as int() always rounds down.
    
    
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

if __name__ == "__main__":  #calls the main function while also ensuring that the main function does not run if imported into another library
    main()