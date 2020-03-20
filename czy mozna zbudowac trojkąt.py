def triangle(a, b, c):
    walls = sorted([a, b, c])
    return walls[0]+walls[1] > walls[2]


print(triangle(3, 3, 4))
