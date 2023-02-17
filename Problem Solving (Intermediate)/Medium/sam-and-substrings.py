MOD = pow(10, 9) + 7


def mod(x):
    return x % MOD


def substrings(n):
    # Write your code here
    l = len(n) + 1
    r = 0
    DP = [0 for i in range(l)]
    for i in range(1, l):
        DP[i] = mod(mod(DP[i - 1] * 10) + mod(i * int(n[i - 1])))
        r = mod(r + DP[i])
    return r


print(substrings("123"))
