prevs = {}


def LCS(A, B):

    def get_key(x, y):
        return str(x)+'-'+str(y)

    def lcs(indexA, indexB):
        key = get_key(indexA, indexB)
        if key in prevs:
            return prevs[key]

        if indexA == 0 or indexB == 0:
            result = 0
        elif A[indexA-1] == B[indexB-1]:
            result = 1 + lcs(indexA-1, indexB-1)
        else:
            temp1 = lcs(indexA, indexB-1)
            temp2 = lcs(indexA-1, indexB)
            result = max(temp1, temp2)

        prevs[key] = result

        return result

    return lcs(len(A), len(B))


print(LCS('banan','szampan'))