from abc import ABC, abstractmethod
class Pizza(ABC): #абстрактный класс Пиццы с абстрактными и наследуемыми методами
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def collect_ingredients(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def cook(self):
        pass

    def prepare(self):
        print('Разрезаем Вашу пиццу.')

    def pack(self):
        print('Упаковывем Вашу пиццу.')

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price