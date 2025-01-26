import sys


class MailItem:
    def __init__(self, mail_from, title, content):
        if type(mail_from) == str:
            self.mail_from = mail_from
        if type(title) == str:
            self.title = title
        if type(content) == str:
            self.content = content
        self.is_read = False

    def set_read(self, fl_read):
        self.is_read = fl_read

    def __bool__(self):
        return self.is_read


class MailBox:
    def __init__(self):
        self.inbox_list = []

    def receive(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        self.inbox_list = [MailItem(*lst.split("; ")) for lst in lst_in]


"""lst_in = ['sc_lib@list.ru; От Балакирева; Успехов в IT!',
          'mail@list.ru; Выгодное предложение; Вам одобрен кредит.',
          'Python ООП; Балакирев С.М.; 2022',
          'mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить.']
"""

mail = MailBox()
mail.receive()
# [print(bool(m), end=" ") for m in mail.inbox_list]
# print()
[m.set_read(True) for n, m in enumerate(mail.inbox_list) if n in [0, (len(mail.inbox_list) - 1)]]
# [print(bool(m), end=" ") for m in mail.inbox_list]
inbox_list_filtered = list(filter(lambda m: m.is_read, mail.inbox_list))
print(inbox_list_filtered)