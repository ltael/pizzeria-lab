from order import Order
from camel_case_meta import CamelCaseMeta
from exceptions import NotExistingItemError, EmptyItemProceedError
import asyncio

class Waiter(metaclass=CamelCaseMeta): #класс Официанта, работающего с пользователем
    def __init__(self, menu):
        self._menu = menu

    def start_order(self): #функция, отвечающая за общение с пользователем и обработку его желаний
        self._finished = False
        self._current_order = Order()
        while not self._finished:
            # try:
                print('Чем я могу Вам помочь? \n 1) Вывести информацию о блюде \n 2) Добавить блюдо в заказ \n 3) Удалить блюдо из заказа \n 4) Подтвердить заказ')
                choice = int(input('Введите Ваш выбор: '))

                if choice == 1:
                    print(f"Информацию о каком блюде Вам показать?")
                    self._menu.print_menu()
                    dish = int(input('Введите Ваш выбор ввиде цифры от 1 до 3: '))
                    try:
                        self._menu.print_information(dish)
                    except NotExistingItemError:
                        print('Такого выбора нет')

                elif choice == 2:
                        self._add_item()

                elif choice == 3:
                    self._remove_item()

                elif choice == 4:
                    print("Ваш заказ: ")
                    self._current_order.print_order()
                    print("Сумма заказа: ", self._current_order.calculate_price())
                    asyncio.run(self._current_order.cook())
                    self._finished = True

                else:
                    print('Такого варианта ответа нет.')
            # except:
            #     print("Ой! Что-то пошло не так( Давайте попробуем еще раз?!")


    def _add_item(self):
        print(f"Какое блюдо Вы хотите добавить в заказ?")
        self._menu.print_menu()
        print(f"Объединить две пиццы")
        print(f"Убрать из пиццы игридиенты из другой пиццы")
        dish = int(input('Введите Ваш выбор ввиде цифры от 1 до 5: '))

        try:
            if dish <= len(self._menu):
                self._current_order.add_item(self._menu.get_item(dish))
            elif dish == (len(self._menu)+1):
                print(f"Какие две пиццы Вы хотите объединить?")
                self._menu.print_menu()
                pizza1 = int(input('Введите цифру от 1 до 3 первой пиццы: '))
                pizza2 = int(input('Введите цифру от 1 до 3 второй пиццы: '))
                combin_pizza = self._menu.get_item(pizza1) + self._menu.get_item(pizza2)
                self._current_order.add_item(combin_pizza)
            elif dish == (len(self._menu)+2):
                print("Игридиенты какой пиццы вы хотите убрать из какой пиццы?")
                self._menu.print_menu()
                pizza1 = int(input('Введите цифру от 1 до 3 пиццы, из которой будем убирать игридиенты: '))
                pizza2 = int(input('Введите цифру от 1 до 3 пиццы, игридиенты которой будет убирать: '))
                combin_pizza = self._menu.get_item(pizza1) - self._menu.get_item(pizza2)
                self._current_order.add_item(combin_pizza)
            else:
                raise EmptyItemProceedError("Нельзя добавить несуществующую позицию")
        except NotExistingItemError:
            print('Такого выбора нет')


    def _remove_item(self):
        print(f"Какое блюдо Вы хотите удалить из заказа?")
        self._current_order.print_order()
        dish = int(input(f'Введите Ваш выбор ввиде цифры от 1 до {len(self._current_order)}: '))
        if dish <= len(self._current_order):
            self._current_order.remove_item(dish)
        else:
            raise EmptyItemProceedError("Нельзя удалить несуществующую позицию")