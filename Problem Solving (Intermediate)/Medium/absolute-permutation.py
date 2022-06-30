#  k = |pos(i) - i|
# with k = 0 -> pos(i) == i -> n % 1
# with k = 1 -> (1, 2), ... -> n % 2
# with k = 2 -> (1, 3), (2, 4), ... -> n % 4
import math


def absolutePermutation(n, k):
    # Write your code here
    if k != 0 and n % (2 * k):
        return [-1]
    result = []
    for i in range(1, n + 1):
        if k != 0 and (
            (i % k and not math.floor(i / k) % 2)
            or (not i % k and math.floor(i / k) % 2)
        ):
            result.append(i + k)
        else:
            result.append(i - k)

    return result


print(absolutePermutation(3, 0))
