import sys


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
lst_out = [l.split(": ") for l in lst_in]
for n, l in enumerate(lst_out):
    lst_out[n][1] = l[1].split()

print(lst_out)