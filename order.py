class Order:
    def __init__(self):
        self._menu_items = []

    def calculate_price(self):
        bill = 0
        for item in self._menu_items:
            bill += item.get_price()
        return bill

    def add_item(self, item):
        self._menu_items.append(item)

    def remove_item(self, number):
        self._menu_items.pop(number-1)

    def __len__(self):
        return len(self._menu_items)

    def cook(self):
        for item in self._menu_items:
            item.collect_ingredients()
            item.cook()
            item.prepare()
            item.pack()

    def print_order(self):
        for item in self._menu_items:
            print(item.get_name())
