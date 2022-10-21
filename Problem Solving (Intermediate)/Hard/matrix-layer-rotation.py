import math


def initialMatrixToArrays(matrix: list[list[int]], m: int, n: int):
    arrays: list = []
    for k in range(0, int(min(m, n) / 2)):
        temp: list = []
        i = j = k
        max_i = m - k - 1
        max_j = n - k - 1
        while i == k and j < max_j:
            temp.append(matrix[i][j])
            j += 1
        while i < max_i and j == max_j:
            temp.append(matrix[i][j])
            i += 1
        while i == max_i and j > k:
            temp.append(matrix[i][j])
            j -= 1
        while j == k and i > k:
            temp.append(matrix[i][j])
            i -= 1
        arrays.append(temp)
    return arrays


def rotateMatrix(matrix: list[list[int]], arrays: list[list[int]], m: int, n: int, r: int):
    for k in range(0, len(arrays)):
        runner = 0
        i = j = k
        r_k = r % ((m + n - 4 * k - 2) * 2)
        max_i = m - k - 1
        max_j = n - k - 1
        while i == k and j < max_j:
            matrix[i][j] = arrays[k][runner + r_k - len(arrays[k])]
            j += 1
            runner += 1
        while i < max_i and j == max_j:
            matrix[i][j] = arrays[k][runner + r_k - len(arrays[k])]
            i += 1
            runner += 1
        while i == max_i and j > k:
            matrix[i][j] = arrays[k][runner + r_k - len(arrays[k])]
            j -= 1
            runner += 1
        while j == k and i > k:
            matrix[i][j] = arrays[k][runner + r_k - len(arrays[k])]
            i -= 1
            runner += 1
    return matrix


def matrixRotation(matrix, r):
    # Write your code here
    m, n = len(matrix), len(matrix[0])
    arrays = initialMatrixToArrays(matrix, m, n)
    rotateMatrix(matrix, arrays, m, n, r)
    string = ''
    for line in matrix:
        string += ' '.join([str(x) for x in line]) + '\n'
    print(string)


matrixRotation([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],
               [13, 14, 15, 16], [17, 18, 19, 20]], 2)
