# cz słow składaja sie z tych samych liter
# prosciej sie nie da


def anagram(a, b):
    a = ''.join(sorted(a))
    b = ''.join(sorted(b))

    return a == b
