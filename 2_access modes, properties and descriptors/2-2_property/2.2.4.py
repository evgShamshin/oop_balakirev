class Car:
    def __init__(self):
        self.__model = ""

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if self.__check_model(model):
            self.__model = model

    def __check_model(self, model):
        if 1 < len(model) < 101 and type(model) == str:
            self.__model = model


car = Car()
car.model = "Toyota"