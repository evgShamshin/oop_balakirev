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

    def __init__(self, N, M):
        """
        :param N: размер поля
        :param M: общее число мин на поле
        """
        self.N = N
        self.M = M
        self.init()

    def init(self):
        from random import randint as r

        pole = [["#" for _ in range(self.N)] for _ in range(self.N)]
        while [a for b in pole for a in b].count("*") != self.M:
            pole[r(0, self.N - 1)][r(0, self.N - 1)] = "*"

        self.pole = pole

        for n1, i in enumerate(range(len(self.pole))):
            for n2, j in enumerate(range(len(self.pole))):

                if self.pole[n1][n2] == "*":
                    mine = True
                else:
                    mine = False
                self.pole[n1][n2] = Cell(around_mines=self.get_around_mines(i=n1, j=n2), mine=mine)

    def get_around_mines(self, i, j):
        n = 0
        for k in range(-1, 2):
            for l in range(-1, 2):
                print(i, j, k, l)
                ii, jj = k + i, l + j
                print(ii, jj)
                print()
                if ii < 0 or jj < 0 or ii >= self.N or jj >= self.N:
                    continue
                if self.pole[ii][jj] == "*":
                    n += 1
        return n

    def show(self):
        """
        Отображение поля в консоли в виде таблицы чисел открытых клеток
        (# - клетка не открыта;
        * - мина;
        между клетками при отображении ставить пробел)
        """
        res = [([j.__dict__["mine"] for j in i]) for i in self.pole]
        for i in res:
            print()
            for j in i:
                if j:
                    print("*", end=" ")
                else:
                    print("#", end=" ")
        print()
        res_temp = [([j.__dict__["around_mines"] for j in i]) for i in self.pole]
        for i, row in enumerate(range(len(res_temp))):
            print()
            for j in res_temp[i]:
                print(j, end=" ")


N = 5
M = 3

pole_game = GamePole(N, M)
pole_game.show()
