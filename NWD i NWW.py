def NWD(a, b):
    rest = a % b
    lower = b

    while (rest):
        rest, lower = lower % rest, rest

    return lower


def NWD_rekurencyjnie(a, b, rest=False, lower=False):
    if rest is False:
        rest = a % b
        lower = b

    if not rest:
        return lower

    return NWD_rekurencyjnie(a, b, rest=lower % rest, lower=rest)


def NWW(a, b):
    return int(a*b / NWD_rekurencyjnie(a, b))


print(NWD(270, 150))
# print(NWD_rekurencyjnie(270, 150))
# print(NWW(24, 36))
#
