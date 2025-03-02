class NoTypeValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def validate_value(self, value):
        raise "Метод не переопределен в дочернем классе"

    def __call__(self, value):
        if self.validate_value(value):
            return value
        else:
            raise ValueError('значение не прошло валидацию')


class FloatValidator(NoTypeValidator):
    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value)

    def validate_value(self, value):
        if type(value) == float and self.max_value >= value >= self.min_value:
            return True
        else:
            return False


class IntegerValidator(NoTypeValidator):
    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value)

    def validate_value(self, value):
        if type(value) == int and self.max_value >= value >= self.min_value:
            return True
        else:
            return False


def is_valid(lst, validators):
    res = []
    for l in lst:
        for validator in validators:
            try:
                res.append(validator(l))
            except ValueError:
                continue
    return res


fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])  # [1, 4.5]
print(lst_out)