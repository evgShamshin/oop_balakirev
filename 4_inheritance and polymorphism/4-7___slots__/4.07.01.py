class Test:
    __slots__ = ("tst")

    def __init__(self, tst):
        self.tst = tst


t = Test(1)
print(t.tst)