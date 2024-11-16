class Cell:
    """ Представление клетки игрового поля """

    def __init__(self, around_mines=0, mine=False, fl_open=False):
        """
        :param around_mines: число мин вокруг клетки (начальное значение 0)
        :param mine: наличие/отсутствие мины в текущей клетке (True/False)
        :param fl_open: открыта/закрыта клетка - булево значение (True/False). Изначально все клетки закрыты (False)
        """
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open


class GamePole:
    """ Управление игровым полем, размером N x N клеток """

    def init(self):
        from random import randint as r

        def count_mines_around(matrix, symbol='#'):
            rows = len(matrix)
            cols = len(matrix[0]) if rows > 0 else 0

            # Создаем новую матрицу для изменения
            new_matrix = [[0] * cols for _ in range(rows)]

            # Проходим по каждому элементу исходной матрицы
            for i in range(rows):
                for j in range(cols):
                    # Если элемент не является символом '#', то продолжаем
                    if matrix[i][j] != symbol:
                        count = 0
                        # Считаем количество символов '#' вокруг текущего элемента
                        for di in [-1, 0, 1]:
                            for dj in [-1, 0, 1]:
                                # Пропускаем сам элемент (0, 0)
                                if di == 0 and dj == 0:
                                    continue
                                ni, nj = i + di, j + dj
                                # Проверка границ массива
                                if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] == symbol:
                                    count += 1
                        # Записываем количество '#' в новую матрицу
                        new_matrix[i][j] = count
                    else:
                        # Если элемент - '#', оставляем его как есть
                        new_matrix[i][j] = 0

            return new_matrix

        pole = [["#" for _ in range(self.N)] for _ in range(self.N)]
        while [a for b in pole for a in b].count("*") != self.M:
            pole[r(0, self.N - 1)][r(0, self.N - 1)] = "*"

        self.pole = pole
        self.pole_count = count_mines_around(pole)
        self.pole_obj = count_mines_around(pole)

        for n1, i in enumerate(range(len(self.pole))):
            for n2, j in enumerate(range(len(self.pole))):

                if self.pole[n1][n2] == "*":
                    mine = True
                else:
                    mine = False
                self.pole_obj[n1][n2] = Cell(around_mines=self.pole_count[n1][n2], mine=mine)

        self.pole = self.pole_obj

    def __init__(self, N, M):
        """
        :param N: размер поля
        :param M: общее число мин на поле
        """
        self.N = N
        self.M = M
        self.init()

    def show(self):
        """
        Отображение поля в консоли в виде таблицы чисел открытых клеток
        (# - клетка не открыта;
        * - мина;
        между клетками при отображении ставить пробел)
        """
        [print([j for j in i]) for i in self.pole_obj]


pole_game = GamePole(10, 12)
GamePole.show(pole_game)

def get_around_mines(i, j):
    n = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            ii, jj = k + i, l + j
            if ii < 0 or jj < 0 or ii >= N or jj >= N:
                continue
            if pole_game.pole[ii][jj].mine:
                n += 1
    return n