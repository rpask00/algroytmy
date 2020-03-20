def fib(n):
    if n < 3:
        return 1
    return fib(n-2)+fib(n-1)


def fib_frajerskie(n):
    ciag = [1, 1]

    while (n-3):
        n -= 1
        ciag.append(ciag[-2] + ciag[-1])

    return ciag[-2]+ciag[-1]


print(fib_frajerskie(50))
print(fib(50))
