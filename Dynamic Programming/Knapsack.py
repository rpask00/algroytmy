import random
from ttictoc import TicToc


def knapsack(V, W, K):
    max_val = 0
    previous = {}

    def solve(k, t):
        key = str(k)+'-'+str(t)

        if key in previous:
            return previous[key]

        if t == len(V):
            result = 0
        elif W[t] > k:
            result = solve(k, t+1)
        else:
            temp1 = V[t] + solve(k-W[t], t+1)
            temp2 = solve(k, t+1)
            result = max(temp1, temp2)

        previous[key] = result
        nonlocal max_val
        max_val = result if result > max_val else max_val

        return result

    solve(K, 0)
    return max_val


def knapsack_bottom_up(V, W, K):
    max_val = 0
    previous = {}

    def solve(k, t):
        key = str(k)+'-'+str(t)

        if key in previous:
            return previous[key]

        if t < 0:
            result = 0
        elif W[t] > k:
            result = solve(k, t-1)
        else:
            temp1 = V[t] + solve(k-W[t], t-1)
            temp2 = solve(k, t-1)
            result = max(temp1, temp2)

        previous[key] = result
        nonlocal max_val
        max_val = result if result > max_val else max_val

        return result

    solve(K, len(V)-1)
    return max_val


t = TicToc()

t.tic()
for i in range(10):
    weight = [random.randrange(1, 30) for x in range(800)]
    val = [random.randrange(1, 20) for x in range(800)]
    knapsack_bu(val, weight, 700)
t.toc()
print(t.elapsed)


t.tic()
for i in range(10):
    weight = [random.randrange(1, 30) for x in range(800)]
    val = [random.randrange(1, 20) for x in range(800)]
    knapsack(val, weight, 700)
t.toc()
print(t.elapsed)
