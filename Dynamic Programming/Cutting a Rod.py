import sys
import random



def cuttingRod(N, prices):
    prevs = {}
    def solve(n):
        if n in prevs:
            return prevs[n]
        if n == 0:
            return 0

        sums = []

        for length, price in enumerate(prices):
            length += 1
            if length > n:
                continue

            sums.append(price + solve(n-length))

        res = max(sums)
        prevs[n] = res
        return res

    return solve(N)



for i in range(100):
    prevs = {}
    arr = [random.randint(1, j*10) for j in range(1, 22)]
    size = len(arr)
    print(arr)
    print(cuttingRod(size, arr))
