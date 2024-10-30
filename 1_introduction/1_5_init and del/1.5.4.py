from random import randrange as r, choice as ch

class Line:
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = 0, 0, 0, 0
class Rect:
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d

class Ellipse:
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d

_class = [Line, Rect, Ellipse]
elements = [ch(_class)(0,1,3,4) for i in range(217)]
