def larrysArray(A: list, r: int):
    # Write your code here
    numberOfInversions = 0
    for i in range(len(A)):
        for j in range(i, len(A)):
            if A[i] > A[j]:
                numberOfInversions += 1

    if numberOfInversions % (r - 1):
        return "NO"
    return "YES"
