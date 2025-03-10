class Food:
    def __init__(self, name, weight, calories):
        self._name = name
        self._weight = weight
        self._calories = calories


class BreadFood(Food):
    def __init__(self, name, weight, calories, white):
        super().__init__(name, weight, calories)
        self._white = white


class SoupFood(Food):
    def __init__(self, name, weight, calories, dietary):
        super().__init__(name, weight, calories)
        self._dietary = dietary


class FishFood(Food):
    def __init__(self, name, weight, calories, fish):
        super().__init__(name, weight, calories)
        self._fish = fish


bf = BreadFood("Бородинский хлеб", 34.5, 512, False)
sf = SoupFood("Черепаший суп", 520, 890.5, False)
ff = FishFood("Консерва рыбная", 340, 1200, "семга")
res = None
