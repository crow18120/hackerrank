def surfaceArea(A: list):
    # Write your code here
    # Initiate result variable with value Double size of A.
    r, c = len(A), len(A[0])
    result = r * c * 2

    # Calculatate the side area: row.
    for i in range(r):
        if c == 1:
            result += A[i][0] * 2
        else:
            for j in range(c):
                if j == 0 or j == c - 1:
                    result += A[i][j]
                if j != 0:
                    result += abs(A[i][j] - A[i][j - 1])

    #  Calculate the side area: column.
    for j in range(c):
        if r == 1:
            result += A[0][j] * 2
        else :
            for i in range(r):
                if i == 0 or i == r - 1:
                    result += A[i][j]
                if i != 0:
                    result += abs(A[i][j] - A[i - 1][j])

    return result


surfaceArea([[1]])
