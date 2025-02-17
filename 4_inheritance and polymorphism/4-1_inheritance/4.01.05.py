class Thing:
    ID = 0

    def __init__(self, name, price):
        Thing.ID += 1
        self.id = Thing.ID
        self.name = name
        self.price = price

    def get_data(self):
        return f'{self.id}, {self.name}, {self.price}, {self.weight}, {self.dims}, {self.memory}, {self.frm}'


class Table(Thing):
    def __init__(self, name, price, weight=None, dims=None):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims
        self.memory = None
        self.frm = None


class ElBook(Thing):
    def __init__(self, name, price, memory=None, frm=None):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm
        self.weight = None
        self.dims = None


table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(table.get_data())
print(book.get_data())
