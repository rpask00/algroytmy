import random


def jump(steps):
    destination = len(steps)-1
    prevs = {}

    def solve(position=0):
        if position >= destination:
            return 0

        if position in prevs:
            return prevs[position]

        res = []

        for i in range(1, steps[position]+1):
            res.append(1 + solve(position+i))

        result = min(res)
        prevs[position] = result
        return result

    return solve()


arr = [random.randrange(1, 15) for x in range(30)]
print(jump(arr))
