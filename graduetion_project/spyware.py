# coding=utf-8

import requests
import time
import json
import os

VERSION = '5.68'
TOKEN = '5dfd6b0dee902310df772082421968f4c06443abecbc082a8440cb18910a56daca73ac8d04b25154a1128'


def get_user_id(user_id):
    params = {
        'user_ids': user_id,
        'access_token': TOKEN,
        'fields': 'screen_name',
        'v': VERSION
    }
    response = requests.get('https://api.vk.com/method/users.get', params)
    return response.json()['response'][0]['id']


def get_ids_of_friends_or_groups(user_id,
                                 method='friends.get',
                                 fields=None,
                                 extended=0,
                                 count=1000):
    params = {
        'user_id': user_id,
        'access_token': TOKEN,
        'fields': fields,
        'extended': extended,
        'count': count,
        'v': VERSION
    }
    try:
        response = requests.get('https://api.vk.com/method/{}'.format(method), params)
        time.sleep(0.5)
        print('.')
        return response.json()['response']
    except KeyError:
        print('Пользователь {} был заблокирован или удалил свою страницу.'
              .format(user_id))
        return {'items': []}


def get_all_friends_groups(user_friends_ids):
    all_friends_groups = []
    for friend_id in user_friends_ids:
        users_groups = get_ids_of_friends_or_groups(friend_id,
                                                    method='groups.get')
        for group_id in users_groups['items']:
            all_friends_groups.append(group_id)
    return all_friends_groups


def get_unique_groups_info(user_groups, friend_groups):
    set_of_user_groups_ids = {group['id'] for group in user_groups['items']}
    set_of_only_user_groups = set_of_user_groups_ids.difference(set(friend_groups))
    unique_groups_info = []
    for group_id in set_of_only_user_groups:
        dict_of_groups_info = {}
        for user_group in user_groups['items']:
            if group_id == user_group['id']:
                dict_of_groups_info['name'] = user_group['name']
                dict_of_groups_info['gid'] = user_group['id']
                dict_of_groups_info['members_count'] = user_group['members_count']
        unique_groups_info.append(dict_of_groups_info)
    return unique_groups_info


def get_path_to_work_dir(file_name=''):
    path_to_work_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
    return path_to_work_dir


def create_new_folder(file_name='Results'):
    if not os.path.isdir(get_path_to_work_dir(file_name)):
        os.mkdir(get_path_to_work_dir(file_name))
        print('\nПапка с именем "{}" создана в директории "{}"'
              .format(file_name, get_path_to_work_dir('')))


def record_data_to_json_file(data, path, file_name, encoding='utf=8'):
    with open(os.path.join(os.path.abspath(path), file_name),
              'w',
              encoding=encoding) as f:
        json.dump(data, f)


def dialog_window():
    while True:
        command = input("Введите, пожалуйста, комманду из списка:\n\
                        ug: get user's unique groups info(получить информацию об уникальных группах пользователя)\n\
                        q: quit(выйти из программы)\n").lower()
        if command == 'ug':
            input_id = input('\nПожалуйста, введите имя пользователя,'
                             '\nчтобы выгрузить информацию о его уникальных группах\n')
            current_user_id = get_user_id(input_id)
            user_friends_ids = get_ids_of_friends_or_groups(current_user_id)
            user_groups = get_ids_of_friends_or_groups(current_user_id,
                                                       method='groups.get',
                                                       fields='members_count',
                                                       extended=1)
            friend_groups = get_all_friends_groups(user_friends_ids['items'])
            groups_info = get_unique_groups_info(user_groups, friend_groups)
            record_data_to_json_file(groups_info,
                                     get_path_to_work_dir('Results'),
                                     'groups.json')
            exit(0)
        elif command == 'q':
            exit(0)
        else:
            print('\nВы ввели неправильную команду\n')

if __name__ == '__main__':
    dialog_window()
