def koDDDDuj(txt, key):
    nowy = ''
    for t in txt:
        if ord(t) + key > 126:
            symbol = chr(126 - (ord(t) + key) + 64 + key)
        else:
            symbol = chr(ord(t) + key)
        nowy += symbol

    return nowy


def deKoDDDDuj(txt, key):
    nowy = ''
    for t in txt:
        if ord(t) - key < 64:
            symbol = chr(126 - (ord(t) + key - 64) + key)
        else:
            symbol = chr(ord(t) - key)
        nowy += symbol

    return nowy


print(koDDDDuj('ricochet', 5))
print(deKoDDDDuj('wnhthmjy', 5))
