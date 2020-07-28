import random


def print_Coin_Change(S, coins):
    def solve(s, taken):
        if s < 0:
            return 0

        if s == 0:
            print(taken)
            return 1

        for coin in coins:
            solve(s-coin,  taken+[coin])

    solve(S, [])


def Coin_Changes(S, coins):
    def solve(s, index=0):
        if s < 0:
            return 0

        if s == 0:
            return 1

        if index == len(coins):
            return 0
        return solve(s, index+1) + solve(s-coins[index], index)

    return solve(S)


for i in range(100):
    arr = list({random.randrange(1, 20) for i in range(10)})
    S = random.randrange(1, 100)

    print(Coin_Changes(S, arr))
