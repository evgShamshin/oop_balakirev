class ListInteger(list):
    def __validate(self, a):
        if type(a) != int:
            raise TypeError('можно передавать только целочисленные значения')
        return True

    def __init__(self, args):
        for i in args:
            self.__validate(i)
        super().__init__(args)

    def __setitem__(self, key, value):
        if self.__validate(value):
            super().__setitem__(key, value)

    def append(self, value):
        if self.__validate(value):
            super().append(value)


# TEST-TASK
s = ListInteger((1, 2, 3))
print(s)

# Positive tests
assert s == [1, 2, 3], f'Некорректно сформирован список {s}'

s[1] = 10
assert s == [1, 10, 3], f'Некорректно сформирован список после переприсваиния элемента на 2 позиции {s}'

s.append(11)
assert s == [1, 10, 3, 11], f'Некорректно сформирован список после добавления элемента в конец {s}'

# Negative tests
flag = False

try:
    s[0] = 10.5
except Exception:
    flag = True
finally:
    assert flag, 'Не был перехвачен эксепшен при setitem, вероятно проблема в валидации'
    flag = False

try:
    s.append(10.5)
except Exception:
    flag = True
finally:
    assert flag, 'Не был перехвачен эксепшен при append, вероятно проблема в валидации'
    flag = False

try:
    s = ListInteger((1, 2, 3.1))
    print(s)
except Exception:
    flag = True
finally:
    assert flag, 'При инициализации объекта не был перехвачен эксепшен, вероятно проблема в валидации'
