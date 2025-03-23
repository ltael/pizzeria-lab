from pizza import Pizza



class CustomPizza(Pizza):
    def __init__(self):
        super().__init__()
        self._name = 'Пицца'
        self._price = 100
        self._ingridients = []
        self._description = 'Вкусная пицца'

    def collect_ingredients(self):
        pass

    def cook(self):
        pass

    def __str__(self):
        return (f"{self.get_name()} - {self.get_price()} рублей.\n"
                f"{self._description}\n"
                f"Ингредиенты: {', '.join(self._ingridients)}")

    def __add__(self, other):
        if isinstance(other, CustomPizza):
            new_name = f"{self.get_name()} + {other.get_name()}"
            new_price = self.get_price() + other.get_price()
            new_ingredients = list(set(self._ingridients + other._ingridients))
            new_pizza = CustomPizza()
            new_pizza._name = new_name
            new_pizza._price = new_price
            new_pizza._ingredients = new_ingredients
            new_pizza._description = f"Комбинация пицц: {self.get_name()} и {other.get_name()}"
            return new_pizza
        else:
            raise TypeError("Можно складывать только объекты класса Pizza")

    def __sub__(self, other):
        if isinstance(other, CustomPizza):
            new_name = f"{self.get_name()} - {other.get_name()}"
            new_price = self.get_price() - other.get_price()
            new_ingredients = [ingredient for ingredient in self._ingridients if ingredient not in other._ingridients]
            new_pizza = CustomPizza()
            new_pizza._name = new_name
            new_pizza._price = new_price
            new_pizza._ingredients = new_ingredients
            new_pizza._description = f"Разница пицц: {self.get_name()} и {other.get_name()}"
            return new_pizza
        else:
            raise TypeError("Можно вычитать только объекты класса Pizza")
