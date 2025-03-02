class Triangle:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def __valid__type(value):
        if type(value) in (int, float) and value >= 0:
            return True
        else:
            raise TypeError

    @staticmethod
    def __valid_triangle(a, b, c):
        if a < sum((b, c)) and b < sum((a, c)) and c < sum((a, b)):
            return True
        else:
            raise ValueError

    def __setattr__(self, key, value):
        try:
            self.__valid__type(value)
        except TypeError:
            raise TypeError('стороны треугольника должны быть положительными числами')

        super().__setattr__(key, value)

        if '_a' in self.__dict__ and '_b' in self.__dict__ and '_c' in self.__dict__:
            try:
                self.__valid_triangle(self._a, self._b, self._c)
            except ValueError:
                raise ValueError('из указанных длин сторон нельзя составить треугольник')


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
lst_tr = []

for i_d in input_data:
    try:
        lst_tr.append(Triangle(i_d[0], i_d[1], i_d[2]))
    except (TypeError, ValueError):
        continue

[print(i.__dict__) for i in lst_tr]