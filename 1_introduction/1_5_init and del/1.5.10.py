class Cell:
    """ Представление клетки игрового поля """

    def __init__(self, around_mines, mine, fl_open=False):
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

    def show(self):
        """
        Отображение поля в консоли в виде таблицы чисел открытых клеток
        (# - клетка не открыта;
        * - мина;
        между клетками при отображении ставить пробел)
        """
        return [["#" * self.N] for _ in range(self.M)]


pole_game = GamePole(5, 4)
print(pole_game.show())
