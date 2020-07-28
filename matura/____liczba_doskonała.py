from math import sqrt


# suma dzienkiów równa sie ta liczba


def perfectbumer(n):
    res = 1
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            # bo jak sprawdzsz jeden dzielnik to automatycznie z n/i wychodzi drugi np n = 28 --- 4 + 28/4 == 4 + 7
            res += i + n/i

    return res == n


print(perfectbumer(137438691328))
