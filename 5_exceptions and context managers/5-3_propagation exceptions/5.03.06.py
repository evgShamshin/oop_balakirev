class TupleLimit(tuple):
    def __new__(cls, lst, max_lenght):
        if len(lst) <= max_lenght:
            return super(TupleLimit, cls).__new__(cls, tuple(lst))
        else:
            raise ValueError('число элементов коллекции превышает заданный предел')


digits = list(map(float, input().split()))

try:
    res = TupleLimit(digits, 5)
    print(res)
except ValueError as e:
    print(e)