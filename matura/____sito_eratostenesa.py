from math import sqrt, floor

# Sito Eratostenesa – algorytm wyznaczania liczb pierwszych z zadanego przedziału

arr = [True for i in range(600)]


def sito(data):
    for i in range(2, floor(sqrt(len(data)))):
        for j in range(2, len(data)):

            if j % i == 0 and not i == j:
                data[j] = False

    for i, d in enumerate(data):
        if d:
            print(i)


sito(arr)
