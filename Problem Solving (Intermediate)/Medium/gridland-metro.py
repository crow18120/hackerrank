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
    tracks.sort(key=lambda x: x[0])
    listTracks = []
    rowTracks = [tracks[0][1:]]
    for i in range(1, len(tracks)):
        if tracks[i][0] != tracks[i-1][0]:
            listTracks.append(rowTracks)
            rowTracks = [tracks[i][1:]]
            continue
        compareTrack = tracks[i][1:]
        for j in range(len(rowTracks)):
            mergeTrack, isSmaller = merge2Track(rowTracks[i], compareTrack)
            if not mergeTrack and isSmaller:
                rowTracks = rowTracks[:j] + [compareTrack] + rowTracks[j:]
            if mergeTrack:
                rowTracks[j] = mergeTrack

print(merge2Track([8, 10], [1, 2]))
