class Pizza:
    def __init__(self):
        self._testoes = 'Тонкое'
        self._souse = 'Томатная соус'
        self._ingridients = ['сыр']

    def collect_ingridients(self):
        pass

    def prepare(self):
        pass

    def cook(self):
        pass

    def pack(self):
        pass

    def print_information(self):
        print(f'У пиццы {self._testoes} тесто, соус - {self._souse}, игридиенты - {self._ingridients}.')


class PeperoniPizza(Pizza):
    def __init__(self):
        self._testoes = 'Дрожжевое'
        self._souse = 'Томатный соус'
        self._ingridients = ['Сыр моцарелла', 'Сырокопченая колбаса']


class BarbecuePizza(Pizza):
    def __init__(self):
        self._testoes = 'Дрожжевое'
        self._souse = 'Соус барбекю'
        self._ingridients = ['Сыр твердый', 'Куриная грудка', 'Зелень', 'Лук']


class SeaGiftsPizza(Pizza):
    def __init__(self):
        self._testoes = 'Дрожжевое'
        self._souse = 'Соус Том Ям'
        self._ingridients = ['Крабы', 'Кальмары', 'Креветки', 'Мидии', 'Сыр твердый']

