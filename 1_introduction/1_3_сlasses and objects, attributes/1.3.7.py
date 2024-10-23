class Dictionary:
    pass

_list = {"rus": "Питон",
     "eng": "Python"}

[setattr(Dictionary, l[0], l[1]) for l in _list.items()]
print(getattr(Dictionary, "rus_word", False))