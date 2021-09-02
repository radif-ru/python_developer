""" Task 4
Реализовать расчет цены товара со скидкой.
Величина скидки должна передаваться в качестве аргумента в дочерний класс.
Выполнить перегрузку методов конструктора дочернего класса
(метод __init__, в который должна передаваться переменная — скидка),
и перегрузку метода __str__ дочернего класса. В этом методе должна
пересчитываться цена и возвращаться результат — цена товара со скидкой.
Чтобы все работало корректно, не забудьте инициализировать дочерний и
родительский классы (вторая и третья строка после объявления дочернего класса).
"""


class ItemDiscount:
    """Родительский класс со статической информацией
    Добавлены инкапсулированные свойства и методы получения данных,
    а так же записи (сеттеры) новых значений
    """

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self.__name = val

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, val):
        self.__price = val


class ItemDiscountReport(ItemDiscount):
    """Дочерний класс от ItemDiscount, дополнен методом получения данных"""

    def __init__(self, name, price, discount=0):
        super().__init__(name, price)
        self.discount = discount

    def __str__(self):
        """ Приведение объекта к строке
        :return: возвращает цену со скидкой
        """
        discount_price = self.price - self.price * (self.discount / 100)
        return f'Цена товара со скидкой: {discount_price}'

    def get_parent_data(self):
        """Отображает информацию о товаре в одной строке"""
        print(f'name - {self.name}, price - {self.price}')


if __name__ == '__main__':
    item_discount = ItemDiscount('груша', 2500)
    print(item_discount.name, item_discount.price)

    item_discount.name, item_discount.price = 'дыня', 90000

    item_discount_report = ItemDiscountReport(
        item_discount.name, item_discount.price, 50)
    item_discount_report.get_parent_data()

    print(str(item_discount_report))
