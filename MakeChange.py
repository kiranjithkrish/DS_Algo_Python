def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for amount in range(n+1)]
    ways[0] = 1
    for denomination in denoms:
        for amount in range(1, n+1):
            if denomination <= amount:
                ways[amount] += ways[amount-denomination]
    return ways[n]


print(numberOfWaysToMakeChange(25, [15, 1, 5, 10, 25]))