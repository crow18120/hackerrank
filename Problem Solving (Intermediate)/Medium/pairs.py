import math

# Note: each element in arr is unique.
def sortList(x):
    x.sort()
    return x


def pairs(k, arr):
    # Write your code here
    result = 0
    settingPairs = [[] for i in range(k)]
    for val in arr:
        settingPairs[val % k].append(int(val/k))

    settingPairs = list(map(lambda x: sortList(x), settingPairs))
    
    for pair in settingPairs:
        for i in range(1, len(pair)):
            if pair[i] - pair[i - 1] == 1:
                result += 1

    return result

pairs(2, [1, 5, 3, 4, 2])
