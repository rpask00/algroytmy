def chain_of_pairs(pairs):
    maxlen = len(pairs)-1

    def solve(chain=[], n=0):
        print(chain)
        if n > maxlen:
            return 0

        if not chain or chain[-1][1] < pairs[n][0]:
            return max([1+solve(chain+[pairs[n]], n+1), solve(chain, n+1)])

        return solve(chain, n+1)

    return solve()

