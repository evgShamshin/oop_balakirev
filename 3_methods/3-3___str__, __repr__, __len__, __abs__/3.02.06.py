from math import sqrt


class Complex:
    def __init__(self, real, img):
        self.__check_type_value(real)
        self.__real = real
        self.__check_type_value(img)
        self.__img = img

    def __check_type_value(self, value):
        if type(value) not in [int, float]:
            raise ValueError("Неверный тип данных.")

    def __abs__(self):
        return sqrt(self.__real ** 2 + self.__img ** 2)

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        self.__check_type_value(value)
        self.__img = value

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        self.__check_type_value(value)
        self.__real = value


cmp = Complex(7, 8)
cmp.real, cmp.img = 3, 4
c_abs = cmp.__abs__()
print(c_abs)
