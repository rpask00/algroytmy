def initialVal(matrix):
    height = len(matrix)
    width = len(matrix[0])
    lmax = width-1
    bmax = height-1

    dp = [[0 for i in range(width)] for x in range(height)]

    for y in range(bmax, -1, -1):
        for x in range(lmax, -1, -1):

            if x == lmax and y == bmax:
                dp[y][x] = max([1-matrix[y][x], 1])
                continue

            elif x == lmax:
                dp[y][x] = max([dp[y+1][x] - matrix[y][x], 1])

            elif y == bmax:
                dp[y][x] = max([dp[y][x+1] - matrix[y][x], 1])
            else:
                min_on_exit = min([dp[y+1][x], dp[y][x+1]])
                dp[y][x] = max([min_on_exit - matrix[y][x], 1])

    return dp[0][0]


print(initialVal([
    [1, -2, -3, 7, -2, 3],
    [9, 1, 2, 7, -6, 7],
    [-1, 8, -3, 9, -2, 3],
    [5, -5, -4, -8, 1, 4]]))

print(initialVal(
    [[-2, -3, 3],
     [-5, -10, 1],
     [10, 30, -5]]
))
