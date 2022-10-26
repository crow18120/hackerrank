def highestValuePalindrome(s, n, k):
    # Write your code here
    arr = list(s)
    dif = 0
    for i in range(int(n/2)):
        if arr[i] != arr[n - 1 - i]:
            dif += 1
    k -= dif
    if k < 0:
        return '-1'
    for i in range(int(n/2)):
        if arr[i] == arr[n - 1 - i] and arr[i] != '9' and k >= 2:
            arr[i] = arr[n - 1 - i] = '9'
            k -= 2
        elif arr[i] != arr[n - 1 - i] and arr[i] != '9' and arr[n - 1 - i] != '9' and k >= 1:
            arr[i] = arr[n - 1 - i] = '9'
            k -= 1
        else:
            temp = arr[i] if arr[i] > arr[n - 1 - i] else arr[n - 1 - i]
            arr[i] = arr[n - 1 - i] = temp
    if n % 2 and k >= 1:
        arr[int(n/2)] = '9'

    return ''.join(arr)


print(highestValuePalindrome('0011', 4, 2))
