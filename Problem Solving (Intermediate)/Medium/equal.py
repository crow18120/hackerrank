# Note: With n elements, each step add 1, 2 or 5 to (n - 1) elements.

def equal(arr):
    # Write your code here
    arr.sort()
    otps = []
    runner = 0
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
        runner += sum(otp)
    return len(otps)


print(equal([1, 5, 5, 5, 5]))
