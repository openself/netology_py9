import os
import subprocess
from  threading import Thread

def convert_files(files_list):
    '''Изменить размер всех изображений до 200px в списке. Результат работы положить в папку «Result»'''
    if not os.path.exists('Result'):
        os.mkdir('Result')

    for file in files_list:
        command_line = r'convert {0} -resize 200 {1}'.format(os.path.join('Source', file), os.path.join('Result', file))
        subprocess.call(command_line)


def directory_listing(directory):
    '''Список всех файлов в каталоге'''
    all_files = [name for name in os.listdir(directory)]
    return all_files


def main_function():
    '''Главная исполняемая функция'''
    all_files = directory_listing('Source')
    total_files = len(all_files)
    baskets = 4
    for basket_number in range(baskets):
        basket = [all_files[counter] for counter in range(basket_number, total_files, baskets)]
        t = Thread(target=convert_files, args=(basket,))
        t.start()


if __name__ == '__main__':
    main_function()