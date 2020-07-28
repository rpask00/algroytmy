import math
wielomian = [4, 5, 3, -3]


# WYCIĄGANIE PRZED NAWIAS
def horner(wielom, st, x):
    # przykład:
    # 4x^3 + 5x^2 + 3x - 3
    # x( 4x^2 + 5x + 3 ) -3
    # x( 4x + 5) +3
    # x( 4 ) + 5
    # 4
    if st == 0:
        return wielom[0]

    return x * horner(wielom, st - 1, x) + wielom[st]


def f(v):
    return horner(wielomian, len(wielomian)-1, v)


def miejsce_zerowe(a, b, eps):
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b

    if math.fabs(a - b) < eps:
        return a

    mid = (a + b) / 2

    if f(a) * f(mid) < 0:
        return miejsce_zerowe(a, mid, eps)
    else:
        return miejsce_zerowe(mid, b, eps)


# print(miejsce_zerowe(0, 6, 0.0000000000001))

print(f(2))
