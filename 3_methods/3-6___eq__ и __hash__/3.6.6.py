import sys


def string_to_list_txt(string):
    name = string.split(': ')[0]
    weight_price = string.split(': ')[1]
    weight = float(weight_price.split()[0])
    price = float(weight_price.split()[1])
    return [name, weight, price]


class ShopItem:
    def __init__(self, name, weight, price):
        if type(name) == str:
            self.name = name
        if type(weight) in (int, float):
            self.weight = weight
        if type(price) in (int, float):
            self.price = price

    def __str__(self):
        return f'{self.name}: {self.weight}, {self.price}'

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return self.name == other.name and self.weight == other.weight and self.price == other.price


lst_in = list(map(str.strip, sys.stdin.readlines()))

shop_items = dict()

for item in lst_in:
    temp_item = ShopItem(*string_to_list_txt(item))
    if temp_item not in shop_items:
        shop_items[temp_item] = [temp_item, 1]
    else:
        shop_items[temp_item][1] += 1


it1 = ShopItem('name', 10, 11)
it2 = ShopItem('name', 10, 11)
assert hash(it1) == hash(it2), "разные хеши у равных объектов"

it2 = ShopItem('name', 10, 12)
assert hash(it1) != hash(it2), "равные хеши у разных объектов"

it2 = ShopItem('name', 11, 11)
assert hash(it1) != hash(it2), "равные хеши у разных объектов"

it2 = ShopItem('NAME', 10, 11)
assert hash(it1) == hash(it2), "разные хеши у равных объектов"

name = lst_in[0].split(':')
for sp in shop_items.values():
    assert isinstance(sp[0], ShopItem) and type(sp[1]) == int, "в значениях словаря shop_items первый элемент должен быть объектом класса ShopItem, а второй - целым числом"

v = list(shop_items.values())
print(v[0][0].name.strip())
if v[0][0].name.strip() == "Системный блок":
    assert v[0][1] == 1 and v[1][1] == 2 and v[2][1] == 1 and len(v) == 3, "неверные значения в словаре shop_items"

if v[0][0].name.strip() == "X-box":
    assert v[0][1] == 2 and v[1][1] == 1 and v[2][1] == 2 and len(v) == 3, "неверные значения в словаре shop_items"