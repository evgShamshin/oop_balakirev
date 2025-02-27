class Digit:
    def __init__(self, value):
        self.validate_value(value)
        self.value = value

    def validate_value(self, value):
        if type(value) not in [int, float]:
            raise TypeError("значение не соответствует типу объекта")


class Integer(Digit):
    def validate_value(self, value):
        if type(value) != int:
            raise TypeError("значение не соответствует типу объекта")


class Float(Digit):
    def validate_value(self, value):
        if type(value) != float:
            raise TypeError("значение не соответствует типу объекта")


class Positive(Digit):
    def validate_value(self, value):
        if type(value) not in [int, float] or value < 0:
            raise TypeError("значение не соответствует типу объекта")


class Negative(Digit):
    def validate_value(self, value):
        if type(value) not in [int, float] or value > 0:
            raise TypeError("значение не соответствует типу объекта")


class PrimeNumber(Integer, Positive):  # 3
    def validate_value(self, value):
        if type(value) != int or value < 0:
            raise TypeError("значение не соответствует типу объекта")


class FloatPositive(Float, Positive):  # 5
    def validate_value(self, value):
        return Positive.validate_value(self, value)


digits = [PrimeNumber(1), PrimeNumber(2), PrimeNumber(3),
          FloatPositive(1.0), FloatPositive(2.0), FloatPositive(3.0),
          FloatPositive(4.0), FloatPositive(5.0)]

lst_positive = list(filter(lambda x: isinstance(x, PrimeNumber), digits))  # filter + isinstance
lst_float = list(filter(lambda x: isinstance(x, FloatPositive), digits))  # filter + isinstance