prevs = {}


def stairs(n, ways):
    if n in prevs:
        return prevs[n]

    result = 0
    if n > 0:
        for way in ways:
            result += stairs(n-way, ways)
    elif n == 0:
        result = 1

    prevs[n] = result
    return result


print(stairs(674, [1, 2]))
