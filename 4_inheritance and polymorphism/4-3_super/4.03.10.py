class ItemAttrs:
    def __setitem__(self, key, value):
        setattr(self, tuple(self.__dict__.keys())[key], value)

    def __getitem__(self, key):
        return self.__getattribute__(tuple(self.__dict__.keys())[key])


class Point(ItemAttrs):
    def __init__(self, x, y):
        self.x = x
        self.y = y


# -----TEST-TASK-----
pt = Point(1, 2.5)
print(pt.__getattribute__(tuple(pt.__dict__.keys())[1]))
x = pt[0]   # 1
y = pt[1]   # 2.5
pt[0] = 10