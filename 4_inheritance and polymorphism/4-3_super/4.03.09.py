import string


class StringDigit(str):
    def __init__(self, data):
        self.__validate_data(data)

    @staticmethod
    def __validate_data(data):
        for d in data:
            if d not in string.digits:
                raise ValueError("в строке должны быть только цифры")
        return True

    def __add__(self, other):
        return StringDigit(str(self) + other)

    def __radd__(self, other):
        return StringDigit(other + str(self))


# -----TEST-TASK-----
sd = StringDigit("123")
assert str(sd) == "123", "неверно работает метод __str__ класса StringDigit"

try:
    sd2 = StringDigit("123a")
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

sd = sd + "345"

assert sd == "123345", "неверно отработал оператор +"

sd = "0" + sd
assert sd == "0123345", "неверно отработал оператор +"

try:
    sd = sd + "12d"
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при выполнении оператора +"

try:
    sd = "12d" + sd
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при выполнении оператора +"
