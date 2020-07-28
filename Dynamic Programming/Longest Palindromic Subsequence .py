def lps(seq,  a, b):
    if a > b:
        return 0

    if a == b:
        return 1

    if seq[a] == seq[b]:
        return lps(seq, a+1, b-1) + 2

    return max(lps(seq, a, b-1), lps(seq, a+1, b))


s = "BBABCBCAB"
print(lps(s, 0, len(s)-1))
