import math

MOD = pow(10, 9) + 7
globalVariable = {"charsPerIndex": [], "maxN": 0, "facts": [], "invfacts": []}


def fermat_binom(n: int, k: int, p: int):
    if k > n:
        return 0

    beginNum = k + 1 if n - k > k else n - k + 1
    endNum = n - k if n - k > k else k

    # calculate numerator
    num = 1
    for i in range(n, endNum, -1):
        num = (num * i) % p

    # calculate denominator
    denom = 1
    for i in range(1, beginNum):
        denom = (denom * i) % p

    # numerator * denominator^(p-2) (mod p)
    return (num * pow(denom, p - 2, p)) % p


# Using Fermat's little theorem to pre-compute factorials and inverses
# Note: only works when p is prime and k < p
def fermat_compute(n, p):
    facts = [0] * (n + 1)
    invfacts = [0] * (n + 1)

    facts[0] = 1
    invfacts[0] = 1
    for i in range(1, n + 1):
        # calculate factorial and corresponding inverse
        facts[i] = (facts[i - 1] * i) % p
        invfacts[i] = pow(facts[i], p - 2, p)

    return facts, invfacts


# Compute binomial coefficient from given pre-computed factorials and inverses
def binom_pre_computed(facts, invfacts, n, k, p):
    # n! / (k!^(p-2) * (n-k)!^(p-2)) (mod p)
    return (facts[n] * ((invfacts[k] * invfacts[n - k] % p))) % p


def initialize(s: str):
    chars = {}
    for i in s:
        chars[i] = chars[i] + 1 if i in chars else 1
        globalVariable["charsPerIndex"].append(chars.copy())
    for i in chars:
        element = chars[i]
        if element >= 2:
            globalVariable["maxN"] = globalVariable["maxN"] + math.floor(element / 2)
    globalVariable["facts"], globalVariable["invfacts"] = fermat_compute(
        globalVariable["maxN"], MOD
    )


def fermat_binom_arr(arr: list):
    n = arr[len(arr) - 1]
    result = 1
    for i in range(len(arr) - 2, 0, -1):
        result = (
            result
            * binom_pre_computed(
                globalVariable["facts"], globalVariable["invfacts"], n, arr[i], MOD
            )
            % MOD
        )
        n -= arr[i]
    return result


def answerQuery(l: int, r: int):
    charsL = globalVariable["charsPerIndex"][l - 2] if l - 2 >= 0 else {}
    charsR = globalVariable["charsPerIndex"][r - 1]
    singleChars = 0
    totalMultiChars = 0
    repeatChar = []
    for i in charsR:
        element = charsL[i] if i in charsL else 0
        remainEle = charsR[i] - element
        if remainEle % 2:
            singleChars += 1
        if remainEle >= 2:
            repeatChar.append(math.floor(remainEle / 2))
            totalMultiChars += math.floor(remainEle / 2)
    repeatChar.sort()
    combination_result = fermat_binom_arr([*repeatChar, totalMultiChars])
    return combination_result * singleChars % MOD if singleChars else combination_result
