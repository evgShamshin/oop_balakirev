class SingletonFive:
    i = 0
    __instance = None

    def __new__(cls, *args, **kwargs):
        """
        <наименование> - это данные,
        которые сохраняются в локальном свойстве name созданного объекта
        """
        if cls.i < 5:
            cls.i += 1
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self, *args, **kwargs):
        self.name = args


objs = [SingletonFive(str(n)) for n in range(10)]
print(objs)