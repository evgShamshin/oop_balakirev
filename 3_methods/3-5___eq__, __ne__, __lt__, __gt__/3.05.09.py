class Body:
    def __init__(self, name, ro, volume):
        if type(name) == str:
            self.name = name
        if type(ro) in (int, float):
            self.ro = ro
        if type(volume) in (int, float):
            self.volume = volume
            self.m = ro * volume

    @classmethod
    def __data_verify(cls, data):
        return data if not isinstance(data, Body) else data.m

    def __eq__(self, other):
        return Body.__data_verify(self) == Body.__data_verify(other)

    def __lt__(self, other):
        return Body.__data_verify(self) < Body.__data_verify(other)

    def __gt__(self, other):
        return Body.__data_verify(self) > Body.__data_verify(other)


body1 = Body(name='<NAME>', ro=100, volume=100)
body2 = Body(name='<NAME>', ro=200, volume=200)

body1 > body2  # True, если масса тела body1 больше массы тела body2
body1 == body2  # True, если масса тела body1 равна массе тела body2
body1 < 10  # True, если масса тела body1 меньше 10
body2 == 5  # True, если масса тела body2 равна 5
