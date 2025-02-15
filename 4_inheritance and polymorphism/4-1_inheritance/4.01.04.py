class Animal:
    def __init__(self, name, old):
        self.name = name
        self.old = old

    def __setattr__(self, key, value):
        valid_data_type = {'old': int,
                           'name': str}
        if key in valid_data_type.keys():
            if valid_data_type[key] == type(value):
                self.__dict__[key] = value


class Cat(Animal):
    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color = color
        self.weight = weight

    def __setattr__(self, key, value):
        valid_data_type = {'old': int,
                           'name': str,
                           'color': str,
                           'weight': int,
                           'old_d': value > 0,
                           'weight_d': value > 0}


        if key in valid_data_type.keys():
            if valid_data_type[key] == type(value):
                self.__dict__[key] = value

class Dog(Animal):



c1 = Cat('123', 5, 'green', 1)
print(c1.__dict__)
