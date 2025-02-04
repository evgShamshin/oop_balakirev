class RadiusVector:
    def __init__(self, *args):
        self.coords = [a for a in args if self.validate_arg(a)]

    @staticmethod
    def validate_arg(a):
        if str(a)[0] == '-':
            if '.' in str(a):
                return str(a)[1:].replace('.', '').isdigit()
            else:
                return str(a)[1:].isdigit()
        elif '.' in str(a):
            return str(a).replace('.', '').isdigit()
        else:
            return str(a).isdigit()

    def __getitem__(self, i):
        print(f'getitem - {i}')
        if isinstance(i, int) and i < len(self.coords):
            return self.coords[i]
        elif isinstance(i, slice):
            return tuple(self.coords[i])

    def __setitem__(self, i, v):
        if isinstance(i, int) and i < len(self.coords):
            if self.validate_arg(v):
                self.coords[i] = v
        elif isinstance(i, slice):
            if i.step is None and i.start is not None and i.stop is not None:
                pos = [n for n in range(i.start, i.stop)]
            elif i.step is not None:
                pos = [n for n in range(i.start, i.stop, i.step)]
                print(pos)
            else:
                pos = [n for n in range(len(self.coords))]
            for _n, _v in enumerate(v):
                if self.validate_arg(_v):
                    self.coords[pos[_n]] = _v


v = RadiusVector(1, 2, 3, -1, 's', 1.2, -1.2)
coord = v[1]
print(coord)
coords_1 = v[:]
print(coords_1)
v[0] = 555
print(v.coords)
v[:] = [0, 4, 5, 6, 1.2, -1.2]
print(v.coords)