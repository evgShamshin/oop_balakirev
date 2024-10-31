# здесь объявите класс TriangleChecker
class TriangleChecker:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def is_triangle(self):
        # 1 - если хотя бы одна сторона не число (не float или int) или хотя бы одно число меньше или равно нулю
        if any([type(i[1]) not in (int, float) or i[1] <= 0 for i in self.__dict__.items()]):
            return 1
        # 3 - указанные числа a, b, c не могут являться длинами сторон треугольника
        if all([self.a + self.b > self.c,
                self.b + self.c > self.a,
                self.a + self.c > self.b]):
            return 3
        # 2 - стороны a, b, c образуют треугольник
        else:
            return 2


try:
    a, b, c = map(int, input().split())  # эту строчку не менять
except ValueError:
    print(a, b, c)

# здесь создайте экземпляр tr класса TriangleChecker и вызовите метод is_triangle() с выводом информации на экран
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())