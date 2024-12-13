class Telecast_Descriptor:
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Telecast:
    uid = Telecast_Descriptor()
    name = Telecast_Descriptor()
    duration = Telecast_Descriptor()

    def __init__(self, uid, name, duration):
        self.uid = uid
        self.name = name
        self.duration = duration


class TVProgram:
    def __init__(self, tl):
        self.tl = tl
        self.items = []

    def add_telecast(self, tl):
        self.items.append(tl)

    def remove_telecast(self, indx):
        [self.items.remove(i) for i in self.items if i.uid == indx]


assert hasattr(TVProgram, 'add_telecast') and hasattr(TVProgram,
                                                      'remove_telecast'), "в классе TVProgram должны быть методы add_telecast и remove_telecast"

pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(3, "Новости", 2000))
t = Telecast(2, "Интервью с Балакиревым", 20)

pr.remove_telecast(3)
assert len(pr.items) == 2, "неверное число телеперач, возможно, некорректно работает метод remove_telecast"
assert pr.items[
           -1] == t, "удалена неверная телепередача (возможно, вы удаляете не по __id, а по порядковому индексу в списке items)"

assert type(Telecast.uid) == property and type(Telecast.name) == property and type(
    Telecast.duration) == property, "в классе Telecast должны быть объекты-свойства uid, name и duration"

for x in pr.items:
    assert hasattr(x, 'uid') and hasattr(x, 'name') and hasattr(x, 'duration')

assert pr.items[0].name == "Доброе утро", "объект-свойство name вернуло неверное значение"
assert pr.items[0].duration == 10000, "объект-свойство duration вернуло неверное значение"

t = Telecast(1, "Доброе утро", 10000)
t.uid = 2
t.name = "hello"
t.duration = 10
