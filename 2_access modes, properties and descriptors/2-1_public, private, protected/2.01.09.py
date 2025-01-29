from string import ascii_lowercase, digits
from random import choice, randint

LETTERS = ascii_lowercase + digits + "_" + "."


class EmailValidator:
    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        res = [choice(LETTERS) for _ in range(randint(7, 10))]
        return "".join(res) + "@gmail.com"

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        if "@" in email and email.count("@") == 1:
            em1, em2 = email.split("@")
            if not all(map(lambda e: e in LETTERS, em1)):
                return False
            if len(em1) > 100:
                return False
            if len(em2) > 50:
                return False
            if em2.count(".") < 1:
                return False
            if ".." in em1 or ".." in em2:
                return False
        else:
            return False

        return True

    @staticmethod
    def __is_email_str(email):
        return type(email) == str


mail = EmailValidator.get_random_email()
print(EmailValidator.check_email(mail))


res1 = EmailValidator.check_email("sc_lib@list.ru") # True
res2 = EmailValidator.check_email("sc_lib@list_ru") # False

print(res1, res2)