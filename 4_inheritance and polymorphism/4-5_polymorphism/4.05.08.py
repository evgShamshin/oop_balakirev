from abc import ABC, abstractmethod


class CountryInterface(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def population(self):
        pass

    @property
    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class Country(CountryInterface):
    def __init__(self, name, population, square):
        self._name = name
        self._population = population
        self._square = square

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, data):
        self._name = data

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, data):
        self._population = data

    @property
    def square(self):
        return self._square

    @square.setter
    def square(self, data):
        self._square = data

    def get_info(self):
        return f"{self.name}: {self.square}, {self.population}"


# -----test-task-----
country = Country("Россия", 140000000, 324005489.55)
name = country.name
pop = country.population
country.population = 150000000
country.square = 354005483.0
print(country.get_info())  # Россия: 354005483.0, 150000000
res = None
