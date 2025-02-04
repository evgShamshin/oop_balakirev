class Cell:
    def __init__(self, value):
        self.value = value


class SparseTable:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.values = {}

    def update_values(self):
        self.rows = max(self.values, key=lambda x: x[0])[0] + 1
        self.cols = max(self.values, key=lambda x: x[1])[1] + 1

    def add_data(self, row, col, data):
        self.values[(row, col)] = data
        self.rows += row
        self.cols += col

    def remove_data(self, row, col):
        if (row, col) in self.values:
            del self.values[(row, col)]
            self.update_values()
        else:
            raise IndexError('ячейка с указанными индексами не существует')

    def __getitem__(self, key):
        if key in self.values:
            return self.values[key]
        else:
            raise ValueError('данные по указанным индексам отсутствуют')

    def __setitem__(self, key, value):
        if key in self.values:
            self.values[key] = value
            self.update_values()
        else:
            self.values[key] = value
            self.update_values()


st = SparseTable()
st.add_data(2, 5, Cell(25))
st.add_data(1, 1, Cell(11))
assert st.rows == 3 and st.cols == 6, "неверные значения атрибутов rows и cols"

try:
    v = st[3, 2]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

st[3, 2] = 100
print(st[3, 2])
assert st[3, 2] == 100, "неверно отработал оператор присваивания нового значения в ячейку таблицы"
print(st.rows)
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols"

st[4, 7] = 132
assert st.rows == 5 and st.cols == 8, "неверные значения атрибутов rows и cols"

st.remove_data(4, 7)
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols, возможно, некорректно отработал метод remove_data"

st.remove_data(1, 1)
try:
    v = st[1, 1]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    st.remove_data(1, 1)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

d = Cell('5')
assert d.value == '5', "неверное значение атрибута value в объекте класса Cell, возможно, некорректно работает инициализатор класса"
