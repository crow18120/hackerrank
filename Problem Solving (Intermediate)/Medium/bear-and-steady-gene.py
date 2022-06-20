def checkValid(runnerChars: dict, replaceChars: dict):
    for k, v in replaceChars.items():
        if runnerChars[k] < v:
            return False
    return True


def getMinimumReplaceGene(gene, replaceChars):
    start = 0  # pointerStart
    end = 0  # pointerEnd
    geneLen = min = len(gene)
    runnerChars = {k: 0 for k, v in replaceChars.items()}
    while start < geneLen and end < geneLen:
        while end < geneLen and not checkValid(runnerChars, replaceChars):
            runnerChars[gene[end]] += 1
            end += 1
        while checkValid(runnerChars, replaceChars):
            runnerChars[gene[start]] -= 1
            start += 1
        min = min if min < end - start + 1 else end - start + 1
    return min

def steadyGene(gene: str):
    # initialize
    chars = {"A": 0, "C": 0, "T": 0, "G": 0}

    geneLen = len(gene)
    limit = int(geneLen / 4)

    for i in gene:
        chars[i] = chars[i] + 1

    # Check spread condition
    if chars["A"] == chars["C"] == chars["T"] == chars["G"]:
        print(0)

    replaceChars = {k: v - limit if v - limit > 0 else 0 for k, v in chars.items()}

    return getMinimumReplaceGene(gene, replaceChars)


# steadyGene("GGAATTTC")
