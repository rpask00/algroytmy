def printAs(N):
    prevs = {}

    def solve(n, output=0, bufor=0, selected=0):
        key = f'{n}-{output}-{bufor}-{selected}'
        if key in prevs:
            return prevs[key]

        if not n:
            return 0

        pressA = 1+solve(n-1, output + 1, 0, 0)
        ctlrA = solve(n-1, output, bufor, output)
        ctlrC = solve(n-1, output, selected, 0)
        ctlrV = bufor+solve(n-1, output+bufor, bufor, 0)

        result = max([pressA, ctlrA, ctlrC, ctlrV])
        prevs[key] = result
        return result

    return solve(N)


# A recursive Python3 program to print maximum 
# number of A's using following four keys 

# A recursive function that returns 
# the optimal length string for N keystrokes 

def findoptimal(N): 
	
	if N<= 6: 
		return N 

	# Initialize result 
	maxi = 0

	for b in range(N-3, 0, -1): 
		curr =(N-b-1)*findoptimal(b) 
		if curr>maxi: 
			maxi = curr 
	
	return maxi 
	

for n in range(1, 44): 
    print('Maximum Number of As with ', n, 'keystrokes is ', findoptimal(n)) 
    # print(printAs(n))
