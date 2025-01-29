class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.slot = {}

    @staticmethod
    def __validate_type(slot_num, filter):
        __validate = {1: Mechanical,
                      2: Aragon,
                      3: Calcium}
        return __validate[slot_num] == filter.__class__

    def add_filter(self, slot_num, filter):
        if self.__validate_type(slot_num, filter) and slot_num not in self.slot:
            self.slot[slot_num] = filter

    def remove_filter(self, slot_num):
        if slot_num in self.slot:
            del self.slot[slot_num]

    def get_filters(self):
        slot = sorted(self.slot.items())
        return [i[1] for i in slot]

    def water_on(self):
        slot = self.slot
        max = GeyserClassic.MAX_DATE_FILTER
        return all((len(slot) == 3, all(0 <= time.time() - s.date <= max for s in slot.values())))


class Mechanical:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            self.__dict__[key] = value


class Aragon:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            self.__dict__[key] = value


class Calcium:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            self.__dict__[key] = value


import time

my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))

# assert my_water.water_on() == False, "метод water_on вернул True, хотя не все фильтры были установлены"

my_water.add_filter(3, Calcium(time.time()))
# print(my_water.water_on())
# assert my_water.water_on(), "метод water_on вернул False при всех трех установленных фильтрах"
# print(my_water.get_filters())
f1, f2, f3 = my_water.get_filters()

# assert isinstance(f1, Mechanical) and isinstance(f2, Aragon) and isinstance(f3,
#                                                                            Calcium), "фильтры должны быть устанлены в порядке: Mechanical, Aragon, Calcium"

my_water.remove_filter(1)
# assert my_water.water_on() == False, "метод water_on вернул True, хотя один из фильтров был удален"

my_water.add_filter(1, Mechanical(time.time()))
# assert my_water.water_on(), "метод water_on вернул False, хотя все три фильтра установлены"

f1, f2, f3 = my_water.get_filters()
my_water.remove_filter(1)

my_water.add_filter(1, Mechanical(time.time() - GeyserClassic.MAX_DATE_FILTER - 1))
print(my_water.water_on())
print(my_water.slot)
assert my_water.water_on() == False, "метод water_on вернул True, хотя у одного фильтра истек срок его работы"

f1 = Mechanical(1.0)
f2 = Aragon(2.0)
f3 = Calcium(3.0)
assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "неверное значение атрибута date в объектах фильтров"

f1.date = 5.0
f2.date = 5.0
f3.date = 5.0

assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "локальный атрибут date в объектах фильтров должен быть защищен от изменения"
