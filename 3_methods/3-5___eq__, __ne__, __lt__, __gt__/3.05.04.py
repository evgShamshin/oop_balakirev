MIN_DIMENSION = 0
MAX_DIMENSION = 10000


class Dimensions:
    def __init__(self, a, b, c):
        if self.data_verify(a):
            self.__a = a
        if self.data_verify(b):
            self.__b = b
        if self.data_verify(c):
            self.__c = c

    @staticmethod
    def data_verify(data):
        return MIN_DIMENSION <= data <= MAX_DIMENSION

    @staticmethod
    def get_volume(data):
        return data.a * data.b * data.c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.data_verify(value):
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.data_verify(value):
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if self.data_verify(value):
            self.__c = value

    def __ge__(self, other):
        return self.get_volume(self) >= self.get_volume(other)

    def __gt__(self, other):
        return self.get_volume(self) > self.get_volume(other)

    def __le__(self, other):
        return self.get_volume(self) <= self.get_volume(other)

    def __lt__(self, other):
        return self.get_volume(self) < self.get_volume(other)


class ShopItem:
    def __init__(self, name, price, dim):
        setattr(self, 'name', name) if type(name) == str else None
        setattr(self, 'price', price) if type(price) in (int, float) else None
        setattr(self, 'dim', dim) if isinstance(dim, Dimensions) else None


lst_shop = [ShopItem('кеды', 1024, Dimensions(40, 30, 120)),
            ShopItem('зонт', 500.24, Dimensions(10, 20, 50)),
            ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)),
            ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))]

lst_shop_sorted = sorted(lst_shop, key=lambda item: item.dim.get_volume(item.dim))

assert len(lst_shop) == 4, "число элементов в lst_shop не равно 4"

lst_sp = []
lst_sp.append(ShopItem('кеды', 1024, Dimensions(40, 30, 120)))
lst_sp.append(ShopItem('зонт', 500.24, Dimensions(10, 20, 50)))
lst_sp.append(ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)))
lst_sp.append(ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200)))

lst_sp_sorted = ['зонт', 'кеды', 'табуретка', 'холодильник']
s = [x.name for x in lst_shop_sorted]
assert lst_sp_sorted == s, "список lst_shop_sorted сформирован неверно"

d1 = Dimensions(40, 30, 120)
d2 = Dimensions(40, 30, 120)
d3 = Dimensions(30, 20, 100)
assert d1 <= d2, "неверно отработал оператор <="
assert d3 <= d2, "неверно отработал оператор <="
assert d3 < d2, "неверно отработал оператор <"

d2.a = 10
d2.b = 10
d2.c = 10
assert d2 < d1, "неверно отработал оператор < после изменения объема через объекты-свойства a, b, c"