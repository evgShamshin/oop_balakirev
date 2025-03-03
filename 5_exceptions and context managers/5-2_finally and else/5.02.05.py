class Point:
    def __init__(self, *args):
        if len(args) == 0:
            self._x, self._y = 0, 0
        elif len(args) == 2:
            self._x, self._y = args

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


def valid_type(value):
    for v in value:
        try:
            int(v)
        except ValueError:
            try:
                float(v)
            except ValueError:
                raise ValueError()

    return True


val_in = input().split()

try:
    valid_type(val_in)
    pt = Point(*val_in)
except ValueError:
    pt = Point()
finally:
    print(f'Point: x = {pt.x}, y = {pt.y}')
