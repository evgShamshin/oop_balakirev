from random import choice as ch

class Line:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.sp, self.ep, = (a, b), (c, d)
class Rect:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.sp, self.ep, = (a, b), (c, d)

class Ellipse:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.sp, self.ep, = (a, b), (c, d)

_class = [Line, Rect, Ellipse]
elements = [ch(_class)(2,1,3,4) for i in range(217)]

for n, i in enumerate(elements):
    if i.__class__.__name__ == 'Line':
        i.ep, i.sp = (0, 0), (0, 0)

