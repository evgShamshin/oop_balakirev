class Cell:
    """ Представление клетки игрового поля """

    def __init__(self, around_mines, mine, fl_open=False):
        """
        :param around_mines: число мин вокруг клетки (начальное значение 0)
        :param mine: наличие/отсутствие мины в текущей клетке (True/False)
        :param fl_open: открыта/закрыта клетка - булево значение (True/False). Изначально все клетки закрыты (False)
        """
        pass

class GamePole:
    """ Управление игровым полем, размером N x N клеток """
    pass
