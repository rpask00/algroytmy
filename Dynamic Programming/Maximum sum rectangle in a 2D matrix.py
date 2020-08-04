import sys


def maxSubArraySum(a):
    size = len(a)

    max_so_far = -sys.maxsize - 1
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far


def maxsum2D(matrix):
    COLS = len(matrix[0])
    res = -sys.maxsize

    def mergeMatrixToAcol(left, right):
        if left == right:
            return [row[left] for row in matrix]

        return [sum(row[left:right+1]) for row in matrix]

    for left in range(COLS):
        for right in range(left, COLS):
            runningcolmax = maxSubArraySum(mergeMatrixToAcol(left, right))
            if runningcolmax > res:
                res = runningcolmax

    return res


M = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4,  2,  1],
    [3,  8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]

print(maxsum2D(M))
