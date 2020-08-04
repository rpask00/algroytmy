def keypad(N):
    moves = {
        0: [0, 8],
        1: [1, 2, 4],
        2: [1, 2, 3, 5],
        3: [2, 3, 6],
        4: [1, 4, 7, 5],
        5: [2, 4, 5, 6, 8],
        6: [3, 5, 6, 9],
        7: [4, 7, 8],
        8: [7, 5, 8, 9, 0],
        9: [6, 8, 9],
    }
    prevs = {}

    def solve(n, previouskey):
        key = f'{n}-{previouskey}'
        if key in prevs:
            return prevs[key]

        result = 0

        if n == 0:
            result = 1
        else:

            for move in moves[previouskey]:
                result += solve(n-1, move)
        
        prevs[key] = result 
        return result

    return sum([solve(N-1, i) for i in range(10)])


print(keypad(34))
