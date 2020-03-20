import math
eps = 0.0000001


def pierwiastek(N, a=1, space=False):
    print('N:', N, ' a:', a)
    if not space:
        space = N

    # jak roznia miedzy bokami prostokąta jest mniejsza niz ustalona wartość to zwracany jest ten bok
    if math.fabs(N - a) < eps:
        return round(N, 8)
    else:
        N = (N + a) / 2
        a = space/N
        return pierwiastek(N, a, space)


print(pierwiastek(3))


# przykład z 3:

# N: 3  a: 1
# N: 2.0  a: 1.5
# N: 1.75  a: 1.7142857142857142
# N: 1.7321428571428572  a: 1.7319587628865978
# N: 1.7320508100147274  a: 1.7320508051230272
# 1.73205081
