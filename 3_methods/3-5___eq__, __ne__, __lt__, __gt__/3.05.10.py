class Box:
    def __init__(self):
        self.things = []

    def add_thing(self, thing):
        self.things.append(thing)

    def get_things(self):
        return self.things

    def __eq__(self, other):
        slf_data = sorted(self) if not isinstance(self, Box) \
            else sorted(((s.name.lower(), s.mass) for s in self.get_things()), key=lambda x: x[0])
        oth_data = sorted(other) if not isinstance(other, Box) \
            else sorted(((s.name.lower(), s.mass) for s in other.get_things()), key=lambda x: x[0])
        return slf_data == oth_data


class Thing:
    def __init__(self, name, mass):
        setattr(self, 'name', name) if type(name) is str else None
        setattr(self, 'mass', mass) if type(mass) in (int, float) else None

    def __eq__(self, other):
        slf_data = tuple(self) if not isinstance(self, Thing) else (self.name.lower(), self.mass)
        oth_data = tuple(other) if not isinstance(other, Thing) else (other.name.lower(), other.mass)
        return slf_data == oth_data


b1 = Box()
assert b1.get_things() == [], "Список предметов при создании должен быть пустой"

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

assert len(b1.get_things()) == 3, "Функция добавление предметов в ящик реализована неверно"

b2 = Box()
th1 = Thing('тряпка', 200)
th2 = Thing('тряпка', 200)
print(th1 == th2)
assert th1 == th2, "Сравнение предметов реализовано некорректно"
th3_a = Thing('швабра', 300)
th3_b = Thing('швабра_1', 300)
th3_c = Thing('швабра', 200)
assert th3_a != th3_b or th3_b != th3_c, "Сравнение предметов реализовано некорректно"

b2.add_thing(th1)
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

assert b1 == b2, "Сравнение ящиков реализовано некорректно"
b2.add_thing(Thing('доска', 2000))
assert len(b2.get_things()) == 4, "Функция добавление предметов в ящик реализована неверно"
assert b1 != b2, "Сравнение ящиков реализовано некорректно, для каждого объекта класса Thing одного ящика можно найти ровно один равный объект из второго ящика"

c1 = Box()
c1.add_thing(Thing('мел', 100))
c1.add_thing(Thing('Тряпка', 200))
c1.add_thing(Thing('Тряпка', 200))
c1.add_thing(Thing('доска', 2000))
c2 = Box()
c2.add_thing(Thing('тряпка', 200))
c2.add_thing(Thing('Мел', 100))
c2.add_thing(Thing('доска', 2000))
c2.add_thing(Thing('доска', 2000))
assert c1 != c2, "Сравнение ящиков реализовано некорректно, для каждого объекта класса Thing одного ящика можно найти ровно один равный объект из второго ящика"

c3 = Box()
c3.add_thing(Thing('мел', 100))
c3.add_thing(Thing('Тряпка', 200))
c3.add_thing(Thing('доска', 2000))
c4 = Box()
c4.add_thing(Thing('тряпка', 200))
c4.add_thing(Thing('Мел', 100))
c4.add_thing(Thing('доска', 2000))
c4.add_thing(Thing('Указка', 200))
assert c3 != c4, "Сравнение ящиков реализовано некорректно, для каждого объекта класса Thing одного ящика можно найти ровно один равный объект из второго ящика"
