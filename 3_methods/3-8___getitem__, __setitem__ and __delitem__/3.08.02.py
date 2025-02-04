class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getitem__(self, key):
        if key < len(list(self.__dict__.keys())):
            return self.__dict__[list(self.__dict__.keys())[key]]
        else:
            raise IndexError('неверный индекс поля')

    def __setitem__(self, key, value):
        if key < len(list(self.__dict__.keys())):
            self.__dict__[list(self.__dict__.keys())[key]] = value
        else:
            raise IndexError('неверный индекс поля')


r = Record(pk=1, title='Python ООП', author='Балакирев')

assert r.pk == 1 and r.title == 'Python ООП' and r.author == 'Балакирев', "Неправильно занесены значения "
assert r.pk == r[0] and r.title == r[1] and r.author == r[2], "Неправильно работает __getitem__"
r[0] = 2  # доступ к полю pk
r[1] = 'Супер курс по ООП'  # доступ к полю title
r[2] = 'Балакирев С.М.'  # доступ к полю author

assert r[0] == 2 and r[1] == 'Супер курс по ООП' and r[2] == 'Балакирев С.М.', "Неправильно работает __setitem__"

try:
    print(r[3])
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError для неверного int индекса"

try:
    print(r[22.2])
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError для не int индекса"


print("Отлично!")