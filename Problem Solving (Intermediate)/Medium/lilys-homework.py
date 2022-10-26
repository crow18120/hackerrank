def lilysHomework(arr):
    # Write your code here
    lenArr = len(arr)
    actASC, actDESC = 0, 0
    arrASC = [{'value': arr[i], 'index': i}
              for i in range(lenArr)]

    arrASC.sort(key=lambda x: x['value'])
    arrDESC = list(reversed(arrASC))
    print(arrASC)
    for i in range(lenArr):
        while arrASC[i]['index'] != i:
            temp = arrASC[arrASC[i]['index']]
            arrASC[arrASC[i]['index']] = arrASC[i]
            arrASC[i] = temp
            actASC += 1
        while arrDESC[i]['index'] != i:
            temp = arrDESC[arrDESC[i]['index']]
            arrDESC[arrDESC[i]['index']] = arrDESC[i]
            arrDESC[i] = temp
            actDESC += 1

    return actASC if actASC < actDESC else actDESC


print(lilysHomework([2, 5, 3, 1]))


# Use selection sort to count action (but timeout limit)
# def lilysHomework(arr):
#     # Write your code here
#     ascArr, descArr = arr, arr.copy()
#     ascAct, descAct = 0, 0
#     for i in range(len(arr)):
#         min_i = i
#         max_i = i
#         for j in range(i + 1, len(arr)):
#             if ascArr[min_i] > ascArr[j]:
#                 min_i = j
#             if descArr[max_i] < descArr[j]:
#                 max_i = j

#         if min_i != i:
#             ascArr[i], ascArr[min_i] = ascArr[min_i], ascArr[i]
#             ascAct += 1
#         if max_i != i:
#             descArr[i], descArr[max_i] = descArr[max_i], descArr[i]
#             descAct += 1
#     return ascAct if ascAct < descAct else descAct
