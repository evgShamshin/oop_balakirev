class Lib:
    def __init__(self):
        self.book_list = []

    def __add__(self, other):
        self.book_list.append(other)
        return self

    def __iadd__(self, other):
        self.book_list.append(other)
        return self

    def __sub__(self, other):
        if not isinstance(other, Book):
            self.book_list.pop(other)
        else:
            self.book_list.remove(other)
        return self

    def __isub__(self, other):
        if not isinstance(other, Book):
            self.book_list.pop(other)
        else:
            self.book_list.remove(other)
        return self

    def __len__(self):
        return len(self.book_list)


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


# TEST-TASK-DATA___________________________________
lib = Lib()
b1 = Book('Бойцовский клуб', 'Чак Паланик', '1996')
b2 = Book('Виктор Пелевин', 'Generation "П"', '1999')
lib_id = id(lib)
# TEST-TASK-ADD___________________________________
lib += b1
lib += b2
assert (len(lib.__dict__['book_list'])) == 2 and [isinstance(l, Book) for l in lib.__dict__], "ошибка в add"
assert (lib_id == id(lib)), "ошибка в id add"
# TEST-TASK-SUB-BOOK___________________________________
lib -= b1
assert b2 not in lib.__dict__, "ошибка в sub-book"
assert (lib_id == id(lib)), "ошибка в id sub-book"
# TEST-TASK-SUB-INDEX___________________________________
lib -= 0
assert lib.book_list == [], "ошибка в sub-index"
assert (lib_id == id(lib)), "ошибка в id sub-index"
# TEST-TASK-LEN___________________________________
assert len(lib) == 0, "ошибка в len"
# ___________________________________
print("Молодец! Решение правильное!")