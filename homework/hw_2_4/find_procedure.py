# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os
import re


def search_text(text_for_search, found_files_set):
    '''Осуществляет поиск текста в файлах sql'''
    found_files_result = set()
    search_pattern = re.compile(text_for_search, re.IGNORECASE)

    for current_file in found_files_set:
        with open(current_file) as file:
            source = file.read()
            if re.search(search_pattern, source):
                found_files_result.add(current_file)

    total_found = len(found_files_result)
    if not total_found:
        print('Совпадений не найдено.')
    elif total_found < 6:
        for found_file in found_files_result:
            print(found_file)
            print('Всего: {0}'.format(total_found))
    else:
        print('... большой список файлов ...')
        print('Всего: {0}'.format(total_found))

    return found_files_result


if __name__ == '__main__':
    migrations = 'Migrations'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    search_dir = os.path.join(current_dir, migrations)
    found_files_set = set(os.path.join(search_dir, name) for name in os.listdir(search_dir) if name.endswith('.sql'))

    while True:
        text_for_search = input('Введите строку: ')
        found_files_set = search_text(text_for_search, found_files_set)