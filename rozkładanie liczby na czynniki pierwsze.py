from math import sqrt


def czynniki(n):
    res = []
    i = 2

    while(n != 1):
        if n % i == 0:
            n /= i
            res.append(i)
        else:
            i += 1
    return res


print(czynniki(1520))
