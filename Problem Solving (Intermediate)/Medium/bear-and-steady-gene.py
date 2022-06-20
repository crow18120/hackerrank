charsPerIndex = []


def steadyGene(gene: str):
    # initialize
    chars = {}
    for i in gene:
        chars[i] = chars[i] + 1 if i in chars else 1
        charsPerIndex.append(chars.copy())
    

steadyGene('GAAATAAA')
