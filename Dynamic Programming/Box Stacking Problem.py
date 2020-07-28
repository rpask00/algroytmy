import sys

class Box:
    def __init__(self, w, d, h):
        self.d = d
        self.w = w
        self.h = h
        self.rotations = self.__getspace()

    def __getspace(self):
        class Rotation:
            def __init__(self, a, b, h):
                self.base = sorted([a, b])
                self.height = h

        space = {
            Rotation(self.w, self.d,  self.h),
            Rotation(self.w, self.h,  self.d),
            Rotation(self.h, self.d,  self.w)
        }

        return space


def get_key(iter):
    res = ''
    for n in iter:
        res += str(n) + '-'

    return res


prevs = {}
def maxStackHeight(boxes, base=[sys.maxsize, sys.maxsize]):
    key = get_key(base)
    if key in prevs:
        return prevs[key]

    stacks = [0]

    for box in boxes:
        for rot in box.rotations:
            if rot.base[0] < base[0] and rot.base[1] < base[1]:
                stacks.append(rot.height + maxStackHeight(boxes, rot.base))

    result = max(stacks)
    prevs[key] = result
    return result


arr = [Box(4, 6, 7), Box(1, 2, 3), Box(4, 5, 6), Box(10, 12, 32)]

n = len(arr)
print("The maximum possible height of stack is", maxStackHeight(arr))
