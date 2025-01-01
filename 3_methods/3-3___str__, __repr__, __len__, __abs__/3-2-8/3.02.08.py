class DeltaClock:
    def __init__(self, *args):
        self.clock1 = args[0]
        self.clock2 = args[1]

    def __dif(self):
        return self.clock1.get_time() - self.clock2.get_time()

    def __len__(self):
        num = self.__dif()
        if num <= 0:
            return 0
        else:
            return num

    def __str__(self):
        tm = self.__dif()
        hours = tm // 3600
        if hours < 0:
            hours = 0

        minutes = (tm - hours * 3600) // 60
        if minutes < 0:
            minutes = 0

        seconds = round((((tm - hours * 3600) / 60) - minutes) * 60)
        if seconds < 0:
            seconds = 0

        if hours <= 9:
            hours = "0" + str(hours)

        if minutes <= 9:
            minutes = "0" + str(minutes)

        if seconds <= 9:
            seconds = "0" + str(seconds)

        return f'{hours}: {minutes}: {seconds}'


class Clock:
    def __init__(self, *args):
        self.hours = args[0]
        self.minutes = args[1]
        self.seconds = args[2]

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


# Тесты для класса Clock
clock1 = Clock(2, 0, 0)
clock2 = Clock(1, 15, 2)
clock3 = Clock(0, 0, 0)
clock4 = Clock(1, 0, 0)

# Проверяем создание объектов класса Clock
assert clock1.hours == 2
assert clock1.minutes == 0
assert clock1.seconds == 0

assert clock2.hours == 1
assert clock2.minutes == 15
assert clock2.seconds == 2

# Проверяем метод get_time
assert clock1.get_time() == 7200
assert clock2.get_time() == 4502
assert clock3.get_time() == 0
assert clock4.get_time() == 3600

# Тесты для класса DeltaClock
dt1 = DeltaClock(clock1, clock2)
dt2 = DeltaClock(clock2, clock3)
dt3 = DeltaClock(clock1, clock3)
dt4 = DeltaClock(clock3, clock4)

# Проверяем метод __str__
print(dt1, dt2, dt3, dt4, sep="\n")
assert str(dt1) == '00: 44: 58', f"Unexpected string representation: {str(dt1)}"
assert str(dt2) == '01: 15: 02', f"Unexpected string representation: {str(dt2)}"
assert str(dt3) == '02: 00: 00', f"Unexpected string representation: {str(dt3)}"
assert str(dt4) == '00: 00: 00', f"Unexpected string representation: {str(dt4)}"  # разница меньше 0, поэтому 0

# Проверяем метод __len__
print(len(dt1), len(dt2), len(dt3), len(dt4), sep="\n")
assert len(dt1) == 2698, f"Unexpected length: {len(dt1)}"
assert len(dt2) == 4502, f"Unexpected length: {len(dt2)}"
assert len(dt3) == 7200, f"Unexpected length: {len(dt3)}"
assert len(dt4) == 0, f"Unexpected length: {len(dt4)}"  # разница меньше 0, поэтому 0

print("Все тесты пройдены успешно!")
