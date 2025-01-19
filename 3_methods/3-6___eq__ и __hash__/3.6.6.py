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

    def __hash__(self):
        return hash((self.name, self.weight, self.price))

    def __eq__(self, other):
        return self.name == other.name and self.weight == other.weight and self.price == other.price


lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_out = [ShopItem(*string_to_list_txt(l)) for l in lst_in]
shop_item = {1:2}

print(shop_item)