class Clock:
    def __init__(self):
        self.__tm = 0

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time

    def __check_time(self, tm):
        return 0 <= tm < 100001 and type(tm) == int


clock = Clock()
clock.set_time(4530)
print(clock.get_time())
print(isinstance(clock, Clock))
print(hasattr(clock, 'set_time'))
print(hasattr(clock, 'get_time'))

clock = Clock(4530)
clock.set_time(15)
print(clock.get_time())  #15
clock.set_time(100000)
clock.set_time(-1)
clock.set_time('2')
clock.set_time(0.1)
print(clock.get_time())  #15