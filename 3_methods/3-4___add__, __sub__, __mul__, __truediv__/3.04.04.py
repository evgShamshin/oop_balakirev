class NewList:
    def __init__(self, value=[]):
        self.value = value

    def __sub__(self, other):
        res = None

        if isinstance(other, NewList) and isinstance(self, NewList):
            res = [[slf, type(slf)] for slf in self.value.copy()]
            for slf in self.value:
                for oth in other.value:
                    if (oth, type(oth)) == (slf, type(slf)):
                        res.remove([slf, type(slf)])

        if not isinstance(other, NewList) and isinstance(self, NewList):
            res = [[slf, type(slf)] for slf in self.value.copy()]
            for slf in self.value:
                for oth in other:
                    if (oth, type(oth)) == (slf, type(slf)):
                        res.remove([slf, type(slf)])

        return [r[0] for r in res]

    def __rsub__(self, other):
        res = None

        if not isinstance(other, NewList) and isinstance(self, NewList):
            res = [[slf, type(slf)] for slf in other.copy()]
            for slf in self.value:
                for oth in other:
                    if (oth, type(oth)) == (slf, type(slf)):
                        res.remove([slf, type(slf)])

        if not isinstance(other, NewList) and not isinstance(self, NewList):
            res = [[slf, type(slf)] for slf in other.copy()]
            for slf in self:
                for oth in other:
                    if (oth, type(oth)) == (slf, type(slf)):
                        res.remove([slf, type(slf)])

        return [r[0] for r in res]


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2  # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True]  # NewList: [1, 2, 3]
print(f"res_1 - {res_1}")
print(f"lst1 - {lst1}")
print(f"res_2 - {res_2}")

res_3 = [1, 2, 3, 4.5] - res_2  # NewList: [4.5]
print(f"res_3 - {res_3}")
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
print(f"res_4 - {res_4}")
