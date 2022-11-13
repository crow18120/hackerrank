def cost(B):
    # Write your code here
    A = [
        (B[i] - 1) if i == 0 or i == len(B) - 1 else (2 * B[i] - 2)
        for i in range(len(B))
    ]
    P = [0 for i in range(len(B))]
    P[0], P[1] = A[0], max(A[0], A[1])
    for i in range(2, len(A)):
        P[i] = max(P[i - 2] + A[i], P[i - 1])
    print(A, P)
    return P[len(A) - 1]

s = "50 41 48 69 35 11 36 38 73 34 26 13 39 94 7 13 92 54 55 86 14 90 76 78 36 70 93 76 16"
a = list(map(lambda x: int(x), s.split(" ")))
print(cost(a))
