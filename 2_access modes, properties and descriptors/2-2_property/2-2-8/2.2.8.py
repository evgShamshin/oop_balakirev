from math import sqrt


class PathLines:
    def __init__(self, *args):
        self.line = list(args)

    def get_path(self):
        return self.line

    def get_length(self):
        l = PathLines.get_path(self)[:]
        l.insert(0, LineTo(0, 0))
        return sum(
            [sqrt((l[n + 1].x - l[n].x) ** 2 + (l[n + 1].y - l[n].y) ** 2) for n, _ in enumerate(l) if n < len(l) - 1])

    def add_line(self, line):
        self.line.append(line)


class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = PathLines(LineTo(1, 2))
print(p.get_length())  # 2.23606797749979
p.add_line(LineTo(10, 20))
p.add_line(LineTo(5, 17))
print(p.get_length())  # 28.191631669843197
m = p.get_path()
print(all(isinstance(i, LineTo) for i in m) and len(m) == 3)  # True

h = PathLines(LineTo(4, 8), LineTo(-10, 30), LineTo(14, 2))
print(h.get_length())  # 71.8992593599813

k = PathLines()
print(k.get_length())  # 0
print(k.get_path())  # []
