class InputDigits:
    def __init__(self, func):
        self.__func = func

    def __call__(self, args):
        return (self.__func
                (list(map(lambda x: int(x), args.split()))))


@InputDigits
def input_dg(num):
    return num


res = input_dg(input())
print(res)