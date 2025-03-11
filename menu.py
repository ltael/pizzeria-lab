from pizza import PeperoniPizza, BarbecuePizza, SeaGiftsPizza


class MenuItem:
    def __init__(self, dish):
        self._price = 555
        self._name = 'Пицца'
        self._description = 'Вкусная пицца'
        self._weight = '400 грамм'
        self._ingridients = []


    def print_information(self):
        print(f'{self._name} - {self._price} рублей', self._weight, self._description, self._description, sep='\n')

class Menu:
    def __init__(self):
        self._items = [MenuItem(PeperoniPizza),
                       MenuItem(BarbecuePizza),
                       MenuItem(SeaGiftsPizza)]

    def print_information(self):
        for item in self._items:
            item.print_information()