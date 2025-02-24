class Aircraft:
    def __init__(self, model, mass, speed, top):
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    def __setattr__(self, key, value):
        valid_data = ('_weapons', '_model', '_mass', '_speed', '_top', '_chairs')
        if key in valid_data:
            if valid_data[1] == key and type(value) == str:
                self.__dict__[key] = value
                return None

            if key in valid_data[2:-1] and type(value) in (int, float) and value > 0:
                self.__dict__[key] = value
                return None

            if valid_data[-1] == key and type(value) == int and value > 0:
                self.__dict__[key] = value
                return None

            if valid_data[0] == key and type(value) == dict:
                self.__dict__[key] = value
                return None

            raise TypeError('неверный тип аргумента')


class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._chairs = chairs


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self._weapons = weapons


planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]