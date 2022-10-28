def initialChars(s):
    chars = []
    for i in range(len(s)):
        if s[i] not in chars:
            chars.append(s[i])
    return chars


def alternating(s):
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            return 0
    return len(s)


def alternate(s):
    # Write your code here
    chars = initialChars(s)
    arr = [0]
    for i in range(len(chars)):
        for j in range(i + 1, len(chars)):
            tempS = ""
            for k in range(len(s)):
                if s[k] == chars[i] or s[k] == chars[j]:
                    tempS += s[k]
            ele = alternating(tempS)
            ele > 0 and arr.append(ele)
    return max(arr)

print(alternate("beabeefeab"))
