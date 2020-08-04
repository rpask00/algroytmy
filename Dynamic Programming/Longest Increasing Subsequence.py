import random


def LIS(Sequnce):
    sequence_resutls = []
    prevs = {}

    def lis(index, big):
        nonlocal prevs
        key = str(index)+'-'+str(big)

        if key in prevs:
            return prevs[key]

        if index == len(Sequnce):
            return 0

        current_val = Sequnce[index]

        temp1 = lis(index+1, big)
        temp2 = 1 + lis(index+1, current_val) if current_val > big else 0

        result = max(temp1, temp2)
        prevs[key] = result

        return result

    for i, s in enumerate(Sequnce):
        sequence_resutls.append(lis(i, 0))
        prevs.clear()

    return max(sequence_resutls)


global maximum


def _lis(arr, n):
    global maximum
    if n == 1:
        return 1
    maxEndingHere = 1

    """Recursively get all LIS ending with arr[0], arr[1]..arr[n-2] 
       IF arr[n-1] is maller than arr[n-1], and max ending with 
       arr[n-1] needs to be updated, then update it"""
    for i in range(1, n):
        res = _lis(arr, i)
        if arr[i-1] < arr[n-1] and res+1 > maxEndingHere:
            maxEndingHere = res + 1

    # Compare maxEndingHere with overall maximum. And
    # update the overall maximum if needed
    maximum = max(maximum, maxEndingHere)

    return maxEndingHere


def lis(arr):
    global maximum
    n = len(arr)
    maximum = 1
    _lis(arr, n)

    return maximum


print(LIS([10, 50, 30, 10, 60, 40]))
for i in range(100):
    arr = [random.randrange(1, 800) for x in range(15)]
    print(arr, LIS(arr) == lis(arr))
    # print(arr, == )
