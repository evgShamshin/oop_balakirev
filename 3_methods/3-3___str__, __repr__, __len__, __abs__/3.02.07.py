from math import sqrt


class RadiusVector:
    def __init__(self, *args):
        if len(args) == 1:
            self.coords = [0] * args[0]
        else:
            self.coords = [_ for _ in args]

    def set_coords(self, *args):
        for n in range(len(self.coords)):
            if n <= len(args) - 1:
                self.coords[n] = args[n]

    def get_coords(self):
        return tuple(self.coords)

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        return sqrt(sum([coord ** 2 for coord in self.coords]))


# TEST-TASK___________________________________
"""vector3D = RadiusVector(3)
print(vector3D.__dict__)
k = str(*[_ for _ in vector3D.__dict__.keys()])

assert len(vector3D.__dict__[k]) == 3, "ошибка в длине списка из значений"
assert all(True if _ == 0 else False for _ in vector3D.__dict__[k]), "ошибка, значения должны быть нулями"

vector3D.set_coords(3, -5.6, 8)
print(vector3D.__dict__)
a, b, c = vector3D.get_coords()
print(a, b, c)
k = str(*[_ for _ in vector3D.__dict__.keys()])
assert len(vector3D.__dict__[k]) == 3 and \
       (vector3D.__dict__[k] == [3, -5.6, 8] or
        vector3D.__dict__[k] == (3, -5.6, 8)), "значения координат неправильные"

assert hasattr(vector3D, 'set_coords') and callable(vector3D.set_coords), "метод set_coords не найден"
assert hasattr(vector3D, 'get_coords') and callable(vector3D.get_coords), "метод get_coords не найден"

assert vector3D.get_coords() == (3, -5.6, 8), "не правильные значения в кортеже"
assert type(vector3D.get_coords()) == tuple, "метод get_coords должен был вернуть кортеж"

vector3D = RadiusVector(3)
vector3D.set_coords(1, 1.1, -8, 10, 11)  # ошибки быть не должно, последние две координаты игнорируются
assert len(vector3D.__dict__[k]) == 3 and \
       (vector3D.__dict__[k] == [1, 1.1, -8] or
        vector3D.__dict__[k] == (1, 1.1, -8)), "метод set_coords работает не верно"

vector3D.set_coords(1, 2)  # ошибки быть не должно, меняются только первые две координаты
assert vector3D.__dict__[k] == [1, 2, -8] or vector3D.__dict__[k] == (1, 2, -8), \
    "метод set_coords изменил не те значения"

res_len = len(vector3D)  # res_len = 3
assert len(vector3D) == 3, "неправильно работает метод len()"

assert abs(vector3D) == sqrt(sum([i * i for i in vector3D.__dict__[k]])), "метод abs() вернул неверное значение"
print("Правильное решение !")"""

vector3D = RadiusVector(3)
print(vector3D.__dict__)
vector3D.set_coords(3, -5.6, 8)
print(vector3D.__dict__)
a, b, c = vector3D.get_coords()
print(a, b, c)
vector3D.set_coords(4, 3, 999, 10, 11)  # ошибки быть не должно, последние две координаты игнорируются
print(vector3D.__dict__)
vector3D.set_coords(1, 2)  # ошибки быть не должно, меняются только первые две координаты
print(vector3D.__dict__)
res_len = len(vector3D)  # res_len = 3
print(res_len)
res_abs = abs(vector3D)
print(res_abs)

vector3D = RadiusVector(2, 4)
print(vector3D.get_coords())