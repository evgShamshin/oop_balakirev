import sys as s

# программу не менять, только добавить два метода
lst_in = list(map(str.split, s.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы
    def insert(self, data):
        l = []
        print([l.append({self.FIELDS[n]: d[n]}) for n, d in enumerate(data)])


db = DataBase()
db.insert(lst_in)
print(lst_in)