class Point:
    __instance = None

    def __new__(cls, *args, **kwargs):
        cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        """
        :param x: координата точки x
        :param y: координата точки y
        """
        return Point(self.__instance.x, self.__instance.y)


pt = Point("x", "y")
pt_clone = pt.clone()