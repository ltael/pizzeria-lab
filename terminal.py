from abc import ABC, abstractmethod
from menu import Menu
from waiter import Waiter


class TerminalWorker: #класс, обрабатывающий выбор в дальнейшем действии пользователя
    def __init__(self):
        self._menu = Menu()
        self._waiter = Waiter(self._menu)

    def print_menu(self):
        self._menu.print_menu()

    def make_order(self):
        self._waiter.start_order()


class Command(ABC): #абстрактный класс Команды с абстрактными методами
    @abstractmethod
    def get_discription(self):
        pass

    @abstractmethod
    def execute(self):
        pass


class PrintMenu(Command): #дочерний класс Вывода меню класса Команды
    def __init__(self, terminal):
        self._terminal = terminal

    def get_discription(self):
        return "Вывести меню со списком всех позиций"

    def execute(self):
        self._terminal.print_menu()


class MakeOrder(Command): #дочерний класс Создания заказа класса Команды
    def __init__(self, terminal):
        self._terminal = terminal

    def get_discription(self):
        return "Сделать новый заказ"

    def execute(self):
        self._terminal.make_order()


class Exit(Command): #дочерний класс Конца программы класса Команды
    def get_discription(self):
        return "Завершить программу"

    def execute(self):
        exit(0)