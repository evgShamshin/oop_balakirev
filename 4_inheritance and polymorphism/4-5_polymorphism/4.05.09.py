class Track:
    def __init__(self, *args):
        self.__points = list(args)

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points = [pt] + self.__points

    def pop_back(self):
        self.__points.pop(-1)

    def pop_front(self):
        self.__points.pop(0)


class PointTrack:
    def __init__(self, *args):
        if all([type(a) in (int, float) for a in args]):
            self.x, self.y = args
        else:
            raise TypeError('координаты должны быть числами')

    def __str__(self):
        return f'PointTrack: {self.x}, {self.y}'


pt = PointTrack(1, 2)
print(pt)  # PointTrack: 1, 2
tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.add_front(PointTrack(2.4, 0))
for pt in tr.points:
    print(pt)
