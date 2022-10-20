import math


def initialMatrixToArrays(matrix: list[list[int]]):
    result: list = []
    m = len(matrix)
    n = len(matrix[0])
    for k in range(0, min(m, n) / 2):
        temp: list = []
        i = j = k
        max_i = m - k - 1
        max_j = n - k - 1
        while (i == 0, j < max_j):
            temp.append(matrix[i][j])
            ++ j
        while (i < max_i, j == max_j):
            temp.append(matrix[i][j])
            ++ i
        while (i == max_i, j > 0):
            temp.append(matrix[i][j])
            -- j
        while (j == 00, i > 0):
            temp.append(matrix[i][j])
            -- i
        result.append(temp)
    return result

print(initialMatrixToArrays([]))
