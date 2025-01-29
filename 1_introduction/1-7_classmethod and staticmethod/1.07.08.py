class CardCheck:
    @classmethod
    def check_card_number(cls, number):
        """
        Проверяет строку с номером карты и возвращает булево значение True,
        если номер в верном формате и False - в противном случае.
        Формат номера следующий: XXXX-XXXX-XXXX-XXXX,
        где X - любая цифра (от 0 до 9).

        :param number: Номер карты
        :return: True / False
        """
        check_list = [[z.isdigit() for z in x] for x in number.split("-")]
        if len(check_list) == 4 and all(map(lambda x: len(x) == 4 and all(x), check_list)):
            return True
        else:
            return False

    @classmethod
    def check_name(cls, name):
        """
        Проверяет строку name с именем пользователя карты.
        Возвращает булево значение True, если имя записано верно и False - в противном случае.
        Формат имени: два слова (имя и фамилия) через пробел,
        записанные заглавными латинскими символами и цифрами.

        Например, SERGEI BALAKIREV
        :param name: Имя пользователя карты
        :return: True / False
        """
        from string import ascii_lowercase, digits

        CHARS_FOR_NAME = ascii_lowercase.upper() + digits
        check_list = map(lambda x: all(z in CHARS_FOR_NAME for z in x), name.split())
        if all(check_list) and len(name.split()) == 2:
            return True
        else:
            return False


is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")

print(is_number, is_name)
