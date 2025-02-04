class TicTacToe:
    def __init__(self):
        self.pole = [[Cell() for _ in range(3)] for _ in range(3)]

    def clear(self):
        for i in self.pole:
            for j in i:
                j.is_free == True
                j.value = 0

    def __setitem__(self, key, value):
        if (key[0] < 4) and (key[1] < 4):
            slf_obj = self.pole[key[0]][key[1]]
            if slf_obj.is_free:
                slf_obj.value = value
                slf_obj.is_free = False
            else:
                raise ValueError('клетка уже занята')
        else:
            raise IndexError('неверный индекс клетки')

    def __getitem__(self, key):
        if isinstance(key[0], slice) or isinstance(key[1], slice):
            if isinstance(key[1], slice):
                return tuple(s.value for s in self.pole[key[0]])

            if isinstance(key[0], slice):
                return tuple(i[key[1]].value for i in self.pole)

        elif (key[0] < 4) and (key[1] < 4):
            slf_obj = self.pole[key[0]][key[1]]
            return slf_obj.value


class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return self.is_free == True


g = TicTacToe()
g.clear()
assert g[0, 0] == 0 and g[2, 2] == 0, "начальные значения всех клеток должны быть равны 0"
g[1, 1] = 1
g[2, 1] = 2
assert g[1, 1] == 1 and g[
    2, 1] == 2, "неверно отработала операция присваивания новых значений клеткам игрового поля (или, некорректно работает считывание значений)"

try:
    res = g[3, 0]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"

try:
    g[3, 0] = 5
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"

g.clear()
g[0, 0] = 1
g[1, 0] = 2
g[2, 0] = 3

assert g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (
1, 2, 3), "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"

cell = Cell()
assert cell.value == 0, "начальное значение атрибута value класса Cell должно быть равно 0"
res = cell.is_free
cell.is_free = True
assert bool(cell), "функция bool вернула False для свободной клетки"
