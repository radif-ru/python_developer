""" Task 1
Написать программу, которая будет содержать функцию для получения имени
файла из полного пути до него. При вызове функции в качестве аргумента
должно передаваться имя файла с расширением. В функции необходимо
реализовать поиск полного пути по имени файла, а затем «выделение»
из этого пути имени файла (без расширения).
"""
from os.path import abspath


def get_name_from_full_path(file_name: str) -> str:
    """Получения имени файла из полного пути до него
    :param file_name: str имя файла с расширением
    :return: str имя файла (без расширения)
    """
    abs_path = abspath(file_name)
    name = '.'.join(abs_path.split('\\')[-1].split('.')[0:-1])
    return name


if __name__ == '__main__':
    print(get_name_from_full_path('example.file.exe'))
