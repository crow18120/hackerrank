def getWays(n, c):
    # Write your code here
    runEnv = [[0 for i in range(len(c))] for j in range(n+1)]
    c.sort()
    for i in range(1, len(runEnv)):
        for j in range(len(c)):
            if i == c[j]:
                runEnv[i][j] = 1
            elif i > c[j]:
                runEnv[i][j] = sum(runEnv[i - c[j]][:j+1])
    return sum(runEnv[n])


print(getWays(10, [2, 3, 5, 6]))
