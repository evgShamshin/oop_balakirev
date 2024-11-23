def check_name(name):
    """
    :param name: имя для проверки
    - длина имени не менее 3 символов и не более 50;
    - в именах могут использоваться только символы русского, английского алфавитов, цифры и пробелы
    """
    from string import ascii_lowercase, digits

    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits
    if name in CHARS_CORRECT and 50 > len(name) > 3:
        return True
    else:

        ("некорректное поле name")


print(check_name("123"))