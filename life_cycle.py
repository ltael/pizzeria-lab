from terminal import MakeOrder, PrintMenu, Exit

class ProgrammCycle:
    def __init__(self, terminal):
        self._terminal = terminal
        self._choices = {1: MakeOrder(terminal),
                         2: PrintMenu(terminal),
                         3: Exit()}

    def _get_input(self):
        print("Введите номер команд для выполнения.")
        for choice in self._choices:
            print(choice, '-', self._choices[choice].get_discription())
        current_choice = int(input('Выбор команды: '))

        return current_choice

    def start(self):
        choice = self._get_input()
        while True:
            if choice in self._choices:
                self._choices[choice].execute()
            else:
                print("Такой команды нет.")

            choice = self._get_input()

