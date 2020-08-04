def binarystrings(n):
    base = [2, 3, 5]

    while len(base) < n:
        base.append(base[-2] + base[-1])

    return base[n-1]




for i in range(1, 65):
    print(binarystrings(i))
