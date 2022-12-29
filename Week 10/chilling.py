grid = [[1,2,3],
        [4,5,6],
        [7,8,9]]
m = 3
n = 3
for row_index in range(0, m):
    for col_index in range(0, n):
        if row_index == m-1 and col_index == n-1:
            print(grid[row_index][col_index])