numbersOfWays = [0, 1, 1, 1, 2]
primes = [2, 3]
   
def getWaysMaker(n):
    for i in range(len(numbersOfWays), n + 1):
        numbersOfWays.append(numbersOfWays[i - 1] + numbersOfWays[i - 4])
 
    return numbersOfWays[n]
 
def checkPrime(n):
    for i in range(len(primes)):
        prime = primes[i]
        if prime * prime > n:
            break
        if n % prime == 0:
            return
    primes.append(n)
  
def getPrimes(n):
    for i in range(primes[-1] + 2, n + 1, 2):
        checkPrime(i)
 
    res = 0
    for i in range(len(primes)):
        if n >= primes[i]:
            res += 1
        else:
            break
    return res

def redJohn(n):
    return getPrimes(getWaysMaker(n))