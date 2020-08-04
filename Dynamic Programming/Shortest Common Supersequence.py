import sys

prevs={}
def shortestSuperSequence(stra, strb, a, b, res, lastrm=0):
    key = f'{a}-{b}-' if not res else  f'{a}-{b}-{res[-1]}'
    if key in prevs:
        return prevs[key]

    if a == len(stra) and b == len(strb):
        prevs[key] = 0
        return prevs[key]

    resA = sys.maxsize
    resB = sys.maxsize

    if a == len(stra):
        if res and strb[b] == res[-1] and lastrm == 1:
            b += 1

            if b == len(strb):
                prevs[key] = 0
                return prevs[key]

        resB = shortestSuperSequence(stra, strb, a, b+1, res+strb[b], 2)

    elif b == len(strb):
        if res and stra[a] == res[-1] and lastrm == 2:
            a += 1

            if b == len(strb):
                prevs[key] = 0
                return prevs[key]

        resA = shortestSuperSequence(stra, strb, a+1, b, res+stra[a], 1)

    else:
        if res and stra[a] == res[-1] and lastrm == 2:
            a += 1

        if res and strb[b] == res[-1] and lastrm == 1:
            b += 1

        if a < len(stra):
            resA = shortestSuperSequence(stra, strb, a+1, b, res+stra[a], 1)
        if b < len(strb):
            resB = shortestSuperSequence(stra, strb, a, b+1, res+strb[b], 2)

    prevs[key] = 1 + min(resA, resB)
    return prevs[key]


def superSeq(X, Y, m, n): 
	dp = [[0] * (n + 2) for i in range(m + 2)] 

	# Fill table in bottom up manner 
	for i in range(m + 1): 
		for j in range(n + 1): 
			
			#Below steps follow above recurrence 
			if (not i): dp[i][j] = j 
			elif (not j): dp[i][j] = i 
			
			elif (X[i - 1] == Y[j - 1]): 
				dp[i][j] = 1 + dp[i - 1][j - 1] 
				
			else: dp[i][j] = 1 + min(dp[i - 1][j], 
									dp[i][j - 1]) 
			
	return dp[m][n] 

# Driver Code 
X = "GEEK"
Y = "EKE"
print("Length of the shortest supersequence is %d" % superSeq(X, Y, len(X), len(Y))) 
print(shortestSuperSequence(X, Y, 0, 0, ''))
