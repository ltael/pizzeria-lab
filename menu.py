from exceptions import NotExistingItemError
from pizza import PeperoniPizza, BarbecuePizza, SeaGiftsPizza

class Menu: #класс Меню, который хранит все позиции данной пиццерии
    def __init__(self):
        self._items = [PeperoniPizza(),
                       BarbecuePizza(),
                       SeaGiftsPizza()]

    def get_item(self, number):
        if number<=len(self._items):
            return self._items[number-1]
        else:
            raise NotExistingItemError("Your item doesn't exist")

    def __len__(self):
        return len(self._items)

    def print_menu(self): #функция, выводящая все позиции меню и их стоимость
        for item in self._items:
            print(f"{item.get_name()} - {item.get_price()} рублей.")

    def print_information(self, number): #фунция, выводящая все характеристики нужной позиции
        if number<=len(self._items):
            print(self._items[number-1])
        else:
            raise NotExistingItemError("Your item doesn't exist")
