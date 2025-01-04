class ListMath:
    def __init__(self, lst_math=None):
        ch_d = self.__check_dig
        if lst_math is not None:
            self.lst_math = [ch_d(d) for d in lst_math if ch_d(d) is not None]
        else:
            self.lst_math = []

    def __check_dig(self, dig):
        if type(dig) in [float, int]:
            return dig

    def __add__(self, other):
        return ListMath([m + other for m in self.lst_math])

    def __sub__(self, other):
        return ListMath([m - other for m in self.lst_math])

    def __rsub__(self, other):
        return ListMath([other - m for m in self.lst_math])

    def __mul__(self, other):
        return ListMath([m * other for m in self.lst_math])

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return ListMath([m / other for m in self.lst_math])


# TEST-TASK___________________________________
lst1 = ListMath()
lp = [1, False, 2, -5, "abc", 7]
lst2 = ListMath(lp)
lst3 = ListMath(lp)

assert id(lst2.lst_math) != id(lst3.lst_math), "внутри объектов класса ListMath должна создаваться копия списка"

assert lst1.lst_math == [] and lst2.lst_math == [1, 2, -5, 7], "неверные значения в списке объекта класса ListMath"

res1 = lst2 + 76
lst = ListMath([1, 2, 3])
lst += 5
assert lst.lst_math == [6, 7, 8] and res1.lst_math == [77, 78, 71,
                                                       83], "неверные значения, полученные при операциях сложения"

lst = ListMath([0, 1, 2])
res3 = lst - 76
res4 = 7 - lst
assert res3.lst_math == [-76, -75, -74] and res4.lst_math == [7, 6,
                                                              5], "неверные значения, полученные при операциях вычитания"

lst -= 3
assert lst.lst_math == [-3, -2, -1], "неверные значения, полученные при операции вычитания -="

lst = ListMath([1, 2, 3])
res5 = lst * 5
res6 = 3 * lst
lst *= 4
assert res5.lst_math == [5, 10, 15] and res6.lst_math == [3, 6,
                                                          9], "неверные значения, полученные при операциях умножения"
assert lst.lst_math == [4, 8, 12], "неверные значения, полученные при операциях умножения"

lst = lst / 2
lst /= 13.0
