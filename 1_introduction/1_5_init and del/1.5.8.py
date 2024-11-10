class Cart:
    def __init__(self):
        # goods - список объектов для покупки (объекты классов Table, TV, Notebook и Cup). Изначально этот список должен быть пустым
        self.goods = []

    def add(self, gd, price=0):
        # add(self, gd) - добавление в корзину товара, представленного объектом gd
        self.goods.append(gd)
        self.price = price

    def remove(self, indx):
        # remove(self, indx) - удаление из корзины товара по индексу indx
        self.goods.pop(indx)

    def get_list(self):
        # get_list(self) - получение из корзины товаров в виде списка из строк
        print(self.goods)

Table = Cart()
Table.add("Столы")

TV = Cart()
TV.add("TV")

Notebook = Cart()
Notebook.add("Ноутбуки")

Cup = Cart()
Cup.add("Кружки")

Table.get_list()
TV.get_list()
Cup.get_list()

