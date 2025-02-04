class IterColumn:
    def __init__(self, lst, column=0):
        self.lst = lst
        self.column = column

    def __iter__(self):
        # self.column = 0
        return self

    def __next__(self):
        if self.column < len(self.lst) and self.column < len(self.lst[self.column]):
            self.column = self.column + 1
            return self.lst[self.column][self.column]
        else:
            raise StopIteration


lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11', 'x12'],
       ['x20', 'x21', 'x22'],
       ['x30', 'x31', 'x32']]

ic = IterColumn(lst)
[print(i) for i in ic]
