def schedule(jobs):
    prevs = {}

    def solve(endtime=0):
        if endtime in prevs:
            return prevs[endtime]

        results = []
        for job in jobs:
            if job[0] >= endtime:
                results.append(job[2]+solve(job[1]))

        res = 0 if not results else max(results)

        prevs[endtime] = res
        return res

    return solve()


j = [
    [3, 10, 20],
    [1, 2, 50],
    [6, 19, 100],
    [2, 100, 200]
]
print(schedule(j))
