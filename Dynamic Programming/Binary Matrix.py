def printMaxSubSquare(M):
    def is_in_square(x, y):
        if x is 0 or y is 0:
            return M[y][x]

        cords = []
        cords.append(M[y-1][x-1])
        cords.append(M[y-1][x])
        cords.append(M[y][x-1])

        res = 0 not in cords

        return res if res else M[y][x]

    auxiliary = [[0 for i in range(len(M[0]))] for x in range(len(M))]

    # maxval = (0, 0, 0)
    for y, row in enumerate(M):
        for x, cell in enumerate(row):
            if y == 4 and x ==3:
                print('a')
            issquere = is_in_square(x, y)
            print(issquere)
            if issquere:
                auxiliary[y][x] = 1
                if issquere == True:
                    cords = set()
                    cords.add(auxiliary[y-1][x-1])
                    cords.add(auxiliary[y-1][x])
                    cords.add(auxiliary[y][x-1])

                    if len(cords) == 1:
                        auxiliary[y][x] = cords.pop() + 1

                        # if auxiliary[y][x] > maxval[2]:
                        #     maxval = (x, y, auxiliary[y][x])

    print('end')


M = [[0, 1, 1, 0, 1],
     [1, 1, 0, 1, 0],
     [0, 1, 1, 1, 0],
     [1, 1, 1, 1, 0],
     [1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0]]

printMaxSubSquare(M)
