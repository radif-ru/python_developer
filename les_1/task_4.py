""" Task 4
Написать программу «Банковский депозит».
Она должна состоять из функции и ее вызова с аргументами.
Клиент банка делает депозит на определенный срок.
В зависимости от суммы и срока вклада определяется процентная
ставка: 1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых,
2 года — 5 % годовых). 10000–100000 руб (6 месяцев — 6 % годовых,
год — 7 % годовых, 2 года – 6.5 % годовых). 100000–1000000 руб
(6 месяцев — 7 % годовых, год — 8 % годовых, 2 года — 7.5 % годовых).
Необходимо написать функцию, в которую будут передаваться параметры:
сумма вклада и срок вклада. Каждый из трех банковских продуктов должен быть
представлен в виде словаря с ключами (begin_sum, end_sum, 6, 12, 24).
Ключам соответствуют значения начала и конца диапазона суммы вклада и
значения процентной ставки для каждого срока. В функции необходимо проверять
принадлежность суммы вклада к одному из диапазонов и выполнять расчет по
нужной процентной ставке. Функция возвращает сумму вклада на конец срока.
"""

bank_dep_1 = {'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5}
bank_dep_2 = {'begin_sum': 10000, 'end_sum': 100000, 6: 5, 12: 7, 24: 6.5}
bank_dep_3 = {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5}
bank_deposits = [bank_dep_1, bank_dep_2, bank_dep_3]


def calculate_total_amount(amount: float, term: int) -> float or str:
    """ Функция возвращает сумму вклада на конец срока
    :param amount: сумму вклада
    :param term: срок вклада
    :return: сумма вклада на конец срока
    """
    total_amount = 0
    try:
        for bank_deposit in bank_deposits:
            if bank_deposit['begin_sum'] <= amount < bank_deposit['end_sum']:
                total_amount = amount
                percent = bank_deposit[term] / 100

                total_amount += amount * percent * (term / 12)
        if not total_amount:
            raise ValueError('Указана неправильная сумма вклада')
        return total_amount
    except KeyError as e:
        return f'Указан неправильный срок вклада. KeyError {e}'
    except ValueError as e:
        return e


if __name__ == '__main__':
    print(calculate_total_amount(10, 1))
    print(calculate_total_amount(1000, 3))

    print(calculate_total_amount(1000, 24))
    print(calculate_total_amount(9999, 12))
    print(calculate_total_amount(1000, 12))
    print(calculate_total_amount(10000, 6))
