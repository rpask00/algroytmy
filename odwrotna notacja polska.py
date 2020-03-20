
ops = {
    '+': lambda a, b: a+b,
    '*': lambda a, b: a*b,
    '-': lambda a, b: a-b,
    '/': lambda a, b: a/b,
}


def rpn(expression):
    tokens = expression.split()
    stos = []

    for token in tokens:
        if token in ops:
            a = stos.pop()
            b = stos.pop()

            result = ops[token](a, b)
            stos.append(result)
        else:
            stos.append(int(token))

    return stos.pop()


# print(eval("1 2 + "))
# print(eval("990 1 2 + *"))
print(rpn("1000 990 1 2 + * +"))
# print(rpn("3 2 - 5 * 4 2 * + 1 - 8 2 - + 5 *"))


# (3 - 2) * 5 + 4 * 2 - 1 + (8 - 2) * 5
# 3 2 - 5 * 4 + 2 * 1 - 8 2 - + 5 *
