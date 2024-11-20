class Point:
    def __init__(self, x, y, color='black'):
        self.x, self.y, self.color = x, y, color


points = [Point(i, i) for n, i in enumerate(range(1, 2001, 2))]
points[1] = Point(3, 3, color='yellow')

print(points)