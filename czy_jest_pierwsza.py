def prime(n):
    for i in range(2, n // 2 + 1):
        if n % i:
            continue
        else:
            return False
    return True


