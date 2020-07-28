import math
eps = 0.0000001


def pierwiastek(a, b=1, space_of_rectangle=False):
    # print('a:', a, ' b:', b)
    if not space_of_rectangle:
        # bo drugi bok ma 1
        space_of_rectangle = a

    # jak roznia miedzy bokami prostokąta jest mniejsza niz ustalona wartość to zwracany jest ten bok
    if math.fabs(a - b) < eps:
        return round(a, 8)
    else:
        a = (a + b) / 2
        b = space_of_rectangle/a
        return pierwiastek(a, b, space_of_rectangle)


print(pierwiastek(3))


# przykład z 3:

# N: 3  a: 1
# N: 2.0  a: 1.5
# N: 1.75  a: 1.7142857142857142
# N: 1.7321428571428572  a: 1.7319587628865978
# N: 1.7320508100147274  a: 1.7320508051230272
# 1.73205081
