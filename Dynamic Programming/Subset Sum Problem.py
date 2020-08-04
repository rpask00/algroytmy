prevs = {}


def sumproblem(arr, val, index=0, s=0):
    key = f'{index}-{s}'
    if key in prevs:
        print('s')
        return prevs[key]

    if s == val:
        result = True

    elif s > val:
        result = False

    elif index == len(arr):
        result = False

    else:
        current = arr[index]
        result = sumproblem(arr, val, index+1, s + current) or sumproblem(arr, val, index+1, s)

    prevs[key] = result
    return result


s = [3, 34, 4, 12, 11, 4,4,7,4,3,2,12,3,5,6]
print(sumproblem(s, 33))
