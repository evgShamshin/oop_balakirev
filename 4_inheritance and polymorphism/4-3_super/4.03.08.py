class SoftList(list):
    def __init__(self, data):
        super().__init__(data)

    def __getitem__(self, index):
        if index < 0:
            if abs(index) <= len(self):
                return super().__getitem__(index)
        else:
            if index < len(self):
                return super().__getitem__(index)
        return False


sl = SoftList("python")
r0 = sl[0]  # 'p'
r1 = sl[-1]  # 'n'
er1 = sl[6]  # False
er2 = sl[-7]  # False
