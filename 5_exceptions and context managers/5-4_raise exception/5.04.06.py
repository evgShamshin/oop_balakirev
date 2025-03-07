from datetime import datetime


class DateString:
    def __init__(self, date):
        try:
            self.date = datetime.strptime(date, '%d.%m.%Y').strftime('%d.%m.%Y')
        except ValueError:
            raise DateError

    def __str__(self):
        return self.date


class DateError(Exception):
    def __str__(self):
        return 'Неверный формат даты'


date_string = input()
try:
    res = DateString(date_string)
    print(res)
except DateError as er:
    print(er)
