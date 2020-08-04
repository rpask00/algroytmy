prevs = {}
def coinChange(n, coins):
    if n in prevs:
        return prevs[n]

    if n == 0:
        result= 0

    else:
        changes = []

        for coin in coins:
            if coin > n:
                continue

            changes.append(1+coinChange(n-coin, coins))

        result =  min(changes)
    prevs[n] = result
    return result



print(coinChange(11,[9, 6, 5, 1] ))
