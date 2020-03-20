from ttictoc import TicToc


def power(a, n):
    if n == 1:
        return a
    if n % 2 == 1:
        return a * power(a, n-1)

    w = power(a, n / 2)
    return w * w


t = TicToc('power')
t.tic()
power(2, 156560)
t.toc()  # Prints and returns the elapsed time
print(t.elapsed)


# def frajer(a, n):
#     result = a
#     while n-1:
#         result *= a
#         n -= 1

#     return result


# t = TicToc('frajer')
# t.tic()
# frajer(2, 10)
# t.toc()  # Prints and returns the elapsed time
# print(t.elapsed)
