class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}

        self.tr.setdefault(eng, [])
        # здесь продолжайте метод add
        if rus not in self.tr[eng]: self.tr[eng].append(rus)

    def remove(self, eng):
        # здесь продолжайте метод remove
        self.tr.pop(eng)

    def translate(self, eng):
        # здесь продолжайте метод translate
        return self.tr[eng]


# здесь создавайте объект класса Translator
tr = Translator()

# здесь вызовите метод add для следующих связок
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")

# здесь методом remove() удалите связку для английского слова car
tr.remove("car")

# здесь с помощью метода translate() переведите слово go
print(*tr.translate("go"))