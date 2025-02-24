class Phone:
    def __init__(self, model):
        self.__model = model

    def get_info(self):
        return self.__model, self.__memory


class SmartPhone(Phone):
    def __init__(self, model, memory):
        super().__init__(model)
        self.__memory = memory


phone = SmartPhone('iPhone 123', 1024)
print(phone.get_info())
