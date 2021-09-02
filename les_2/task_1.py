""" Task 1
Проверить механизм наследования в Python. Для этого создать два класса.
Первый — родительский (ItemDiscount), должен содержать статическую информацию
о товаре: название и цену. Второй — дочерний (ItemDiscountReport),
должен содержать функцию (get_parent_data), отвечающую за отображение
информации о товаре в одной строке. Проверить работу программы,
создав экземпляр (объект) родительского класса.
"""


class ItemDiscount:
    """Родительский класс со статической информацией"""

    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    """Дочерний класс от ItemDiscount, дополнен методом получения данных"""

    def get_parent_data(self):
        """Отображает информацию о товаре в одной строке"""
        print(f'name - {self.name}, price - {self.price}')


if __name__ == '__main__':
    item_discount = ItemDiscount('груша', 2500)

    item_discount_report = ItemDiscountReport(
        item_discount.name, item_discount.price)
    item_discount_report.get_parent_data()
