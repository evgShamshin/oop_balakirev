class Notes:
    pass


atributes = {
    'uid': 1005435,
    'title': "Шутка",
    'author': "И.С. Бах",
    'pages': 2
}

[setattr(Notes, atr[0], atr[1]) for atr in atributes.items()]
print(Notes.__dict__['author'])