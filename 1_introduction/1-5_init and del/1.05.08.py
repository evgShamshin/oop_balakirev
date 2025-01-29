class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        # add(self, gd) - добавление в корзину товара, представленного объектом gd
        self.goods.append(gd)

    def remove(self, indx):
        # remove(self, indx) - удаление из корзины товара по индексу indx
        self.goods.pop(indx)

    def get_list(self):
        # get_list(self) - получение из корзины товаров в виде списка из строк
        return [f'{gd.name}: {gd.price}' for gd in self.goods]


class Table:
    def __init__(self, name="", price=""):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name="", price=""):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name="", price=""):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name="", price=""):
        self.name = name
        self.price = price


# Объявите в программе следующие классы для описания товаров:
table = Table("Стол", 2500)
tv1 = Cup("ТВ1", 25000)
tv2 = Cup("ТВ2", 27000)
notebook1 = Notebook("Ноутбук1", 35000)
notebook2 = Notebook("Ноутбук2", 37000)
cup = Cup("Кружка", 250)

# Создайте в программе объект cart класса Cart.
# Добавьте в него два телевизора (TV), один стол (Table), два ноутбука (Notebook) и одну кружку (Cup).
# Названия и цены придумайте сами.
cart = Cart()
cart.add(tv1), cart.add(tv2), cart.add(table), cart.add(notebook1), cart.add(notebook2), cart.add(cup)
print(cart.get_list())
