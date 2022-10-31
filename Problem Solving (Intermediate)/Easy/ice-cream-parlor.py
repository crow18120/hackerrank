def icecreamParlor(m, arr):
    # Write your code here
    for i in range(len(arr) - 1):
        runner = m - arr[i]
        for j in range(i + 1, len(arr)):
            if runner == arr[j]:
                return [i + 1, j + 1]
    return [0, 0]