class IteratorAttrs:
    def __iter__(self):
        for i in self.__dict__:
            yield (i, self.__dict__[i])


class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory):
        self.model = model
        self.size = size
        self.memory = memory


S = SmartPhone('SmartPhone', (150.9, 75, 7), "4 Гб")
[print((i, q)) for i, q in S]