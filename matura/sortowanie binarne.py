import random
tab = [162]

# generownaie tablicy z losowymi watrtosciami
for i in range(100):
    tab.append(random.randrange(0,200))

qsort = lambda arr: qsort([x for x in arr[1:] if x < arr[0]]) + [arr[0]] + qsort([x for x in arr[1:] if arr[0] < x]) if arr else []

# sortowanie tablicy
tab = qsort(tab)
print(tab)


def findX(x, arr=tab, start=0):
    index = int(len(arr) / 2)

    if x == arr[index]:
        return index + start

    if len(arr) == 1:
        return -1

    else:
        if x > arr[index]:
            tablica = arr[index:]
            start+=index
        else:
            tablica = arr[:index]
            # start-=index

        return findX(x, tablica.copy(), start)

print(findX(162))
