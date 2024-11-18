class SingletonFive:
    i = 0
    __instance = None
    def __new__(cls, *args, **kwargs):
        """
        <наименование> - это данные,
        которые сохраняются в локальном свойстве name созданного объекта
        """
        return super().__new__(cls).__dict__

    def __init(self, *args, **kwargs):
        self.name = args


objs = [SingletonFive(str(n)) for n in range(10)]
print(objs)