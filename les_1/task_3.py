""" Task 3
Разработать генератор случайных чисел.
В функцию передавать начальное и конечное число генерации
(нуль необходимо исключить). Заполнить этими данными список и словарь.
Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
Вывести содержимое созданных списка и словаря.
"""
import random


def random_number_generator(start, end, exclusions=None):
    if not exclusions:
        exclusions = []

    while True:
        rand_num = random.randint(start, end)
        if rand_num not in exclusions:
            yield rand_num


if __name__ == '__main__':
    for el in random_number_generator(-34, 3342):
        print(el)
