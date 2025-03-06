class PrimaryKeyError(Exception):
    def __init__(self, id=None, pk=None):
        self.id = id
        self.pk = pk

    def __str__(self):
        if self.id == None and self.pk == None:
            return 'Первичный ключ должен быть целым неотрицательным числом'

        if self.id != None:
            return f'Значение первичного ключа id = {self.id} недопустимо'

        if self.pk != None:
            return f'Значение первичного ключа pk = {self.pk} недопустимо'


er = PrimaryKeyError(id='-10.5')
print(er)