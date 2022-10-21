def superReducedString(s):
    # Write your code here
    array = []
    for i in range(len(s)):
        if len(array) != 0 and s[i] == array[len(array) - 1]: 
            array.pop()
        else:
            array.append(s[i])
    return ''.join([str(x) for x in array])

print(superReducedString('aaabccddd'))