# Note: With n elements, each step add 1, 2 or 5 to (n - 1) elements.

def equal_1(arr):
    # Write your code here
    arr.sort()
    otps = []
    runner = 0
    # Pre loop.
    # If arr = [1,5,6,...] or [1,4,5,...] => we only take 2 steps for turn 1 to 4 or 5.
    # But with arr = [1,5,5,6...] or ... => we will take 2*n steps for turn 1 to 5s (n: number of 5)
    #  => to reduce we add 2nd element with 1 and we will take only n steps for turn 1 to 6s.
    #  However, after we add 1 or 2 for 2nd to nth element -> we will take more steps for make another become equal.
    # we will discuss about this problem in 2nd function.
    arr[0] -= 1
    print(arr)
    if arr[1] - arr[0] == 3:
        otps.append(2)
        runner += 2
    elif arr[1] - arr[0] == 4:
        otps.append(1)
        runner += 1
    for i in range(1, len(arr)):
        arr[i] += runner
        if arr[i] == arr[i - 1]:
            continue
        dif = arr[i] - arr[i-1]
        s5 = int(dif/5)
        otp = [5 for i in range(s5)]
        remain = dif % 5
        remain == 4 and otp.extend([2, 2])
        remain == 3 and otp.extend([2, 1])
        1 <= remain <= 2 and otp.append(remain)
        otps.extend(otp)
        runner += dif
    return len(otps)

# After making my first function equal, I realised that each loop count steps which spend making (i-1)-th element become i-th element.
# => After making (i-1)-th element = i-th element, the distance from (i-1)-th and (i+1)-th is immutable
# => the steps to make from 1st element become nth element is immutable.
# Comeback to issue with 1st function, I cannot count easily steps changes when I add 1 or 2 into 2nd => nth elements.
# Now the steps will be easy to count because the amount of steps to make 1st element -> nth element is adding 1 step or not change.
#  Example: I will call about the dif from 1st to nth element is x.
#  if x = 2 => take 1 step, but after adding, x = 3 => take 2 steps: 1 and 2
#  if x = 3 => take 2 steps, after adding, x = 4 => still take 2 steps: 2 and 2.
#  2nd fn will count steps based on the dif from 1st to nth.


def equal(arr):
    m = min(arr)
    difs = [0 for i in range(5)]
    factor = [1, 1, 1, 2, 2]
    stepAdd5 = 0
    dif0s = 0
    for val in arr:
        dif = val - m
        if dif:
            difs[dif % 5] += 1
            stepAdd5 += int(dif/5) if (dif % 5) else int(dif/5) - 1
        else:
            dif0s += 1

    difArr = [difs]
    # Add 1 into 2nd to nth element, number difs change...
    difArr.append([difs[4], difs[0] + dif0s - 1, difs[1], difs[2], difs[3]]) 
    # Add 2 into 2nd to nth element, number difs change...
    difArr.append([difs[3], difs[4], difs[0] + dif0s - 1, difs[1], difs[2]])

    addR = [stepAdd5, stepAdd5 + 1 + difs[0], stepAdd5 + 1 + difs[0] + difs[4]]
    r = [sum([difArr[j][i] * factor[i] for i in range(5)]) + addR[j] for j in range(len(difArr))]
    return min(r)


s = "1 1 5 5"
a = s.split(" ")
a = list(map(lambda x: int(x), a))
print(equal(a))
