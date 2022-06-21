def hackerlandRadioTransmitters(x: list, k: int):
    # Write your code here
    pos = []                # An array to store position 
    x.sort()                # Sort list x from the smallest to the biggest element.
    currentPos = x[0] + k   # Current position will declare the middle point. Exp: 1,2,3,4,5 => currentPos = 3 with k = 2.
    i = 0                   # Because with 'for in range()' I can't change the value of i, so that I use while loop.
    while i < (len(x)):
        # if in list x has element equal to currentPos -> store it in pos. 
        # In some case, the pos stores 2 times currentPos value -> add conditions to store it. 
        if x[i] == currentPos and (len(pos) == 0 or currentPos != pos[len(pos) - 1]):
            pos.append(x[i])
        # if in list doesn't has currentPos, I will fine the nearest element to the left of currentPos.
        #   Case 1: the element > currentPos but still in the range of k -> store the nearest element and change currentPos.
        if x[i] > currentPos and 0 < x[i] - currentPos <= k:
            if len(pos) == 0 or pos[len(pos) - 1] != currentPos:
                pos.append(x[i - 1])
                currentPos = x[i - 1]
                i -= 1
        #   Case 2: the element > currentPos but not in the range of k -> store the new currentPos base on new element + k.
        if x[i] > currentPos and x[i] - currentPos > k:
            # This action to store pos when 2 elements are out of range k. 
            # For exp: 9,15,100 with k = 2 and currrentPos = 11 -> will change to 17 and 102 without store 15 into array pos.
            if len(pos) == 0 or pos[len(pos) - 1] != currentPos:
                pos.append(x[i - 1]) 
                currentPos = x[i - 1]
            else:
                currentPos = x[i] + k
            i -= 1
        i += 1
    if currentPos - x[len(x) - 1] > 0:
        pos.append(x[len(x) - 1])
    return len(pos)


s = "7 2 4 6 5 9 12 11"
hackerlandRadioTransmitters(list(map(lambda i: int(i), s.split(" "))), 2)
