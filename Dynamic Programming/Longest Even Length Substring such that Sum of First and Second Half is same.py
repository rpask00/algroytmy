def substr(S):
    def sumstr(s):
        mid = len(s)//2
        suma = sum([int(a) for a in s[:mid]])
        sumb = sum([int(b) for b in s[mid:]])

        return suma == sumb

    prevs = {}

    def solve(a, b):

        key = f'{a}-{b}'
        if key in prevs:
            return prevs[key]

        if a >= b:
            result = 0

        elif (b-a) % 2 and sumstr(S[a:b+1]):
            result = len(S[a:b+1])
        else:
            result = max([solve(a+1, b), solve(a, b-1)])

        prevs[key] = result
        return result

    return solve(0, len(S)-1)


print(substr('87878634897590238563047356546543543789684356435674568743569875436745368453674596746934769857604237562345'))
