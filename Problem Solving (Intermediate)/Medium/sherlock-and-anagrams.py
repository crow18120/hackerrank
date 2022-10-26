def initialDictChars(s):
    dict = {}
    for index in range(len(s)):
        if dict.get(s[index]):
            dict[s[index]].append(index)
        else:
            dict[s[index]] = [index]
    return dict


def sherlockAndAnagrams(s):
    # Write your code here
    dictS = initialDictChars(s)

    for (k, v) in dictS.items():
        if len(v) == 1:
            continue
        print(k, v)


print(sherlockAndAnagrams("abcba"))
