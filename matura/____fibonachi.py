prevs = {}


def fib(n):
    if n in prevs:
        return prevs[n]

    if n < 3:
        result = 1
    else:
        result = fib(n-2)+fib(n-1)

    prevs[n] = result
    return result


