class Money:
    def __init__(self):
        self.__money = 0

    def set_money(self, value):
        self.__money = value

    def get_money(self):
        return self.__money

    def del_money(self):
        del self.__money


    money = property(get_money, set_money, del_money)


m = Money()
print(m.money)
m.money = 10
print(m.money)
res = m.money # 1
print(res)
del m.money