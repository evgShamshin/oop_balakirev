class Model:
    def query(self, *args, **kwargs):
        setattr(self, 'query_flag', True)
        [setattr(self, key, value) for key,value in kwargs.items()]

    def __str__(self):
        if 'query_flag' in self.__dict__:
            self.__delattr__('query_flag')
            return "Model:" + ", ".join([f'{d} = {y}' for d, y in self.__dict__.items()])
        else:
            return "Model"


m = Model()
m.query(id=1, fio='Sergey', old=33)
print(m)