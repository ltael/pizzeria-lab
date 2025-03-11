from abc import ABC, abstractmethod
from menu import Menu, MenuItem

class TerminalWorker:
    def print_menu(self):
        self._print_information


    def make_order(self):
        pass


class Command(ABC):
    @abstractmethod
    def get_discription(self):
        pass

    @abstractmethod
    def execute(self):
        pass


class PrintMenu(Command):
    def __init__(self, terminal):
        self._terminal = terminal

    def get_discription(self):
        return "Вывести меню со списком всех позиций"

    def execute(self):
        self._terminal.print_menu()


class MakeOrder(Command):
    def __init__(self, terminal):
        self._terminal = terminal

    def get_discription(self):
        return "Сделать новый заказ"

    def execute(self):
        self._terminal.make_order()


class Exit(Command):
    def get_discription(self):
        return "Завершить программу"

    def execute(self):
        exit(0)