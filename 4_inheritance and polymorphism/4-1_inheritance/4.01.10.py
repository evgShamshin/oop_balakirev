class Vector:
    def __init__(self, *args):
        self.coords = args

    @staticmethod
    def valid_data(*data):
        return all(map(lambda x: type(x) in (int, float), data))

    @staticmethod
    def valid_len_data(data, other):
        if len(data) == len(other):
            return True
        else:
            raise TypeError('размерности векторов не совпадают')

    def get_coords(self):
        return self.coords

    def __add__(self, other):
        slf_data = self.get_coords() if isinstance(self, Vector) else self
        oth_data = other.get_coords() if isinstance(other, Vector) else other

        if self.valid_len_data(slf_data, oth_data):
            res = [slf_data[i] + oth_data[i] for i in range(len(slf_data))]
            return Vector(*res)

    def __sub__(self, other):
        slf_data = self.get_coords() if isinstance(self, Vector) else self
        oth_data = other.get_coords() if isinstance(other, Vector) else other

        if self.valid_len_data(slf_data, oth_data):
            res = [slf_data[i] - oth_data[i] for i in range(len(slf_data))]
            return Vector(*res)


class VectorInt(Vector):
    @staticmethod
    def valid_data(*data):
        return all(map(lambda x: type(x) == int, data))

    def __init__(self, *args):
        if self.valid_data(*args):
            super().__init__(*args)
        else:
            raise ValueError('координаты должны быть целыми числами')

    def __add__(self, other):
        slf_data = self.get_coords() if isinstance(self, Vector) or isinstance(self, VectorInt) else self
        oth_data = other.get_coords() if isinstance(other, Vector) or isinstance(other, VectorInt) else other

        if self.valid_len_data(slf_data, oth_data):
            res = [slf_data[i] + oth_data[i] for i in range(len(slf_data))]
            if self.valid_data(*slf_data) and self.valid_data(*oth_data):
                return VectorInt(*res)
            else:
                return Vector(*res)

    def __sub__(self, other):
        slf_data = self.get_coords() if isinstance(self, Vector) or isinstance(self, VectorInt) else self
        oth_data = other.get_coords() if isinstance(other, Vector) or isinstance(other, VectorInt) else other

        if self.valid_len_data(slf_data, oth_data):
            res = [slf_data[i] - oth_data[i] for i in range(len(slf_data))]
            if self.valid_data(*slf_data) and self.valid_data(*oth_data):
                return VectorInt(*res)
            else:
                return Vector(*res)


# -----TEST-TASK-----
v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)

assert (v1 + v2).get_coords() == (
    4, 6, 8), "операция сложения дала неверные значения (или некорректно работает метод get_coords)"
assert (v1 - v2).get_coords() == (
    -2, -2, -2), "операция вычитания дала неверные значения (или некорректно работает метод get_coords)"

v = VectorInt(1, 2, 3, 4)
assert isinstance(v, Vector), "класс VectorInt должен наследоваться от класса Vector"

try:
    v = VectorInt(1, 2, 3.4, 4)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError для команды v = VectorInt(1, 2, 3.4, 4)"

v1 = VectorInt(1, 2, 3, 4)
v2 = VectorInt(4, 2, 3, 4)
v3 = Vector(1.0, 2, 3, 4)

v = v1 + v2
print(v)
assert type(
    v) == VectorInt, "при сложении вектором с целочисленными координатами должен формироваться объект класса VectorInt"
v = v1 + v3
assert type(v) == Vector, "при сложении вектором с вещественными координатами должен формироваться объект класса Vector"
