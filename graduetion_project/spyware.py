# coding=utf-8

import requests
import time
import json
import os


VERSION = '5.68'
TOKEN = '5dfd6b0dee902310df772082421968f4c06443abecbc082a8440cb18910a56daca73ac8d04b25154a1128'


def call_vk_api(method='users.get', **params):
    response = requests.get('https://api.vk.com/method/{}'.format(method), params)
    time.sleep(0.5)
    print('.')
    try:
        return response.json()['response']
    except KeyError:
        err_response = response.json()['error']
        skipped_errors_nums = [18, 24, 113]
        if err_response['error_code'] in skipped_errors_nums:
            print('Ошибка VK Api №{} - "{}"'.format(err_response['error_code'],
                                                    err_response['error_msg']))
            return {'items': []}
        else:
            print('Ошибка VK Api №{} - "{}"'.format(err_response['error_code'],
                                                    err_response['error_msg']))
            exit(1)

#
# def friends_get(call_vk_api):
#     def give_arg_to_api(params):
#         params = {user_id:'user_id'{}
#         call_vk_api(method='friends.get')
#     return call_vk_api


def get_all_friends_groups(user_friends_ids):
    all_friends_groups = []
    for friend_id in user_friends_ids:
        users_groups = call_vk_api(method='groups.get',
                                   user_id=friend_id,
                                   access_token=TOKEN,
                                   v=VERSION)
        all_friends_groups.extend(users_groups['items'])
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
    path_to_work_dir = os.path.join(os.path.abspath(file_name))
    return path_to_work_dir


def create_new_folder(file_name='Results'):
        path_to_dir = get_path_to_work_dir(file_name)
        if not os.path.exists(path_to_dir):
            os.makedirs(get_path_to_work_dir(file_name), exist_ok=True)
            print('\nПапка с именем "{}" создана в директории "{}"'
                  .format(file_name, get_path_to_work_dir('')))


def record_data_to_json_file(data, path, file_name, encoding='utf=8'):
    path_to_dump_file = os.path.join(path, file_name)
    with open(path_to_dump_file, 'w', encoding=encoding) as f:
        json.dump(data,
                  f,
                  sort_keys=False,
                  indent=4,
                  ensure_ascii=False)


def dialog_window():
    while True:
        command = input("Введите, пожалуйста, комманду из списка:\n\
                        ug: get user's unique groups info(получить информацию об уникальных группах пользователя)\n\
                        q: quit(выйти из программы)\n").lower()
        if command == 'ug':
            input_id = input('\nПожалуйста, введите имя пользователя,'
                             '\nчтобы выгрузить информацию о его уникальных группах\n')
            current_user_id = call_vk_api(user_ids=input_id,
                                          access_token=TOKEN,
                                          v=VERSION)
            user_friends_ids = call_vk_api(method='friends.get',
                                           user_id=current_user_id[0]['id'],
                                           access_token=TOKEN,
                                           v=VERSION)
            user_groups = call_vk_api(method='groups.get',
                                      user_id=current_user_id[0]['id'],
                                      access_token=TOKEN,
                                      v=VERSION,
                                      fields='members_count',
                                      extended=1,
                                      count=1000)
            friend_groups = get_all_friends_groups(user_friends_ids['items'])
            groups_info = get_unique_groups_info(user_groups, friend_groups)
            create_new_folder('Results')
            path_to_work_dir = get_path_to_work_dir('Results')
            record_data_to_json_file(groups_info,
                                     path_to_work_dir,
                                     'groups.json')
            break
        elif command == 'q':
            break
        else:
            print('\nВы ввели неправильную команду\n')


if __name__ == '__main__':
    dialog_window()
