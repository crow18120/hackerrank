def initialDictChars(s):
    arr = []
    dictS = {}
    for index in range(len(s)):
        if dictS.get(s[index]):
            dictS[s[index]] += 1
        else:
            dictS[s[index]] = 1
            dictS = dict(sorted(dictS.items()))
        arr.append(dictS.copy())
    return arr, dictS


def getDictSubstring(arr, i, j):
    if j == 0:
        return arr[i + j - 1]
    dict = {}
    for k in arr[i + j - 1].keys():
        if arr[j - 1].get(k):
            remainV = arr[i + j - 1][k] - arr[j - 1][k]
            if remainV:
                dict[k] = remainV
        else:
            dict[k] = arr[i + j - 1][k]
    return dict


def checkDictSubstring(dict, keys):
    for key in dict.keys():
        if key not in keys:
            return False
    return True


def compareDictSubstrings(dictX, dictY, l):
    iX, iY = dictX['index'], dictY['index']
    x, y = dictX['dict'], dictY['dict']
    if abs(iX - iY) < l:
        return 0
    compareDict = {k: x[k] - y[k] for k in x if k in y and x[k] == y[k]}
    if len(compareDict) == len(x):
        if abs(iX - iY) == l:
            return 1
        else:
            return 2
    else:
        return 0


def sherlockAndAnagrams(s):
    # Write your code here
    arr, dict = initialDictChars(s)
    filterKeys = []
    result = 0
    for key, val in dict.items():
        if val > 1:
            filterKeys.append(key)

    for l in range(1, int(len(s)/2) + 1):
        arrTemp = []
        for i in range(len(arr) - l + 1):
            dict = getDictSubstring(arr, l, i)
            if checkDictSubstring(dict, filterKeys):
                arrTemp.append({'dict': dict, 'index': i})
        for i in range(len(arrTemp) - 1):
            for j in range(i + 1, len(arrTemp)):
                result += compareDictSubstrings(arrTemp[i], arrTemp[j], l)

    return result


print(sherlockAndAnagrams("ifailuhkqq"))
