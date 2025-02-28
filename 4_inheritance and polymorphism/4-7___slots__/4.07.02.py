class Money:
    __slots__ = '_money',

    def __init__(self, value):
        self._money = value


class MoneyR(Money):
    pass


m = MoneyR(10)
m.s = 100
