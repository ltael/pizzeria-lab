class Order: #Класс заказа
    def __init__(self): #создаем список заказа со всеми блюдами, которые добавил пользователь
        self._menu_items = []

    def calculate_price(self): #функция, подсчитывающая окончательную сумму заказа пользователя
        bill = 0
        for item in self._menu_items:
            bill += item.get_price()
        return bill

    def add_item(self, item): #функция, добавляющая в заказ новую позицию
        self._menu_items.append(item)

    def remove_item(self, number): #функция, удаляющая из заказа определенную позицию
        self._menu_items.pop(number-1)

    def __len__(self): #функция, считающая количество позиция в заказе
        return len(self._menu_items)

    def cook(self): #функция, запускающая готовку заказа пользователя
        for item in self._menu_items:
            item.collect_ingredients()
            item.cook()
            item.prepare()
            item.pack()

    def print_order(self): #функция, выводящая все позиции из заказа пользователя
        for item in self._menu_items:
            print(item.get_name())
