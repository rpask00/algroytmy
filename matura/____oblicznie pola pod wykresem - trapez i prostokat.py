import math
# wielomian = [1, 2, -1, 1]
wielomian = [1, 0]


def horner(wsp, st, x):
    if st == 0:
        return wsp[0]

    return x * horner(wsp, st - 1, x) + wsp[st]


def f(v):
    return horner(wielomian, len(wielomian)-1, v)


def pole_prostokąty(start, end, eps):
    result = 0
    while start < end:
        result += math.fabs(f(start+eps/2)*eps)
        start += eps

    return result


print(pole_prostokąty(-3, -2,  0.001))


def pole_trapezy(start, end, eps):
    result = 0
    while start < end:
        result += 1/2 * (math.fabs(f(start)+f(start+eps))) * eps
        start += eps

    return result


print(pole_trapezy(-3, -2, 0.001))
