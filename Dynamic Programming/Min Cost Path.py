import sys

prevs = {}

def shortestpath(matrix, destx, desty, x=0, y=0):
    key = f'{x}-{y}'
    if key in prevs:
        return prevs[key]

    if x == len(matrix) or y == len(matrix[0]):
        return sys.maxsize

    cell = matrix[x][y]

    if x == destx and y == desty:
        return cell

    result = cell + min(
        shortestpath(matrix, destx, desty, x+1, y),
        shortestpath(matrix, destx, desty, x+1, y+1),
        shortestpath(matrix, destx, desty, x, y+1)
    )
    prevs[key] = result

    return result

mtr = [
    [1, 4, 1],
    [2, 8, 5],
    [3, 2, 3]
]

print(shortestpath(mtr, 2, 1))
