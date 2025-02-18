class Validator:
    def _is_valid(self, data):
        return True
        # Предусмотреть проверку в дочерних классах
        # else:
        # raise ValueError('данные не прошли валидацию')

    def __call__(self, data):
        return self._is_valid(data)


class IntegerValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        if type(data) == int and self.min_value <= data <= self.max_value:
            return True
        else:
            raise ValueError('данные не прошли валидацию')


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        if type(data) == float and self.min_value <= data <= self.max_value:
            return True
        else:
            raise ValueError('данные не прошли валидацию')


# -----TEST-TASK-----
v = Validator()
res_of_valid = v("123")
print(res_of_valid)
integer_validator = IntegerValidator(-10, 10)
float_validator = FloatValidator(-1, 1)
res1 = integer_validator(10)  # исключение не генерируется (проверка проходит)
res2 = float_validator(10)    # исключение ValueError
print(res1)