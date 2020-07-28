def NWD(low, big):
    if low > big:
        low, big = big, low

    rest = low % big

    while rest:
        rest, low = low % rest, rest

    return low

def NWW(a, b):
    return int(a*b / NWD(a, b))


print(NWD(270, 150))
#
