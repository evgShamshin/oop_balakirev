# здесь объявляйте класс Money
class Money:
    def __init__(self, money=0):
        self.money = int(money)


my_money = Money(100)
your_money = Money(1000)
print(my_money.__dict__)
print(your_money.__dict__)