def beautifulPairs(A, B):
    # Write your code here
    A.sort()
    B.sort()
    i, j, r = 0, 0, 0
    while (i < len(A) and j < len(B)):
        if A[i] < B[j]:
            i += 1
        elif A[i] > B[j]:
            j += 1
        else:
            r += 1
            i += 1
            j += 1
    return r - 1 if r == len(A) else r + 1
