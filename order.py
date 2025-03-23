from time import sleep

import time

class Order: #Класс заказа
    def __init__(self): #создаем список заказа со всеми блюдами, которые добавил пользователь
        self._menu_items = []

    def calculate_price(self): #функция, подсчитывающая окончательную сумму заказа пользователя
        bill = 0
        for item in self._menu_items:
            bill += item.get_price()
        return bill

    def check_adding(function):
        def wrapper(self, item):
            start_menu = len(self._menu_items)
            function(self, item)
            end_menu = len(self._menu_items)
            if (end_menu-start_menu)!=0:
                print('Блюдо добавлено в заказ.')
            else:
                print('Вы ничего не добавили в заказ.')
        return wrapper

    @check_adding
    def add_item(self, item): #функция, добавляющая в заказ новую позицию
        self._menu_items.append(item)

    def remove_item(self, number): #функция, удаляющая из заказа определенную позицию
        self._menu_items.pop(number-1)

    def __len__(self): #функция, считающая количество позиция в заказе
        return len(self._menu_items)

    def track_time(function):
        def wrapper(self):
            start_time = time.time()
            function(self)
            end_time = time.time()
            print(f'Ваш заказ готовился {(end_time - start_time)*1000} милисекунд.')
        return wrapper

    def check_order(function):
        def wrapper(self):
            if len(self._menu_items)>0:
                function(self)
            else:
                print('Нечего готовить(.')
        return wrapper

    @track_time #сам все функции из cook отправляет в track_time
    @check_order
    def cook(self): #функция, запускающая готовку заказа пользователя
        sleep(1)
        for item in self._menu_items:
            item.collect_ingredients()
            item.cook()
            item.prepare()
            item.pack()

    def print_order(self): #функция, выводящая все позиции из заказа пользователя
        for item in self._menu_items:
            print(item.get_name())
