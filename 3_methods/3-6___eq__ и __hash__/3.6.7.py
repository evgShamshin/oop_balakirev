class DataBase:
    def __init__(self, path):
        self.path = path
        self.dict_db = {}

    def write(self, record):
        self.dict_db[record] = record

    def read(self, pk):
        return self.dict_db[pk]


class Record:
    def __init__(self, fio, descr, old):
        if type(fio) == str:
            self.fio = fio
        if type(descr) == str:
            self.descr = descr
        if type(old) == int:
            self.old = old