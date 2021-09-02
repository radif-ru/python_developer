""" Task 2
Инкапсулировать оба параметра (название и цену) товара родительского класса.
Убедиться, что при сохранении текущей логики работы программы будет
сгенерирована ошибка выполнения. Усовершенствовать родительский класс
таким образом, чтобы получить доступ к защищенным переменным.
Результат выполнения заданий 1 и 2 должен быть идентичным.
"""


class ItemDiscount:
    """Родительский класс со статической информацией
    Добавлены инкапсулированные свойства и методы получения данных
    """

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):
    """Дочерний класс от ItemDiscount, дополнен методом получения данных"""

    def get_parent_data(self):
        """Отображает информацию о товаре в одной строке"""
        print(f'name - {self.name}, price - {self.price}')


if __name__ == '__main__':
    item_discount = ItemDiscount('груша', 2500)
    print(item_discount.name, item_discount.price)

    item_discount_report = ItemDiscountReport(
        item_discount.name, item_discount.price)
    item_discount_report.get_parent_data()
