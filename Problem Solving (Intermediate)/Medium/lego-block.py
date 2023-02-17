MOD = pow(10, 9) + 7

def legoBlocks(n, m):
    # n: height
    # m: weight
    #initial number of layers with weight 1 -> 4:
    layers = [1, 2, 4, 8]
    
    for i in range(4, m):
        layers.append(sum(layers[-4:]) % MOD)

    #initial number of combine with layer 1
    total_combine = [1]

    for i in range(1, m):
        total_combine.append(pow(layers[i], n, MOD))
    
    #initial number of suitable with layer 1
    suitable_combine = [1]

    for i in range(1, m):
        run = total_combine[i]
        for j in range(i):
            if i - j < 0:
                break
            run -= (total_combine[i - j - 1] * suitable_combine[j]) % MOD
            run = run if run >= 0 else run + MOD
        suitable_combine.append(run)

    return suitable_combine[-1]

print(legoBlocks(2,5))
