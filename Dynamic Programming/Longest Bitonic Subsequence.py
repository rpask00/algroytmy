import random


def lbs(arr):
    maxindex = len(arr) - 1

    def solve_incr(big=-89887887, n=0, incresing=True, storage=[]):
        if n > maxindex:
            return 0

        currnet = arr[n]

        if incresing:
            if currnet > big:
                return max([1+solve_incr(currnet, n+1, True, storage+[currnet]), solve_incr(big, n+1, True, storage),  1+solve_incr(currnet, n+1, False, storage+[currnet])])

            return max([solve_incr(big, n+1, True, storage), 1+solve_incr(currnet, n+1, False, storage+[currnet])])
        else:
            if currnet < big:
                return max([1+solve_incr(currnet, n+1, False, storage+[currnet]), solve_incr(big, n+1, False, storage)])

            return solve_incr(big, n+1, False, storage)

    def solve_decr(big=777777, n=0, incresing=False, storage=[]):
            
        if n > maxindex:
            return 0

        currnet = arr[n]

        if incresing:
            if currnet > big:
                return max([1+solve_decr(currnet, n+1, True, storage+[currnet]), solve_decr(big, n+1, True, storage)])

            return solve_decr(big, n+1, True, storage)
        else:
            if currnet < big:
                return max([1 + solve_decr(currnet, n+1, False, storage+[currnet]), solve_decr(big, n+1, False, storage), 1+solve_decr(currnet, n+1, True, storage+[currnet])])

            return max([solve_decr(-big, n+1, False), 1+solve_decr(currnet, n+1, True, storage+[currnet])])

    return max([solve_incr(), solve_decr()])


def _lbs(arr):
    n = len(arr)

    # allocate memory for LIS[] and initialize LIS values as 1
    # for all indexes
    lis = [1 for i in range(n+1)]

    # Compute LIS values from left to right
    for i in range(1, n):
        for j in range(0, i):
            if ((arr[i] > arr[j]) and (lis[i] < lis[j] + 1)):
                lis[i] = lis[j] + 1

    # allocate memory for LDS and initialize LDS values for
    # all indexes
    lds = [1 for i in range(n+1)]

    # Compute LDS values from right to left
    for i in reversed(range(n-1)):  # loop from n-2 downto 0
        for j in reversed(range(i-1, n)):  # loop from n-1 downto i-1
            if(arr[i] > arr[j] and lds[i] < lds[j] + 1):
                lds[i] = lds[j] + 1

    # Return the maximum value of (lis[i] + lds[i] - 1)
    maximum = lis[0] + lds[0] - 1
    for i in range(1, n):
        maximum = max((lis[i] + lds[i]-1), maximum)

    return maximum


print(lbs([0 , 8 , 4, 12, 2, 10 , 6 , 14 , 1 , 9 , 5 , 13, 3, 11 , 7 , 15] ),   _lbs([0 , 8 , 4, 12, 2, 10 , 6 , 14 , 1 , 9 , 5 , 13, 3, 11 , 7 , 15] ))

# for i in range(22):
#     arr = [random.randrange(1, 100) for x in range(10)]
#     print(arr)
#     print(lbs(arr) == _lbs(arr))
