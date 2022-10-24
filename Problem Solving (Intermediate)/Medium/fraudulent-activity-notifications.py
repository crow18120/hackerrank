def pos(d):
    return [int(d/2)] if bool(d % 2) else [int(d/2) - 1, int(d/2)]


def initializeSet(expenditure, d):
    return expenditure[:d].sort()


def genNewSet(sortData, dequeueEle, enqueueEle):
    isDequeue = isEnqueue = False


def median(sortData):
    pos = pos(len(sortData))
    return sum(sortData[i] for i in pos)/len(pos)


def activityNotifications(expenditure, d):
    # Write your code here
    r = 0
    dataSet = initializeSet(expenditure, d)
    for i in range(d, len(expenditure)):
        if expenditure[i] >= median(dataSet):
            r += 1



