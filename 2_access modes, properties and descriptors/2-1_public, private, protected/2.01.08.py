class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, *args):
        if all([self.check_point(i) for i in args]):
            self.set_coords(*args)
        else:
            self.__x1, self.__y1 = args[0], args[1]
            self.__x2, self.__y2 = args[2], args[3]

    def set_coords(self, sp, ep):
        self.__x1, self.__y1 = sp.get_coords()
        self.__x2, self.__y2 = ep.get_coords()
        self.__sp = sp
        self.__ep = ep

    def check_point(self, point):
        return type(point) is Point

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f"Прямоугольник с координатами: ({self.__x1}, {self.__y1}) ({self.__x2}, {self.__y2})")


rect = Rectangle(0, 0, 20, 34)

p1 = Point(1, 2)
p2 = Point(3, 4)

r2 = Rectangle(1, 2, 3, 4)
r1 = Rectangle(p1, p2)

print(r1.get_coords())  # (1, 2, 3, 4)
r1.draw()  # Прямоугольник с координатами: (1, 2) (3, 4)
print()
# print(r2.get_coords())  # (1, 2, 3, 4)
r2.draw()  # Прямоугольник с координатами: (1, 2) (3, 4)
