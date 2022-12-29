cols = 5
rows = 5
row_count = 0
matrix = []
while row_count < rows:
    matrix.append([])
    col_count = 0
    while col_count < cols:
        matrix[row_count].append(0)
        col_count += 1
    row_count += 1
grid = [[0 for i in range(cols)] for j in range(cols)]
print(matrix)
print(grid)