def almostSorted(arr: list):
    # Write your code here
    indexArr = []
    arrayOfIndexArr = []

    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            indexArr.append(i - 1)
        if arr[i] > arr[i - 1] and len(indexArr) > 0:
            indexArr.append(i - 1)
            arrayOfIndexArr.append(indexArr)
            indexArr = []
    if i == len(arr) - 1 and arr[i] < arr[i - 1]:
        indexArr.append(i)
        arrayOfIndexArr.append(indexArr)
        indexArr = []

    print(arrayOfIndexArr)

    if len(arrayOfIndexArr) == 0:
        print("yes")
    elif len(arrayOfIndexArr) == 1:
        checkReverse(arr, arrayOfIndexArr[0])
    elif len(arrayOfIndexArr) == 2:
        checkSwap(arr, arrayOfIndexArr[0], arrayOfIndexArr[1])
    else:
        print("no")


# indexArr store indexes in arr which to reverse.
def checkReverse(arr: list, indexArr: list):
    lenArr = len(arr)
    lenIndexArr = len(indexArr)
    # initial 2 elements cover indexArr
    left, right = (
        (arr[0] if indexArr[0] == 0 else arr[indexArr[0] - 1]),
        (
            arr[lenArr - 1]
            if indexArr[lenIndexArr - 1] == lenArr - 1
            else arr[indexArr[lenIndexArr - 1] + 1]
        ),
    )
    if (left < arr[indexArr[lenIndexArr - 1]] or left == arr[indexArr[0]]) and (
        right > arr[indexArr[0]] or right == arr[indexArr[lenIndexArr - 1]]
    ):
        print("yes")
        if lenIndexArr == 2:
            print("swap", indexArr[0] + 1, indexArr[1] + 1)
        else:
            print("reverse", indexArr[0] + 1, indexArr[lenIndexArr - 1] + 1)
    else:
        print("no")


def checkSwap(arr: list, indexArr1: list, indexArr2: list):
    lenIndexArr1 = len(indexArr1)
    lenIndexArr2 = len(indexArr2)
    if (
        lenIndexArr1 == lenIndexArr2 == 2
        and arr[indexArr2[0]] < arr[indexArr1[0]]
        and arr[indexArr1[1]] > arr[indexArr2[1]]
    ):
        print("yes")
        print("swap", indexArr1[0] + 1, indexArr2[1] + 1)
    else:
        print("no")


almostSorted([3, 1, 2])
