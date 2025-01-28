class Vector:
    def __init__(self, *args):
        [setattr(self, f'x{n + 1}', arg) for n, arg in enumerate(args) if type(arg) in (int, float)]

    def __len__(self):
        return len(self.__dict__)

    def __add__(self, other):
        if type(other) == Vector and len(self) != len(other):
            raise ArithmeticError('размерности векторов не совпадают')
        elif type(other) == Vector and len(self) == len(other):
            return Vector(*[self.__dict__[f"x{n + 1}"] + other.__dict__[f"x{n + 1}"] for n in range(len(self))])
        elif type(other) == int:
            return Vector(*[self.__dict__[f"x{n + 1}"] + other for n in range(len(self))])

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)

    def __sub__(self, other):
        if type(other) == Vector and len(self) != len(other):
            raise ArithmeticError('размерности векторов не совпадают')
        elif type(other) == Vector and len(self) == len(other):
            return Vector(*[self.__dict__[f"x{n + 1}"] - other.__dict__[f"x{n + 1}"] for n in range(len(self))])
        elif type(other) == int:
            return Vector(*[self.__dict__[f"x{n + 1}"] - other for n in range(len(self))])

    def __mul__(self, other):
        if type(other) == Vector and len(self) != len(other):
            raise ArithmeticError('размерности векторов не совпадают')
        elif type(other) == Vector and len(self) == len(other):
            return Vector(*[self.__dict__[f"x{n + 1}"] * other.__dict__[f"x{n + 1}"] for n in range(len(self))])
        elif type(other) == int:
            return Vector(*[self.__dict__[f"x{n + 1}"] * other for n in range(len(self))])


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print((v1 + v2).__dict__)  # [5, 7, 9]
print((v1 - v2).__dict__)  # [-3, -3, -3]
print((v1 * v2).__dict__)  # [4, 10, 18]

v1 += 10
print(v1.__dict__)  # [11, 12, 13]
v1 -= 10
print(v1.__dict__)  # [1, 2, 3]
v1 += v2
print(v1.__dict__)  # [5, 7, 9]
v2 -= v1
print(v2.__dict__)  # [-1, -2, -3]

print(v1 == v2)  # False
print(v1 != v2)  # True
