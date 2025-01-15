class Morph:
    def __init__(self, *word):
        self.word = list(word)

    def add_word(self, word):
        self.word.append(word)

    def get_words(self):
        return tuple(self.word)

    def __eq__(self, other):
        slf_data = self.get_words() if isinstance(self, Morph) else self
        oth_data = other.get_words() if isinstance(other, Morph) else other
        if type(oth_data) == list:
            return ((oth.lower() in slf_data) for oth in oth_data)
        else:
            return oth_data.lower() in slf_data


dict_words = [Morph('связь', 'связи', 'связью', 'связей', 'связям', 'связями', 'связях'),
              Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами',
                    'формулах'),
              Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам',
                    'векторами', 'векторах'
                    ),
              Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам',
                    'эффектами', 'эффектах'
                    ), Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях'
                             )]

mw = dict_words[0]
print(mw == 'СВЯЗИ')



"""
text = input().replace(".", "")
counter = 0

for txt in text.split():
    for dict_word in dict_words:
        if txt.lower() in dict_word.get_words():
            counter += 1

print(counter)"""


"""
mw = dict_words[0]
# print(mw.get_words())
# assert mw.get_words() == ('связь', 'связи', 'связью', 'связей', 'связям', 'связями', 'связях'), "метод get_words вернул неверные данные"
mw1 = Morph('свет', 'светом')
mw1.add_word('свете')
mw1.add_word('свете')

print(mw1.get_words() == ('свет', 'светом', 'свете'))
assert mw1 == ('свет', 'светом', 'свете'), "метод get_words вернул неверные данные"
assert mw1 == 'свете', "метод == работает некорректно"
assert mw1 != 'света', "метод != работает некорректно"
assert 'сВете' == mw1, "метод == работает некорректно"
assert 'света' != mw1, "метод != работает некорректно"
"""
