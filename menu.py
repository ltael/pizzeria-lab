from pizza import PeperoniPizza, BarbecuePizza, SeaGiftsPizza

class Menu:
    def __init__(self):
        self._items = [PeperoniPizza(),
                       BarbecuePizza(),
                       SeaGiftsPizza()]

    def get_item(self, number):
        if number<=len(self._items):
            return self._items[number-1]
        else:
            return None

    def __len__(self):
        return len(self._items)

    def print_menu(self):
        for item in self._items:
            print(f"{item.get_name()} - {item.get_price()} рублей.")

    def print_information(self, number):
        if number<=len(self._items):
            print(self._items[number-1])
        else:
            print(f"Позиции с номером {number} не существует.")
