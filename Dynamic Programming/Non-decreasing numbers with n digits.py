# non-decreasing number with n digits 
def countNonDecreasing(n): 
	
	# dp[i][j] contains total count 
	# of non decreasing numbers ending 
	# with digit i and of length j 
	dp = [[0 for i in range(n + 1)] 
			for i in range(10)] 
			
	# Fill table for non decreasing 
	# numbers of length 1. 
	# Base cases 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 

	for i in range(10): 
		dp[i][1] = 1

	# Fill the table in bottom-up manner 
	for digit in range(10): 
		
		# Compute total numbers of non 
		# decreasing numbers of length 'len' 
		for len in range(2, n + 1): 
			
			# sum of all numbers of length 
			# of len-1 in which last 
			# digit x is <= 'digit' 
			for x in range(digit + 1): 
				dp[digit][len] += dp[x][len - 1] 
	count = 0
	
	# There total nondecreasing numbers 
	# of length n won't be dp[0][n] + 
	# dp[1][n] ..+ dp[9][n] 
	for i in range(10): 
		count += dp[i][n] 
	return count 
	
# Driver Code 
n = 3
print(countNonDecreasing(n)) 

# This code is contributed 
# by sahilshelangia 
