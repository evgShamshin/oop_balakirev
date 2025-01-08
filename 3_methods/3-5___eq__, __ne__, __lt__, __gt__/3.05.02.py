class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


v1 = Vector(1, 2)
v2 = Vector(2, 1)
print(v1 != v2)
print(v1 == v2)
print(v1 <= v2)
print(v1 >= v2)