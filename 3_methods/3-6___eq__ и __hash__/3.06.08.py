import sys


class BookStudy:
    def __init__(self, name, author, year):
        if type(name) == str:
            self.__name = name
        if type(author) == str:
            self.__author = author
        if str(year).isdigit():
            self.__year = year

    def __eq__(self, other):
        return self.__name == other.__name and self.__author == other.__author

    def __hash__(self):
        return hash((self.__name, self.__author))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value


lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_bs = [BookStudy(*lst.split("; ")) for lst in lst_in]
unique_books = len(set(lst_bs))
print(unique_books)