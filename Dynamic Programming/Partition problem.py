import random


def py(arr, index=0, left=[], right=[]):
    if index == len(arr):
        return sum(left) == sum(right)

    left.append(arr[index])
    if py(arr, index+1, left, right):
        return True

    left.pop()
    right.append(arr[index])
    if py(arr, index+1, left, right):
        return True

    right.pop()
    return False

