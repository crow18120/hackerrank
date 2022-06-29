def biggerIsGreater(w: str):
    # Write your code here
    chars = []
    chars.extend(w)
    isValid = False
    switchIndex = 0

    for i in range(len(chars) - 1):
        if chars[i] < chars[i + 1]:
            isValid = True
            switchIndex = i

    if not isValid:
        return "no answer"

    switchChar = chars[switchIndex]
    switchedIndex = 0
    for i in range(switchIndex + 1, len(chars)):
        if chars[i] > switchChar and (not switchedIndex or chars[i] < chars[switchedIndex]):
            switchedIndex = i
    
    # switch char
    chars[switchIndex] = chars[switchedIndex]
    chars[switchedIndex] = switchChar

    #  sort
    for i in range(switchIndex + 1, len(chars) - 1):
        for j in range(i + 1, len(chars)):
            if chars[i] > chars[j]:
                temp = chars[i]
                chars[i] = chars[j]
                chars[j] = temp

    return ''.join(chars)


print(biggerIsGreater("dkhc"))
