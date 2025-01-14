class StringText:
    def __init__(self, lst_words):
        self.lst_words = lst_words

    def __lt__(self, other):
        return len(self.lst_words) < len(other.lst_words)

    def __gt__(self, other):
        return len(self.lst_words) > len(other.lst_words)

    def __le__(self, other):
        return len(self.lst_words) <= len(other.lst_words)

    def __ge__(self, other):
        return len(self.lst_words) >= len(other.lst_words)


stich = ["Я к вам пишу – чего же боле?",
         "Что я могу еще сказать?",
         "Теперь, я знаю, в вашей воле",
         "Меня презреньем наказать.",
         "Но вы, к моей несчастной доле",
         "Хоть каплю жалости храня,",
         "Вы не оставите меня."]

chars = ["– ", "?", "!", ",", ".", ";", ","]

for n, s in enumerate(stich):
    for char in chars:
        if char in stich[n]:
            stich[n] = stich[n].replace(char, "")

lst_text = [StringText(s) for s in stich]
lst_text_sorted = sorted([lst.lst_words for lst in lst_text],
                         key=lambda word: len(word.split()), reverse=True)

print(lst_text_sorted)

# TEST-TASK___________________________________
assert all([[True if i in _ else False for i in "–?!,.;"] for _ in stich]), \
    "в stich есть знаки которые нужно удалить - (–?!,.;)"
assert len(lst_text) == 7 and all(
    True if isinstance(_, StringText) else False for _ in lst_text), "ошибка в lst_text"

assert lst_text_sorted == ['Я к вам пишу чего же боле',
                           'Теперь я знаю в вашей воле',
                           'Но вы к моей несчастной доле',
                           'Что я могу еще сказать',
                           'Хоть каплю жалости храня',
                           'Вы не оставите меня',
                           'Меня презреньем наказать'], "неверно отсортирован список lst_text_sorted"

assert lst_text[0] > lst_text[4] and lst_text[4] > lst_text[1], "метод > работает неверно"
assert lst_text[1] < lst_text[4], "метод < работает неверно"

assert lst_text[2] >= lst_text[4], "метод >= работает неверно"
assert lst_text[2] <= lst_text[4], "метод >= работает неверно"

print("Правильный ответ.")