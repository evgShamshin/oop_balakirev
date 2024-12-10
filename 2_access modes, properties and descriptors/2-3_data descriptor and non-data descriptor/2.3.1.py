class num:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Point3D:
    x = num()
    y = num()
    z = num()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p1 = Point3D(1,2,3)
print(p1.__dict__)
p1.x = 4
print(p1.__dict__)