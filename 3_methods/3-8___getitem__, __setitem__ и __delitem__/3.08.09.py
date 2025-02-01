class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.things = []

    def get_total_weight(self):
        return sum([i.weight for i in self.things])

    def add_thing(self, thing):
        if self.get_total_weight() + thing.weight < self.max_weight:
            self.things.append(thing)
        else:
            raise ValueError('превышен суммарный вес предметов')

    def __getitem__(self, index):
        if index < len(self.things):
            return self.things[index]
        else:
            raise IndexError('неверный индекс')

    def __setitem__(self, index, thing):
        slf_t = self.things[index].weight
        if index < len(self.things) and self.get_total_weight() + thing.weight - self.things[index].weight <= self.max_weight:
            self.things[index] = thing
        elif index >= len(self.things):
            raise IndexError('неверный индекс')
        elif self.get_total_weight() + thing.weight - self.things[index].weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')

    def __delitem__(self, index):
        del self.things[index]


class Thing:
    def __init__(self, name, weight):
        if type(name) is str:
            self.name = name
        if type(weight) in (int, float):
            self.weight = weight


b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

try:
    b.add_thing(Thing('рубашка', 500))
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

assert b[0].name == 'книга' and b[
    0].weight == 100, "атрибуты name и weight объекта класса Thing принимают неверные значения"

t = Thing('Python', 20)
b[1] = t
assert b[1].name == 'Python' and b[
    1].weight == 20, "неверные значения атрибутов name и weight, возможно, некорректно работает оператор присваивания с объектами класса Thing"

del b[0]
assert b[0].name == 'Python' and b[0].weight == 20, "некорректно отработал оператор del"

try:
    t = b[2]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))
print(b.get_total_weight())
b[0] = Thing('рубашка', 500)

try:
    b[0] = Thing('рубашка', 800)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"

print('kaif')