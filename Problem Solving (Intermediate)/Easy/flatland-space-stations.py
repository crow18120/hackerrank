import math


def flatlandSpaceStations(n: int, c: list):
    # This problem can change to get the longgest middle of two station.
    if len(c) == n:
        return 0

    # Sort list c:
    # for i in range(len(c) - 1):
    #     for j in range(i + 1, len(c)):
    #         if c[i] > c[j]:
    #             temp = c[i]
    #             c[i] = c[j]
    #             c[j] = temp
    #  User python sort to reduce runtime (must improve my sort algorithsm)
    c.sort()

    # Distance from last city to last station:
    lastDistance = n - 1 - c[len(c) - 1]
    result = lastDistance if lastDistance > c[0] else c[0]

    for i in range(1, len(c)):
        temp = math.floor((c[i] - c[i - 1]) / 2)
        result = result if temp < result else temp

    return result


flatlandSpaceStations(20, [13, 1, 11, 10, 6])
