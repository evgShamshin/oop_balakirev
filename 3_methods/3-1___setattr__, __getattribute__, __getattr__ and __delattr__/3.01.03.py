class Book:
    def __init__(self, title="", author="", pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        # Проверка свойств класса - title и author
        if key in ['title', 'author'] and type(value) != str:
            raise TypeError("Неверный тип присваиваемых данных.")

        # Проверка свойств класса - pages and year
        if key in ['pages', 'year'] and type(value) != int:
            raise TypeError("Неверный тип присваиваемых данных.")

        self.__dict__[key] = value


book = Book("Python ООП", "Сергей Балакирев", 123, 2022)
print(book.__dict__)
