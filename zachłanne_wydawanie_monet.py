coins = [0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
result = []


def rest(n):
    while (n > 0.1):
        for i in reversed(coins):
            if n - i >= 0:
                n -= i
                result.append(i)
                break
    return result


print(rest(27.38))
