# Note: each element in arr is unique.


def pairs(k, arr):
    # Write your code here
    compareArr = [val - 2 for val in arr]
    result = 0
    for val in arr:
        for compareVal in compareArr:
            if val == compareVal:
                result += 1
                break

    return result
