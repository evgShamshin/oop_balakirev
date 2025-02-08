class IterColumn:
    def __init__(self, lst, column=0):
        self.lst = lst
        self.column = column
        self.index = 0

    def __iter__(self):
        for i in range(len(self.lst)):
            yield self.lst[i][self.column]



lst_in = [['x00', 'x01', 'x02'],
          ['x10', 'x11', 'x12'],
          ['x20', 'x21', 'x22'],
          ['x30', 'x31', 'x32']]

ic = IterColumn(lst_in, 2)
# [print(i) for i in ic]
print(next(ic))
print(next(ic))
print(next(ic))
print(next(ic))
print(next(ic))
