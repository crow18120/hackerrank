

def stockmax(prices):
    # Write your code here
    lenPrices = len(prices)
    sellIndex = []
    runnerIndex = 0
    goods = 0
    res = 0

    # Get day to sell
    maxIndex = 0
    while maxIndex < lenPrices:
        for i in range(maxIndex, lenPrices):
            if prices[i] > prices[maxIndex]:
                maxIndex = i
                
        sellIndex.append(maxIndex)
        maxIndex += 1

    for i in range(lenPrices):
        if i == sellIndex[runnerIndex]:
            res += goods * prices[i]
            goods = 0
            runnerIndex += 1
            continue
        goods += 1
        res -= prices[i]
    
    return res

print(stockmax([1, 3 , 1, 2]))