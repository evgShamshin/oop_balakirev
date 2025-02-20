# ZALUPA EBANYIA

"""class Thing:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight


class DictShop(dict):
    def __init__(self, **kwargs):
        for i in kwargs.keys():
            self.__validate_type(i)
        super().__init__(**kwargs)

    @staticmethod
    def __validate_type(data):
        if not isinstance(data, Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')
        else:
            return True"""