from abc import ABC, abstractmethod


# здесь объявляйте классы
class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return "Базовый класс Model"


class ModelForm(Model):
    ID = 0

    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = __class__.ID
        __class__.ID = __class__.ID + 1

    def get_pk(self):
        return self._id


form1 = ModelForm("Логин", "Пароль")
form2 = ModelForm("Логин", "Пароль")
print(form1.get_pk())
print(form2.get_pk())