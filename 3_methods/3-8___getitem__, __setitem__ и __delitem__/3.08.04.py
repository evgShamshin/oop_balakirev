class Array:
    def __init__(self, max_length, cell):
        self.max_length = max_length
        self.cell = cell
        self.our_info = [0 for _ in range(max_length)]

    def __str__(self):
        return " ".join(str(n) for n in self.our_info)

    def __setitem__(self, index, value):
        if type(value) == int and len(self.our_info) > index >= 0:
            self.our_info[index] = value
        elif type(value) != int:
            raise ValueError('должно быть целое число')
        else:
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __getitem__(self, index):
        if len(self.our_info) > index >= 0:
            return self.our_info[index]
        else:
            raise IndexError('неверный индекс для доступа к элементам массива')


class Integer:
    def __init__(self, value):
        if type(value) == int:
            self.start_value = value

    @property
    def value(self):
        return self.start_value

    @value.setter
    def value(self, value):
        if type(value) == int:
            self.start_value = value
        else:
            raise ValueError('должно быть целое число')


a = Array(20, cell=Integer)
assert a[18] == 0, "начальные значения в ячейках массива (в объектах класса Integer) должны быть равны 0"

a = Array(2, cell=Integer)
a[0] = 1
a[1] = 2

print(str(a))
assert str(a) == "1 2", "функция str(a) для объекта класса Array вернула неверное значение"
print(a[0])
assert a[0] == 1 and a[1] == 2, "некорректно работает запись и/или считывание значений из массива по индексу"


try:
    a[1] = 2.5
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    a[100] = 25
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"
