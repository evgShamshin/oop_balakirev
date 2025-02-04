import sys


class DataBase:
    def __init__(self, path):
        self.path = path
        self.dict_db = {}

    def write(self, record):
        if record not in self.dict_db.keys():
            self.dict_db[record] = [record]
        else:
            self.dict_db[record].append(record)

    def read(self, pk):
        temp = [key for key in self.dict_db.keys() if key.pk == pk]
        if pk in [key.pk for key in self.dict_db.keys()]:
            return self.dict_db[temp[0]][0]


class Record:
    N = 0

    def __init__(self, fio, descr, old):
        if type(fio) == str:
            self.fio = fio
        if type(descr) == str:
            self.descr = descr
        if str(old).isdigit():
            self.old = int(old)

        Record.N += 1
        self.pk = Record.N

    def __eq__(self, other):
        slf = self if isinstance(self, Record) else self[0]
        oth = other if isinstance(other, Record) else other[0]
        return slf.fio == oth.fio and slf.old == oth.old

    def __hash__(self):
        return hash((self.fio, self.old))


lst_in = ['Балакирев С.М.; программист; 33',
          'Кузнецов Н.И.; разведчик-нелегал; 35',
          'Суворов А.В.; полководец; 42',
          'Иванов И.И.; фигурант всех подобных списков; 26',
          'Балакирев С.М.; преподаватель; 33'
          ]

db = DataBase(r"C:\Users\USER404\Documents")
lst_out = list(map(lambda x: Record(*x.split("; ")), lst_in))
[db.write(l) for l in lst_out]

# TEST-TASK-----------------------
d = tuple(db.dict_db.values())[0][0]
assert type(d.descr) == str and type(d.fio) == str and type(
    d.old) == int, "значениями словаря должен быть список из объектов класса Rect с набором атрибутов: descr (строка), fio (строка), old (целое число)"

db22345 = DataBase('123')
r1 = Record('fio', 'descr', 10)
r2 = Record('fio', 'descr', 10)
assert r1.pk != r2.pk, "равные значения атрибута pk у разных объектов класса Record"

db22345.write(r2)
r22 = db22345.read(r2.pk)

print(r22)

assert r22.pk == r2.pk and r22.fio == r2.fio and r22.descr == r2.descr and r22.old == r2.old, "при операциях write и read прочитанный объект имеет неверные значения атрибутов"

assert len(db22345.dict_db) == 1, "неверное число объектов в словаре dict_db"

fio = lst_in[0].split(';')[0].strip()
v = list(db.dict_db.values())
if fio == "Балакирев С.М.":
    assert len(v[0]) == 2 and len(v[1]) == 1 and len(v[2]) == 1 and len(
        v[3]) == 1, "неверно сформирован словарь dict_db"

if fio == "Гейтс Б.":
    assert len(v[0]) == 2 and len(v[1]) == 2 and len(v[2]) == 1 and len(
        v[3]) == 1, "неверно сформирован словарь dict_db"