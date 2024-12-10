class FloatValue:
    @staticmethod
    def __check_float_value(value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.__check_float_value(value)
        setattr(instance, self.name, value)


class Cell:
    value = FloatValue()

    def __init__(self, value):
        self.value = value


class TableSheet:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.cells = [[Cell(float(0.0)) for i in range(M)] for j in range(N)]


        s = 0
        self.cells = []
        for i in range(N):
            self.cells.append([])
            for j in range(M):
                s += 1
                self.cells[i].append(Cell(float(s)))



table = TableSheet(5, 3)
print(table.cells)

for row in table.cells:
    print()
    for cell in row:
        print(cell.value, end=" ")
