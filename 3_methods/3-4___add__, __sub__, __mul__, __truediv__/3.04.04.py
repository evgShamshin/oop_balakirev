class NewList:
    def __init__(self, value=[]):
        self.value = value

    @staticmethod
    def list_sub_list(a, b):
        b = [(x, type(x)) for x in b]
        return [x for x in a if (x, type(x)) not in b or b.remove((x, type(x)))]

    def __sub__(self, other):
        slf_val = self if isinstance(self, list) else self.value
        oth_val = other if isinstance(other, list) else other.value

        res = [[slf, type(slf)] for slf in slf_val]
        for slf in slf_val:
            for oth in oth_val:
                if (oth, type(oth)) == (slf, type(slf)):
                    res.remove([slf, type(slf)])

        return NewList([r[0] for r in res])

    def __rsub__(self, other):
        slf_val = self if isinstance(self, list) else self.value
        oth_val = other if isinstance(other, list) else other.value

        return NewList(self.list_sub_list(oth_val, slf_val))

    def get_list(self):
        return self.value


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2  # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True]  # NewList: [1, 2, 3]
print(f"res_1 - {res_1.__dict__}")
print(f"lst1 - {lst1.__dict__}")
print(f"res_2 - {res_2.__dict__}")

res_3 = [1, 2, 3, 4.5] - res_2  # NewList: [4.5]
print(f"res_3 - {res_3.__dict__}")
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
print(f"res_4 - {res_4.__dict__}")

# TEST-TASK___________________________________
lst = NewList()
lst1 = NewList([0, 1, -3.4, "abc", True])
lst2 = NewList([1, 0, True])

assert lst1.get_list() == [0, 1, -3.4, "abc", True] and lst.get_list() == [], "метод get_list вернул неверный список"

res1 = lst1 - lst2
res2 = lst1 - [0, True]
res3 = [1, 2, 3, 4.5] - lst2
lst1 -= lst2

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
