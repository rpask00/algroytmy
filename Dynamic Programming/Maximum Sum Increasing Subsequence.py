import random


def msis(seq):
    maxindex = len(seq)-1

    def solve(big=0, index=0):
        if index > maxindex:
            return 0

        if seq[index] > big:
            return max([seq[index] + solve(seq[index], index+1), solve(big, index + 1)])

        return solve(big, index+1)

    return max([solve(i) for i, s in enumerate(seq)])



for i in range(50):
    arr = [random.randrange(1, 200) for i in range(20)]
    print(msis(arr))
