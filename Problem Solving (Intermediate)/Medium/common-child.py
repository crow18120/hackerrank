# Use Longest Common Subsequence (LCS) algorithm
# With 2 string X = {x1,x2,...,xi}, Y = {y1,y2,...,yj}, prefixes of X is X1,X2,...,Xi and prefixes of Y is Y1,Y2,...,Yj
# LCS(Xi,Yj) displays the longest common subsequence of Xi, Yi and LCS(Xi, Yi) is set by:
#                   ⊘ if i == 0 or j == 0
#   LCS(Xi,Yj) =    LCS(Xi-1, Yj-1) if i,j > 0 and xi == yj
#                   max{LCS(Xi-1,Yj),LCS(Xi,Yj-1)}  if i,j > 0 and xi != yj


def LCS(x: str, y: str):
    if x == y:
        return len(x)
    w, h = len(x) + 1, len(y) + 1
    arr = [[0 for i in range(w)] for j in range(h)]
    for j in range(h - 1):
        for i in range(w - 1):
            arr[j + 1][i + 1] = (
                max(arr[j][i + 1], arr[j + 1][i]) if x[i] != y[j] else arr[j][i] + 1
            )
    return arr[h - 1][w - 1]


def commonChild(x: str, y: str):
    w, h = len(x) + 1, len(y) + 1
    currentArr = [0 for i in range(w)]
    previousArr = [0 for i in range(w)]
    for j in range(h - 1):
        for i in range(w - 1):
            if x[i] != y[j]:
                currentArr[i + 1] = (
                    previousArr[i + 1]
                    if previousArr[i + 1] > currentArr[i]
                    else currentArr[i]
                )
            else:
                currentArr[i + 1] = previousArr[i] + 1
            previousArr[i] = currentArr[i]
        previousArr[w - 1] = currentArr[w - 1]
    return currentArr[w - 1]


print(
    commonChild(
        "ASCD",
        "ACB",
    )
)
