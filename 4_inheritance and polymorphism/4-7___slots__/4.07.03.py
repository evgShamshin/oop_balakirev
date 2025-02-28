class Money:
    __slots__ = '_money',

    def __init__(self, value):
        self._money = value


class MoneyR(Money):
    __slots__ = '_value',


m = MoneyR(10)
m._money = 100
m._value = 20
# m.other = 2
