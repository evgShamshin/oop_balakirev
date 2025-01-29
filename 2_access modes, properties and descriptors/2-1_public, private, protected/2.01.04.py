class Money:
    def __init__(self, mn):
        self.__money = mn

    def set_money(self, mn):
        if self.check_money(mn): self.__money = mn

    def get_money(self):
        return self.__money

    def add_money(self, mn):
        self.__money += mn.get_money()

    def check_money(self, mn):
        return type(mn) == int and mn > 0


mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(100)
mn_2.add_money(mn_1)
m1 = mn_1.get_money()    # 100
m2 = mn_2.get_money()    # 120

print(m1)
print(m2)