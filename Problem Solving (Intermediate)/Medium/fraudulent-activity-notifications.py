def posMedian(d: int):
    return [int(d/2) + 1] if bool(d % 2) else [int(d/2), 1]


def initializeSet(expenditure: list, d: int):
    # Use counting sort
    sortSet = dict()
    for ele in expenditure[:d]:
        sortSet[ele] = 1 if not sortSet.get(ele) else sortSet[ele] + 1
    sortKeys = sorted(sortSet.keys())
    return sortSet, sortKeys

# Dict in python when add new key not sorting as Object in Javascript.
# So I create Array Keys to sorting Dict Keys
# I can make sorted dick but I think it will run out of time. 
# (Actually, it still in time. Another solution in the end.)
def genNewKeys(sortKeys: list, enqueueEle: int, dequeueEle: int):
    newKeys = []
    isInsert = True
    for val in sortKeys:
        if val > enqueueEle:
            newKeys.append(enqueueEle)
            isInsert = False
        if val != dequeueEle:
            newKeys.append(val)
    isInsert and newKeys.append(enqueueEle)
    return newKeys


def genNewSet(sortSet: dict, sortKeys: list, dequeueEle: int, enqueueEle: int):
    if dequeueEle != enqueueEle:
        sortSet[dequeueEle] -= 1
        if not sortSet.get(enqueueEle):
            sortSet[enqueueEle] = 1
            sortKeys = genNewKeys(sortKeys, enqueueEle, -1) if sortSet[dequeueEle] > 0 else genNewKeys(
                sortKeys, enqueueEle, dequeueEle)
        else:
            sortSet[enqueueEle] += 1
    return sortSet, sortKeys


def getMedian(sortSet: dict, sortKeys: list, pos: list):
    num = []
    temp = pos[0]
    isBreak = False
    for i in sortKeys:
        temp -= sortSet[i]
        isBreak and num.append(i)
        if len(num) == len(pos):
            break
        if (temp <= 0 and len(pos) == 1):
            num.append(i)
        elif (temp < 0 and len(pos) == 2):
            num.extend([i, i])
        elif (temp == 0 and len(pos) == 2):
            num.append(i)
            isBreak = True
    return sum(num)/len(num)


def activityNotifications(expenditure, d):
    # Write your code here
    r = 0
    dataSet, dataKey = initializeSet(expenditure, d)
    pos = posMedian(d)
    for i in range(d, len(expenditure)):
        median = getMedian(dataSet, dataKey, pos)
        if expenditure[i] >= median * 2:
            r += 1
        dataSet, dataKey = genNewSet(
            dataSet, dataKey, expenditure[i - d], expenditure[i])
    return r


print(activityNotifications([2, 0, 3, 4, 2, 3, 6, 8, 4, 5], 5))

# Using dict(sorted(sortSet.items())) to make dict with sorted keys.
# def posMedian(d: int):
#     return [int(d/2) + 1] if bool(d % 2) else [int(d/2), 1]


# def initializeSet(expenditure: list, d: int):
#     # Use counting sort
#     sortSet = dict()
#     for ele in expenditure[:d]:
#         sortSet[ele] = 1 if not sortSet.get(ele) else sortSet[ele] + 1
#     return dict(sorted(sortSet.items()))


# def genNewSet(sortSet: dict, dequeueEle: int, enqueueEle: int):
#     if dequeueEle != enqueueEle:
#         sortSet[dequeueEle] -= 1
#         if not sortSet.get(enqueueEle):
#             sortSet[enqueueEle] = 1
#             return dict(sorted(sortSet.items()))
#         else:
#             sortSet[enqueueEle] += 1
#     return sortSet


# def getMedian(sortSet: dict, pos: list):
#     num = []
#     temp = pos[0]
#     isBreak = False
#     for i in sortSet.keys():
#         temp -= sortSet[i]
#         isBreak and num.append(i)
#         if len(num) == len(pos):
#             break
#         if (temp <= 0 and len(pos) == 1):
#             num.append(i)
#         elif (temp < 0 and len(pos) == 2):
#             num.extend([i, i])
#         elif (temp == 0 and len(pos) == 2):
#             num.append(i)
#             isBreak = True
#     return sum(num)/len(num)


# def activityNotifications(expenditure, d):
#     # Write your code here
#     r = 0
#     dataSet = initializeSet(expenditure, d)
#     pos = posMedian(d)
#     for i in range(d, len(expenditure)):
#         median = getMedian(dataSet, pos)
#         if expenditure[i] >= median * 2:
#             r += 1
#         dataSet = genNewSet(dataSet, expenditure[i - d], expenditure[i])
#     return r
