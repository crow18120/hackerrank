import math


def nonDivisibleSubset(k: int, s: list):
    # Write your code here
    remainderArray = [0] * k
    result = 0
    for i in range(len(s)):
        remainderArray[s[i] % k] += 1
    if remainderArray[0] >= 1:
        result += 1
    if k % 2 == 0 and remainderArray[int(k / 2)] >= 1:
        result += 1
    for i in range(1, math.ceil(k / 2)):
        result += max(remainderArray[i], remainderArray[k - i])
    return result


nonDivisibleSubset(1, [1, 2, 3, 4, 5])
