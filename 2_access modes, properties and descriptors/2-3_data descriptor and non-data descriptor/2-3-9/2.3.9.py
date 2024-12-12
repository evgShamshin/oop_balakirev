class Thing:
    def __init__(self, name, weight):
        if type(name) == str:
            self.name = name
        if type(weight) in (float, int):
            self.weight = weight


class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = []

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        if self.get_total_weight() + thing.weight < self.max_weight:
            self.__things.append(thing)

    def remove_thing(self, indx):
        self.__things.pop(indx)

    def get_total_weight(self):
        return sum([thing.weight for thing in self.__things])


bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.get_total_weight()
print(w)
for t in bag.things:
    print(f"{t.name}: {t.weight}")
