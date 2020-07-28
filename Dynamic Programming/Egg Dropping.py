import sys

# Function to get minimum number of trials
# needed in worst case with eggs eggs and floor floors

prevs = {}


def eggDrop(eggs, floors):
    key = f'{eggs}-{floors}'
    if key in prevs:
        return prevs[key]

    if eggs == 1:
        result = floors

    elif floors in [0, 1]:
        result = floors
    else:
        ress = []
        for floor in range(1, floors+1):
            did_break = eggDrop(eggs-1, floor-1)
            no_break = eggDrop(eggs, floors-floor)
            ress.append(max(did_break,  no_break))

        result = min(ress) + 1

        print(key, result)

    prevs[key] = result
    return result


print(eggDrop(2, 3))
