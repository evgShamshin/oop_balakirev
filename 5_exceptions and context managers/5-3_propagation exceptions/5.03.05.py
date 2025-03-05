class Test:
    def __init__(self, descr):
        if 10 <= len(descr) <= 10000:
            self.descr = descr
        else:
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):
    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        super().__init__(descr)
        if type(ans_digit) in (int, float) and type(max_error_digit) in (int, float) and max_error_digit > 0:
            self.ans_digit = ans_digit
            self.max_error_digit = max_error_digit
        else:
            raise ValueError('недопустимые значения аргументов теста')

    def run(self):
        ans = float(input())
        return self.ans_digit - self.max_error_digit <= ans <= self.ans_digit + self.max_error_digit


descr, ans = map(str.strip, input().split('|'))
try:
    testAnsDigit = TestAnsDigit(descr, float(ans))
    print(testAnsDigit.run())
except Exception as e:
    print(e)

try:
    test = Test('descr')
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при вызове инициализатора класса Test с неверным набором аргументов"

try:
    test = Test('descr ghgfhgjg ghjghjg')
    test.run()
except NotImplementedError:
    assert True
else:
    assert False

assert issubclass(TestAnsDigit, Test)

t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1)
t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1, 0.5)

try:
    t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1, -0.5)
except ValueError:
    assert True
else:
    assert False