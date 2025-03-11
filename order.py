from
class Order:
    def __init__(self):
        self._menu_items = []

    def calculate_price(self):
        bill = 0
        for item in self._menu_items:
            bill += item._price
