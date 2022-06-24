import math


def extraLongFactorials(n: int):
    # Write your code here
    runner = 3
    arr = [1]
    for i in range(2, n + 1):
        temp1 = 0
        for j in range(len(arr)):
            temp2 = arr[j] * i + temp1
            arr[j] = temp2 % pow(10, runner)
            temp1 = math.floor(temp2 / pow(10, runner))
        if temp1 != 0:
            arr.append(temp1)
    result = str(arr[len(arr) - 1])
    for i in range(len(arr) - 2, -1, -1):
        temp = str(arr[i])
        while len(temp) != runner:
            temp = "0" + temp
        result += temp
    print(result)


extraLongFactorials(8)
