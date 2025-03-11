from abc import ABC, abstractmethod
class TerminalWorker:
    def print_menu(self):
        pass

    def receive_order(self):
        pass


class Command:
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
        self._terminal.receive_order()


class Exit(Command):
    def get_discription(self):
        return "Завершить программу"

    def execute(self):
        exit(0)