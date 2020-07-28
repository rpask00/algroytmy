import math


def prime(n):

    for i in range(2, n//2+1):
        if n % i is 0:
            return False

    return True


print(prime(12))
