qsort = lambda L: qsort([x for x in L[1:] if x <= L[0]]) + [L[0]] + qsort([x for x in L[1:] if x > L[0]]) if L else []


# def run():
#     from random import randint
#     l = [randint(0, 50) for i in range(10)]
#     print(l)
#     print(qsort(l))


# run()

array = [3,3,3,3,3,3, 3432, 5, 2, 56, 78, 6, 545, 4]
print(qsort(array))