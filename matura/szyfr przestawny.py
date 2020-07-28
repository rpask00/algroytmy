def szyfr_przestawny(txt):
    arrA = [t for i, t in enumerate(txt) if not i % 2]
    arrB = [t for i, t in enumerate(txt) if i % 2]

    result = ''

    for i, a in enumerate(arrA):
        if i != len(arrB):
            result += arrB[i]

        result += a

    return result


print(szyfr_przestawny('wielomian'))
