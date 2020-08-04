prevs = {}


def editDistance(nstr, mstr, n, m, operation=0):
    key = f'{n}-{m}'
    if key in prevs:
        return prevs[key]

    nstr = nstr[:n+1]
    mstr = mstr[:m+1]

    if not nstr:
        result = len(mstr)

    elif not mstr:
        result = len(nstr)

    elif nstr[n] == mstr[m]:
        result = editDistance(nstr, mstr, n-1, m-1)

    else:
        replace = editDistance(nstr, mstr, n-1, m-1)
        insert = editDistance(nstr, mstr, n, m-1)
        delete = editDistance(nstr, mstr, n-1, m)
        result = 1+min([replace, insert, delete])

    prevs[key] = result
    return result


nstr = "saturday"
mstr = "sunday"

print(editDistance(nstr, mstr, len(nstr)-1, len(mstr)-1))
