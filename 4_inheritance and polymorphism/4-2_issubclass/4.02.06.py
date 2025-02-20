class Tuple(tuple):
    def __int__(self, data):
        super().__init__(data)

    def __add__(self, other):
        slf_data = tuple(self)
        oth_data = tuple(other)
        return Tuple(slf_data + oth_data)

# -----TEST-TASK-----
t = Tuple([1, 2, 3])
t = t + "Python"
print(t)   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
t = (t + "Python") + "ООП"