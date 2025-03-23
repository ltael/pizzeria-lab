from .custom_pizza import CustomPizza
from .cook_mixin import CookMixin


class PeperoniPizza(CustomPizza, CookMixin): #дочерный класс Пиццы - ПепперониПицца
    def __init__(self):
        super().__init__()
        self._ingredients = ['Дрожжевое тесто', 'Сыр моцарелла', 'Сырокопченая колбаса', 'Томатный соус']
        self._price = 555
        self._name = 'Пицца Пепперони'
        self._description = ('Насладитесь классикой с нашей пиццей Пеперони! Тонкая хрустящая основа покрыта сочным '
                             'томатным соусом, обильно посыпана ароматным сыром моцарелла и украшена ломтиками острой '
                             'колбасы пепперони. Каждый кусочек — это идеальное сочетание пикантности, сырной нежности '
                             'и аппетитного аромата. Идеальный выбор для любителей насыщенных вкусов и настоящей '
                             'итальянской кухни. Попробуйте — и вы не сможете остановиться!')

    def collect_ingredients(self):
        print('Подготавливаем ингридиенты для пиццы Пепперони.')

    def cut_sausage(self):
        print('Нарезаем колбаски.')

    def __str__(self):
        return f'{self._name} - {self._price} рублей. \n {self._description} \n Игридиенты: {", ".join(self._ingredients)}'