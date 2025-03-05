class ValidatorString:
    def __init__(self, min_length, max_length, chars):
        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars

    def is_valid(self, string):
        l = len(string)
        if self.max_length >= l >= self.min_length:
            if len(self.chars) > 0:
                if any([s in self.chars for s in string]):
                    return True
            else:
                return True

        raise ValueError('недопустимая строка')


class LoginForm:
    def __init__(self, login_validator, password_validator):
        self.login_validator = login_validator
        self.password_validator = password_validator

    def form(self, request):
        if list(request.keys()) == ['login', 'password']:
            if self.login_validator.is_valid(request['login']) and self.password_validator.is_valid(
                    request['password']):
                setattr(self, '_login', request['login'])
                setattr(self, '_password', request['password'])
        else:
            # print(request.keys())
            raise TypeError('в запросе отсутствует логин или пароль')


login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = 'sergey balakirev!'.split()
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)
