""" Task 5
Проверить на практике возможности полиморфизма.
Необходимо разделить дочерний класс ItemDiscountReport на два класса.
Инициализировать классы необязательно. Внутри каждого поместить функцию
get_info, которая в первом классе будет отвечать за вывод названия товара,
а вторая — его цены. Далее реализовать выполнение каждой из функции тремя
способами.
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


class ItemDiscountReportInfoName(ItemDiscount):
    def get_info(self):
        print(self.name)


class ItemDiscountReportInfoPrice(ItemDiscount):
    def get_info(self):
        print(self.price)


if __name__ == '__main__':
    first_informer = ItemDiscountReportInfoName('капуста', 100000)
    second_informer = ItemDiscountReportInfoPrice('лук', 9999999999)

    def get_information(obj):
        obj.get_info()

    def get_information_2(*args):
        for arg in args:
            arg.get_info()

    get_information(first_informer)
    get_information(second_informer)

    get_information_2(first_informer, second_informer)

    for obj in (first_informer, second_informer):
        obj.get_info()



