class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.points = []

    def add_point(self, x, y, speed):
        self.points.append([x, y, speed])

    def __getitem__(self, index):
        if 0 <= index < len(self.points):
            slf = self.points[index]
            return (slf[0], slf[1]), slf[2]
        else:
            raise IndexError('некорректный индекс')

    def __setitem__(self, index, value):
        if 0 <= index < len(self.points):
            if type(value) in [int, float]:
                self.points[index][2] = value
        else:
            raise IndexError('некорректный индекс')


tr = Track(10, -5.4)
tr.add_point(20, 0, 100)  # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80)  # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34)  # третий линейный сегмент: indx = 2
print(tr.points)
print(tr[2])
c, s = tr[2]
print(c, s)
tr[2] = 60
c, s = tr[2]
print(c, s)

res = tr[3]  # IndexError
