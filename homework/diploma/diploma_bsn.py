#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import time
from sys import stdout
import json

base_params = {'access_token': '5dfd6b0dee902310df772082421968f4c06443abecbc082a8440cb18910a56daca73ac8d04b25154a1128',
               'v': '5.69'}
base_url = 'https://api.vk.com/method/'

def create_generator():
    i = 0
    while True:
        i += 1
        yield i


def show_progress(gen):
    i = gen.__next__()
    stdout.write('\rКоличество вызовов API: %d ' % i)
    stdout.flush()


def get_service_response(url, params, progress_gen):
    response_json = None

    for attempt_no in range(10):
        show_progress(progress_gen)

        try:
            response = requests.get(url, params)
            if response.status_code == 200:
                response_json = response.json()
                if 'error' in response_json:
                    if response_json['error']['error_code'] == 113:
                        print('Ошибка: не найден пользователь ВК по введенным данным.')
                        break
                    elif response_json['error']['error_code'] == 6:
                        time.sleep(0.5)
                    else:
                        print('Ошибка запроса к сервису ВК.')
                        print('Системная ошибка:', response_json['error']['error_msg'])
                else:
                    break
            else:
                print('Ошибка доступа к сервису ВК. Код статуса: ' + response.status_code)

        except Exception as err:
            print('Ошибка доступа к сервису ВК.')
            print('Системная ошибка:', str(err))

    if response_json and 'error' in response_json:
        response_json = None

    return response_json


def get_user_id(user_data, progress_gen):
    '''Возвращает идентификатор пользователя'''
    user_id = None
    spec_params = {'user_ids': user_data}
    params = {**base_params, ** spec_params}
    response_json = get_service_response(base_url + 'users.get', params, progress_gen)

    if response_json:
        user_id = response_json['response'][0]['id']

    return user_id


def get_user_groups(user_id, progress_gen):
    '''Возвращает список групп пользователя'''
    groups_list = None
    spec_params = {'user_id': user_id, 'extended': 1, 'fields': 'members_count'}
    params = {**base_params, **spec_params}
    response_json = get_service_response(base_url + 'groups.get', params, progress_gen)

    if response_json:
        groups_list = response_json['response']['items']
        if not groups_list:
            print('У выбранного пользователя нет групп ВК.')

    print(f'\nКоличество групп пользователя: {len(groups_list)}')
    return groups_list


def get_user_friends(user_id, progress_gen):
    '''Возвращает список друзей пользователя'''
    friends_list = None
    spec_params = {'user_id': user_id}
    params = {**base_params, **spec_params}
    response_json = get_service_response(base_url + 'friends.get', params, progress_gen)

    if response_json:
        friends_list = response_json['response']['items']
        if not friends_list:
            print('У выбранного пользователя нет друзей ВК.')

    print(f'\nКоличество друзей пользователя: {len(friends_list)}')
    return friends_list


def is_there_any_friend(group_id, friends_list, progress_gen):
    '''Возвращает True, если в группе есть кто-то из друзей пользователя'''
    result = False

    # разделим на порции по 400 штук - ограничение API ВК на кол-во id + ограничение на длину строки URI
    total_friends = len(friends_list)
    baskets = total_friends // 400
    if total_friends % 400 != 0:
        baskets += 1

    for basket_number in range(baskets):
        user_list = [str(friends_list[counter]) for counter in range(basket_number, total_friends, baskets)]
        user_ids = ','.join(user_list)
        spec_params = {'group_id': group_id, 'user_ids': user_ids}
        params = {**base_params, **spec_params}
        response_json = get_service_response(base_url + 'groups.isMember', params, progress_gen)
        if response_json:
            if not 'error' in response_json:
                for item in response_json['response']:
                    if item['member'] == 1:
                        result = True
                        break
        # Если нашли в группе хотя бы одного друга, дальше не ищем
        if result:
            break

    return result


def generate_answer_file(uncommon_groups):
    data = []
    for group in uncommon_groups:
        data.append(
            {
                'name': group['name'],
                'gid': str(group['id']),
                'members_count': group['members_count']
            }
        )

    with open('groups.json', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)

    print('\nФайл "groups.json" сформирован.')


def analize_user_groups(user_data):
    '''Анализируем данные по введенному значению пользователя'''
    progress_gen = create_generator()

    uncommon_groups = []
    # 1. Проверим, что по введенным данным существует пользователь ВК и получим его идентификатор
    user_id = get_user_id(user_data, progress_gen)
    if user_id:
        # 2. Получим список групп пользователя
        groups_list = get_user_groups(user_id, progress_gen)

        # 3. Получим список друзей пользователя
        friends_list = get_user_friends(user_id, progress_gen)

        # 4. Проверим вхождение друзей в группы пользователя
        for group in groups_list:
            result = is_there_any_friend(group['id'], friends_list, progress_gen)
            if not result:
                uncommon_groups.append(group)

    # 5. Вывод иноформации
    generate_answer_file(uncommon_groups)


if __name__ == '__main__':
    print('Программа выводит в файл "groups.json" в каталоге программы список групп в ВК, '
          'в которых состоит пользователь, но не состоит никто из его друзей.')
    user_data = input("Введите идентификатор пользователей или его короткое имя (screen_name):\n")
    if len(user_data) > 0:
        analize_user_groups(user_data)
    else:
        print('Пустое значение ввода. Файл не сформирован.')