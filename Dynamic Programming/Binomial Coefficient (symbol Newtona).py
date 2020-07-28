import math


def newton(N, K):
    prevs = {}

    def solve(n, k):
        key = f'{n}-{k}'
        if key in prevs:
            return prevs[key]

        if k == 1:
            result = n
        elif n == k:
            result = 1
        else:
            result = solve(n-1, k-1) + solve(n-1, k)

        prevs[key] = result

        return result

    return solve(N, K)


print(newton(454, 34))
