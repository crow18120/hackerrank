MOD = pow(10, 9) + 7


def mod(x):
    return x % MOD


def countArray(n, k, x):
    # Return the number of ways to fill in the array.
    DP = [0 for i in range(n)]
    (DP[0], DP[1]) = (1, 0) if x == 1 else (0, 1)
    for i in range(2, n):
        DP[i] = mod(mod(DP[i - 1] * (k - 2)) + mod(DP[i - 2] * (k - 1)))
    return DP[n - 1]


print(countArray(5, 4, 1))
