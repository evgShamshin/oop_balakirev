from math import sqrt


class Line:
    def __init__(self, x1, y1, x2, y2):
        d_type = [int, float]
        if type(x1) in d_type and type(x2) in d_type and type(y1) in d_type and type(y2) in d_type:
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2

    def __len__(self):
        return int(sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2))

    def __bool__(self):
        return len(self) > 1


l1 = Line(1.2, 2, 4, 6)
print(bool(l1))