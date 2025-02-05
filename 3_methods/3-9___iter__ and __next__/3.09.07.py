class IterColumn:
    def __init__(self,lst, column=0):
        self._lst = lst
        self.column = column
        self.index = 0

    def __iter__(self):
        self.index = self.column - self.index - 1
        return self

    def __next__(self):
        if self.index < len(self._lst):
            res = self._lst[self.index][self.column]
            return res
        else:
            raise StopIteration


lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11', 'x12'],
       ['x20', 'x21', 'x22'],
       ['x30', 'x31', 'x32']]

ic = IterColumn(lst, 2)
[print(i) for i in ic]
print(next(ic))
print(next(ic))
print(next(ic))
print(next(ic))
print(next(ic))