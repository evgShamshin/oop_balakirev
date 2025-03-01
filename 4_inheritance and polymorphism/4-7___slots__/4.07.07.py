class Note:
    __сyrillic_notes = 'до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'

    def __validate_name(self, name):
        if name in Note.__сyrillic_notes:
            return True
        else:
            raise ValueError('недопустимое значение аргумента')

    def __validate_ton(self, ton):
        if type(ton) == int and ton in (-1, 0, 1):
            return True
        else:
            raise ValueError('недопустимое значение аргумента')

    def __init__(self, name, ton):
        self.__validate_name(name)
        self._name = name
        self.__validate_ton(ton)
        self._ton = ton

    def __setattr__(self, key, value):
        if key == '_name':
            self.__validate_name(value)
            object.__setattr__(self, key, value)

        if key == '_ton':
            self.__validate_ton(value)
            object.__setattr__(self, key, value)


class Notes:
    __slots__ = '_do', '_re', '_mi', '_fa', '_solt', '_la', '_si'
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self._do = Note('до', 0)
        self._re = Note("ре", 0)
        self._mi = Note("ми", 0)
        self._fa = Note("фа", 0)
        self._solt = Note("соль", 0)
        self._la = Note("ля", 0)
        self._si = Note("си", 0)

    def __getitem__(self, item):
        if item < len(self.__slots__):
            return getattr(self, self.__slots__[item])
        else:
            raise IndexError('недопустимый индекс')