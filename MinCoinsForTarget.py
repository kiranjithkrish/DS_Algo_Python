def minNumberOfCoinsForChange(n, denoms):
    minCoins = list(range(0, n+1))
    for denomination in denoms:
        for amount in range(0, n+1):
            if denomination<=amount and amount%denomination == 0:
                minCoins[amount] = min(minCoins[amount], 1+minCoins[amount-denomination])
    return minCoins[n]

print(minNumberOfCoinsForChange(3, [2,1]))