import sys as s

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, s.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы
    def insert(self, data):
        lst_temp = {}
        for n_1, d in enumerate(data):
            for n_2, _ in enumerate(data[n_1]):
                lst_temp.update({self.FIELDS[n_2]: d[n_2]})
            self.lst_data.append(lst_temp)
            lst_temp = {}

    def select(self, a, b):
        if b > len(self.lst_data):
            return self.lst_data[a:]
        else:
            return self.lst_data[a:b]

db = DataBase()
db.insert(lst_in)
