def wzorzec(txt, w):
    result = []

    for i, t in enumerate(txt):
        if t == w[0]:
            sample = txt[i: i + len(w)]
            if sample == w:
                result.append(i)

    return False if not result else result


print(wzorzec('lokomotywa ', 'motyw'))
