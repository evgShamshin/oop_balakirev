class NewList:
    def __init__(self, value=None):
        self.value = value[:] if value and type(value) == list else []

    @staticmethod
    def list_sub_list(a, b):
        b = [(x, type(x)) for x in b]
        return [x for x in a if (x, type(x)) not in b or b.remove((x, type(x)))]

    def __sub__(self, other):
        slf_val = self.copy() if isinstance(self, list) else self.value.copy()
        oth_val = other.copy() if isinstance(other, list) else other.value.copy()

        res = [[slf, type(slf)] for slf in slf_val]
        for slf in slf_val:
            for oth in oth_val:
                if (oth, type(oth)) == (slf, type(slf)):
                    res.remove([slf, type(slf)])
                    oth_val.remove(oth)

        return NewList([r[0] for r in res])

    def __rsub__(self, other):
        slf_val = self if isinstance(self, list) else self.value
        oth_val = other if isinstance(other, list) else other.value

        return NewList(self.list_sub_list(oth_val, slf_val))

    def get_list(self):
        return self.value


# TEST-TASK___________________________________
lst = NewList()
lst1 = NewList([0, 1, -3.4, "abc", True])
lst2 = NewList([1, 0, True])

assert lst1.get_list() == [0, 1, -3.4, "abc", True] and lst.get_list() == [], "метод get_list вернул неверный список"

res1 = lst1 - lst2
res2 = lst1 - [0, True]
res3 = [1, 2, 3, 4.5] - lst2
lst1 -= lst2
print(res3.get_list())
assert res1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
assert res2.get_list() == [1, -3.4, "abc"], "метод get_list вернул неверный список"
assert res3.get_list() == [2, 3, 4.5], "метод get_list вернул неверный список"
assert lst1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"

lst_1 = NewList([1, 0, True, False, 5.0, True, 1, True, -7.87])
lst_2 = NewList([10, True, False, True, 1, 7.87])
res = lst_1 - lst_2
assert res.get_list() == [0, 5.0, 1, True, -7.87], "метод get_list вернул неверный список"

a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
assert res_4.get_list() == [1, 2], "метод get_list вернул неверный список"
