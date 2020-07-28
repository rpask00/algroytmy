def czy_jest_palidnromem(w):
    i = 0
    j = len(w)-1

    while i < j:

        if w[i] == ' ':
            i += 1

        if w[j] == ' ':
            j += 1

        if w[i] != w[j]:
            return False

        i += 1
        j -= 1

    return True


def palidnrom_v2(w):
    w = w.lower()
    rev = ''.join(reversed(w))
    return w == rev


print(czy_jest_palidnromem('kobyła ma mały bok'))
