class Dimensions:
    def __init__(self, a, b, c):
        if type(a) in [int, float]:
            self.a = a
        if type(b) in [int, float]:
            self.b = b
        if type(c) in [int, float]:
            self.c = c

    def __setattr__(self, key, value):
        if value <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        else:
            self.__dict__[key] = value

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c

    def __lt__(self, other):
        return self.a < other.a and self.b < other.b and self.c < other.c

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    @staticmethod
    def a_b_c(self):
        return (self.a, self.b, self.c)


def float_or_int(num):
    return float(num) if "." in str(num) else int(num)


data_in = input().split("; ")
data_out = [list(map(float_or_int, i.split())) for i in data_in]

lst_dims = [Dimensions(*o) for o in data_out]  # 1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5
lst_dims.sort(key=hash)