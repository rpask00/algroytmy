from math import sqrt


def perfectbumer_frajerskie(n):
    res = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            res.append(i)

    return sum(res) == n


def perfectbumer(n):
    res = 1
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            # bo jak sprawdzsz jeden dzielnik to automatycznie z n/i wychodzi drugi np n = 28 --- 4 + 28/4 == 4 + 7
            res += i + n/i

    return res == n


print(perfectbumer(137438691328))
print(perfectbumer_frajerskie(137438691328))
