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
                           'weight': (int, float)}

        if key == "weight":
            if type(value) in valid_data_type[key]:
                if value > 0:
                    self.__dict__[key] = value

        if key in valid_data_type.keys():
            if valid_data_type[key] == type(value):
                self.__dict__[key] = value

    def get_info(self):
        return f"{self.name}: {self.old}, {self.color}, {self.weight}"


class Dog(Animal):
    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.breed = breed
        self.size = size

    def __setattr__(self, key, value):
        valid_data_type = {'old': int,
                           'name': str,
                           'breed': str,
                           'size': tuple}

        if key == "size":
            if valid_data_type[key] == type(value):
                if all(type(i) == int for i in value):
                    self.__dict__[key] = value

        if key in valid_data_type.keys():
            if valid_data_type[key] == type(value):
                self.__dict__[key] = value

    def get_info(self):
        return f"{self.name}: {self.old}, {self.breed}, {self.size}"


c1 = cat = Cat('cat', 5, 'green', 2)
# cat: 5, green, 2
print(c1.get_info() == 'cat: 5, green, 2')
print(c1.get_info())