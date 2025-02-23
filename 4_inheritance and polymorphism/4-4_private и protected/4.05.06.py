class Furniture:
    def __init__(self, name, weight):
        if self.__verify_name(name):
            self._name = name
        if self.__verify_weight(weight):
            self._weight = weight

    def __verify_name(self, name):
        if type(name) != str:
            raise TypeError('название должно быть строкой')
        return True

    def __verify_weight(self, weight):
        if type(weight) not in (int, float) and weight > 0:
            raise TypeError('вес должен быть положительным числом')
        return True

    def get_attrs(self):
        return tuple(self.__dict__.values())

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if self.__verify_name(name):
            self._name = name

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        if self.__verify_weight(weight):
            self._weight = weight


class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors


class Chair(Furniture):
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height


class Table(Furniture):
    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square


# -----test-task-----
cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(tb.get_attrs())
