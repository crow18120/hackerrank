def posMedian(d):
    return [int(d/2)] if bool(d % 2) else [int(d/2) - 1, int(d/2)]


def initializeSet(expenditure, d):
    sortSet = expenditure[:d]
    sortSet.sort()
    return sortSet


def genNewSet(sortData, dequeueEle, enqueueEle):
    isDequeue = isEnqueue = False
    newSortData = []
    for val in sortData:
        if val == dequeueEle and not isDequeue:
            isDequeue = True
            continue
        if val >= enqueueEle and not isEnqueue:
            isEnqueue = True
            newSortData.append(enqueueEle)
        newSortData.append(val)
    if not isEnqueue:
        newSortData.append(enqueueEle)

    return newSortData


def median(sortData, pos):
    return sum(sortData[i] for i in pos)/len(pos)


def activityNotifications(expenditure, d):
    # Write your code here
    r = 0
    dataSet = initializeSet(expenditure, d)
    pos = posMedian(d)
    for i in range(d, len(expenditure)):
        if expenditure[i] >= median(dataSet, pos) * 2:
            r += 1
        dataSet = genNewSet(dataSet, expenditure[i - d], expenditure[i])

    return r


print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))
