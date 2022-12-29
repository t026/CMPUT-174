from copy import deepcopy
def display(matrix):
    length = len(matrix)
    for i in range(length):
        row = '  '
        for j in range(len(matrix[i])):
            row += matrix[i][j] + ' '*5
        print(row.rstrip())
def transpose(matrix):
    row = len(matrix)
    col = len(matrix[0])
    transposed_matrix = []
    for i in range(col):
        column = []
        for j in range(row):
            column.append(matrix[j][i])
        transposed_matrix.append(column)
    return transposed_matrix
    print()
def main():
    matrix = [['A', 'B'], ['C', 'D'], ['E', 'F']]
    list2 = matrix
    matrix = transpose(matrix)
    al = [[1,2,3],[1,2,3]]
    l = deepcopy(al)
    al[1][1] = 'a'
    print(l)
if __name__ == '__main__':
    main()