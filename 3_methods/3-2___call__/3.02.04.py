from string import ascii_lowercase, digits


class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")

    def is_validate(self):
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False

        return True


# здесь прописывайте классы валидаторов: LengthValidator и CharsValidator
class CharsValidator:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, value):
        return all([i in self.chars for i in value])


class LengthValidator:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, string):
        return self.max_length >= len(string) >= self.min_length


# TEST-TASK___________________________________
try:
    issubclass(LengthValidator, object)
except NameError:
    print("Вы не создали класс - LengthValidator")

try:
    issubclass(CharsValidator, object)
except NameError:
    print("Вы не создали класс - CharsValidator")

# проверка создания объекта LengthValidator
lv = LengthValidator(2, 5)
print(lv('1234567'))
assert callable(lv), "валидатор LengthValidator не вызываться как функция"
assert not lv('123456'), 'ошибка в LengthValidator, проверяемая строка выходит за заданный диапазон длины знаков'

# проверка создания объекта CharsValidator
cv = CharsValidator('abc')
assert callable(cv), "валидатор CharsValidator не вызываться как функция"
assert not cv('1'), "ошибка в CharsValidator, проверяемая строка содержит недопустимые знаки"
print("Отлично, так держать !!")