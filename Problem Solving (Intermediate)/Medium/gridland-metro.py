# Note: A train track may overlap other train tracks within the same row.
def merge2Track(primary: list, secondary: list):
    [a, b], [x, y] = primary, secondary
    dA, dB = x - a, y - b
    # secondary is outside from primary => return False.
    # If secondary is before primary return True else False.
    if y + 1 < a:
        return False, True
    elif b + 1 < x:
        return False, False

    rX = x if dA <= 0 else a
    rY = y if dB >= 0 else b
    return [rX, rY], []


def gridlandMetro(n, m, k, tracks):
    # Write your code here
    total = n * m
    if k == 0:
        return total
    tracks.sort(key=lambda x: x[0])
    print(tracks)
    listTracks = []
    rowTracks = [tracks[0][1:]]
    for i in range(1, k):
        if tracks[i][0] != tracks[i - 1][0]:
            listTracks.append(rowTracks)
            rowTracks = [tracks[i][1:]]
            continue
        compareTrack = tracks[i][1:]
        newRowTracks = []
        isAddCompareTrack = False
        for j in range(len(rowTracks)):
            mergeTrack, isSmaller = merge2Track(rowTracks[j], compareTrack)
            if not mergeTrack:
                if isSmaller:
                    newRowTracks += [compareTrack] + rowTracks[j:]
                    isAddCompareTrack = True
                    break
                else:
                    newRowTracks.append(rowTracks[j])
            if mergeTrack:
                compareTrack = mergeTrack
        if not isAddCompareTrack:
            newRowTracks += [compareTrack]
        rowTracks = newRowTracks
    listTracks.append(rowTracks)

    for rowTracks in listTracks:
        for track in rowTracks:
            total -= track[1] - track[0] + 1
    return total


gridlandMetro(4, 4, 3, [[2, 2, 3], [3, 1, 4], [4, 4, 4]])
