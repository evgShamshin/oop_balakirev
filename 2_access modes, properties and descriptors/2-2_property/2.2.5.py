class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")

    @staticmethod
    def __check_value(value):
        return -1 < value < 10001

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if self.__check_value(width):
            self.__width = width
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if self.__check_value(height):
            self.__height = height
            self.show()

# TEST-TASK___________________________________
wnd = WindowDlg('Окно', 10, 11)
assert '_WindowDlg__title' in wnd.__dict__ and '_WindowDlg__width' in wnd.__dict__ and '_WindowDlg__height' in wnd.__dict__, \
    "Атрибуты в экземпляре класса не совпадают, так же они должны быть защищёнными"

assert wnd._WindowDlg__title == 'Окно' and type(wnd._WindowDlg__title) is str, 'Название должно быть строкой'
assert 'width' in dir(wnd) and 'height' in dir(wnd), 'В классе должны быть методы для обращения к приватным атрибутам'

assert wnd.width == 10, 'Геттер для __width работает неправильно'
wnd.width = 11
assert wnd.width == 11, 'Сеттер для __width работает неправильно'

assert wnd.height == 11, 'Геттер для __height работает неправильно'
wnd.height = 22
assert wnd.height == 22, 'Сеттер для __height работает неправильно'

import io
import sys

output = io.StringIO()
sys.stdout = output
wnd.show()
sys.stdout = sys.__stdout__
assert output.getvalue().strip() == "Окно: 11, 22", 'Неправильный формат вывода в методе show'