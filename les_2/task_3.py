""" Task 3
Реализовать возможность переустановки значения цены товара.
Необходимо, чтобы и родительский, и дочерний классы получили новое значение
цены. Следует проверить это, вызвав соответствующий метод родительского
класса и функцию дочернего (функция, отвечающая за отображение информации
о товаре в одной строке).
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

    def get_parent_data(self):
        """Отображает информацию о товаре в одной строке"""
        print(f'name - {self.name}, price - {self.price}')


if __name__ == '__main__':
    item_discount = ItemDiscount('груша', 2500)
    print(item_discount.name, item_discount.price)

    item_discount.name, item_discount.price = 'дыня', 90000

    item_discount_report = ItemDiscountReport(
        item_discount.name, item_discount.price)
    item_discount_report.get_parent_data()
