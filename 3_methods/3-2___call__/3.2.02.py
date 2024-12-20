from random import randrange as r_rng, choice as r_ch


class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self):
        min = self.min_length
        max = self.max_length
        return "".join(r_ch(self.psw_chars) for _ in range(r_rng(min, max)))


rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*",
                     5, 20)

lst_pass = (rnd() for _ in range(3))
print(list(lst_pass))