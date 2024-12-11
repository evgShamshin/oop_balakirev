class FloatValue:
    @staticmethod
    def check_float_value(value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.check_float_value(value)
        setattr(instance, self.name, value)


class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:
    def __init__(self, N, M):
        self.cells = [[Cell() for _ in range(M)] for _ in range(N)]


table = TableSheet(5, 3)
s = 1.0

for i in range(5):
    for j in range(3):
        table.cells[i][j].value = s
        s += 1

for i in range(5):
    print()
    for j in range(3):
        print(table.cells[i][j].value, end=" ")
