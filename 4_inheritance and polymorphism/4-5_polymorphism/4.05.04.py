class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    ID = 0

    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price
        self.ID = __class__.ID
        __class__.ID = __class__.ID + 1

    def get_id(self):
        return self.ID


item1 = ShopItem("имя1", "вес1", "100")
item2 = ShopItem("имя2", "вес2", "200")
item3 = ShopItem("имя3", "вес3", "300")
print(item1.get_id())
print(item2.get_id())
print(item3.get_id())
