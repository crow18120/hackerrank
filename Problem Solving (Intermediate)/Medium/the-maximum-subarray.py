def maxSubarray(arr):
    # Write your code here
    subsequence = 0
    subarray = 0
    arrSubarray = []
    maxVal = arr[0]
    for val in arr:
        if val > maxVal:
            maxVal = val
        if val >= 0:
            subsequence += val
            subarray += val
        else:
            subarray > 0 and arrSubarray.append(subarray)
            if subarray + val < 0:
                subarray = 0
            else:
                subarray += val
    subarray > 0 and arrSubarray.append(subarray)

    if subsequence == 0:
        return maxVal, maxVal

    return max(arrSubarray), subsequence


print(maxSubarray([9, -8, 9, -6, 5, -4, 3, -2, 1]))
