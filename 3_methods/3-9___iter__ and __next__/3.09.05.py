class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job

    def __setattr__(self, key, value):
        data_type = {'fio': isinstance(value, str),
                     'job': isinstance(value, str),
                     'old': isinstance(value, int),
                     'salary': isinstance(value, int) or isinstance(value, float),
                     'year_job': isinstance(value, int)}

        if data_type[key]:
            self.__dict__[key] = value
        else:
            raise TypeError('Неверный тип присваиваемых данных.')

    def __validate_index(self, key):
        return key < len(list(self.__dict__))

    def __getitem__(self, key):
        if self.__validate_index(key):
            return getattr(self, (list(self.__dict__)[key]))
        else:
            raise IndexError('неверный индекс')

    def __setitem__(self, key, value):
        if self.__validate_index(key):
            setattr(self, (list(self.__dict__)[key]), value)
        else:
            raise IndexError('неверный индекс')

    def __iter__(self):
        for i in range(len(self.__dict__)):
            yield getattr(self, (list(self.__dict__)[i]))


p1 = Person('Andrey', 'it', 35, 2000, 10)
[print(i) for i in p1]
