class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y
        else:
            self.__x = 0
            self.__y = 0

    def check_value(self, value):
        return (type(value) == int or type(value) == float) and self.MAX_COORD >= value >= self.MIN_COORD

    @staticmethod
    def norm2(vector):
        x = vector.x
        y = vector.y
        return x ** 2 + y ** 2

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if self.check_value(value):
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if self.check_value(value):
            self.__y = value


v1 = RadiusVector2D()        # радиус-вектор с координатами (0; 0)
v2 = RadiusVector2D(1)       # радиус-вектор с координатами (1; 0)
v3 = RadiusVector2D(1, 2)    # радиус-вектор с координатами (1; 2)

print(v1.x, v1.y)
print(v2.x, v2.y)
print(v3.x, v3.y)
print(v3.norm2(v3))
v2.x = 19999
print(v2.x, v2.y)




r1 = RadiusVector2D()
r2 = RadiusVector2D(1)
r3 = RadiusVector2D(4, 5)

assert hasattr(RadiusVector2D, 'MIN_COORD') and hasattr(RadiusVector2D, 'MAX_COORD'), "в классе RadiusVector2D должны присутствовать атрибуты MIN_COORD и MAX_COORD"

assert type(RadiusVector2D.x) == property and type(RadiusVector2D.y) == property, "в классе RadiusVector2D должны присутствовать объекты-свойства x и y"

assert r1.x == 0 and r1.y == 0 and r2.x == 1 and r2.y == 0 and r3.x == 4 and r3.y == 5, "свойства x и y возвращают неверные значения"

assert RadiusVector2D.norm2(r3) == 41, "неверно вычисляется норма вектора"

r4 = RadiusVector2D(4.5, 5.5)
assert 4.4 < r4.x < 4.6 and 5.4 < r4.y < 5.6, "свойства x и y возвращают неверные значения"

r5 = RadiusVector2D(-102, 2000)
print(r5.__dict__)
assert r5.x == 0 and r5.y == 0, "присвоение значений, выходящих за диапазон [-100; 1024] не должно выполняться"

r = RadiusVector2D(10, 20)
r.x = 'a'
r.y = (1, 2)
assert r.x == 10 and r.y == 20, "присвоение не числовых значений должно игнорироваться"