class CellException(Exception): ...


class CellStringException(CellException):
    def __str__(self):
        return "длина строки выходит за допустимый диапазон"


class CellFloatException(CellException):
    def __str__(self):
        return "значение выходит за допустимый диапазон"


class CellIntegerException(CellException):
    def __str__(self):
        return "значение выходит за допустимый диапазон"


class Cell:
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value
        self._value = None

    def _valid_value(self, value):
        raise ("Метод не переопределен в дочернем классе")

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._valid_value(value)
        self._value = value


class CellString(Cell):
    def __init__(self, min_value, max_value):
        self._min_length = min_value
        self._max_length = max_value
        self._value = None

    def _valid_value(self, value):
        if self._min_length > len(value) or len(value) > self._max_length:
            raise CellStringException


class CellFloat(Cell):
    def _valid_value(self, value):
        if self._min_value > value or value > self._max_value:
            raise CellFloatException


class CellInteger(Cell):
    def _valid_value(self, value):
        if self._min_value > value or value > self._max_value:
            raise CellIntegerException


class TupleData:
    def __init__(self, *args):
        self.data = args

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        slf_data = [slf_val.value for slf_val in self.data]
        return iter(slf_data)

    def __getitem__(self, item):
        if item < self.__len__():
            return self.data[item]
        else:
            raise IndexError

    def __setitem__(self, key, value):
        if key < self.__len__():
            self.data[key].value = value
        else:
            raise IndexError


t = TupleData(CellInteger(-10, 10), CellInteger(0, 2), CellString(5, 10))

d = (1, 0, 'sergey')
t[0] = d[0]
t[1] = d[1]
t[2] = d[2]

for i, x in enumerate(t):
    assert x == d[i], "объект класса TupleData хранит неверную информацию"

assert len(t) == 3, "неверное число элементов в объекте класса TupleData"

cell = CellFloat(-5, 5)
try:
    cell.value = -6.0
except CellFloatException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellFloatException"

cell = CellInteger(-1, 7)
try:
    cell.value = 8
except CellIntegerException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellIntegerException"

cell = CellString(5, 7)
try:
    cell.value = "hello world"
except CellStringException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellStringException"

assert issubclass(CellIntegerException, CellException) and issubclass(CellFloatException, CellException) and issubclass(
    CellStringException,
    CellException), "классы CellIntegerException, CellFloatException, CellStringException должны наследоваться от класса CellException"
