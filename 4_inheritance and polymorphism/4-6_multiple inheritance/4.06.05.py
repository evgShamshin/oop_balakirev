class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        # super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


class ShopGenericView:
    def __str__(self):
        info = [f'{s}: {self.__dict__[s]}' for s in self.__dict__]
        return '\n'.join(info)


class ShopUserView:
    def __str__(self):
        info = [f'{s}: {self.__dict__[s]}' for s in self.__dict__ if s != '_id']
        return '\n'.join(info)


class Book(ShopItem, ShopUserView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


book = Book("Python ООП", "Балакирев", 2022)
print(book)
# на экране увидим строчки:
# _id: 1
# _title: Python ООП
# _author: Балакирев
# _year: 2022
