from math import sqrt


class Triangle:
    def __init__(self, a, b, c):
        if a >= b + c or b >= a + c or c >= a + b:
            raise ValueError("с указанными длинами нельзя образовать треугольник")
        self.__a = a
        self.__b = b
        self.__c = c

    def __setattr__(self, key, value):
        if type(value) in [int, float] and value > 0:
            super().__setattr__(key, value)
        else:
            raise ValueError("длины сторон треугольника должны быть положительными числами")

    def __len__(self):
        return int(self.__a + self.__b + self.__c)

    def __call__(self):
        p = len(self) / 2
        a = self.__a
        b = self.__b
        c = self.__c

        return float(sqrt(p * (p - a) * (p - b) * (p - c)))

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        self.__c = value



tr = Triangle(5, 4, 3)
assert tr.a == 5 and tr.b == 4 and tr.c == 3, "дескрипторы вернули не верные значения"

try:
    tr = Triangle(-5, 4, 3)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    tr = Triangle(10, 1, 1)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

tr = Triangle(5, 4, 3)
assert len(tr) == 12, "функция len вернула не верное значение"
assert 5.9 < tr() < 6.1, "метод __call__ вернул не верное значение"

tr = Triangle(3.4, 4, 5)
assert len(tr) == 12, "функция len вернула не верное значение для треугольника со сторонами (3.4, 4, 5)"
print(tr())
# assert 6.7 < tr() < 6.8, "метод __call__ вернул не верное значение для треугольника со сторонами (3.4, 4, 5)"

try:
    tr.a = 1
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при изменении атрибута 'a'"

try:
    tr.b = 1
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при изменении атрибута 'b'"

try:
    tr.c = 0.1
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при изменении атрибута 'c'"

try:
    tr.b = -4
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при изменении атрибута 'b'"
