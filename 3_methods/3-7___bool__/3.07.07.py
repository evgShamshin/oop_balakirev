class Ellipse:
    def __init__(self, *args):
        if len(args) == 4 and all(type(a) == int for a in args):
            self.x1 = args[0]
            self.y1 = args[1]
            self.x2 = args[2]
            self.y2 = args[3]

    def __bool__(self):
        slf_dict = self.__dict__
        return all(('x1' in slf_dict, 'y1' in slf_dict, 'x2' in slf_dict, 'y2' in slf_dict))

    def get_coords(self):
        if not self.__bool__():
            raise AttributeError('нет координат для извлечения')
        else:
            return self.x1, self.y1, self.x2, self.y2


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]
[print(lst.get_coords()) for lst in lst_geom if bool(lst)]