# coding=utf-8

from pprint import pprint
import requests
from urllib.parse import urlencode
from collections import Counter
import time
import os


VERSION = '5.68'
# TOKEN = '5dfd6b0dee902310df772082421968f4c06443abecbc082a8440cb18910a56daca73ac8d04b25154a1128'
TOKEN = 'ac258fb52dc7caa382d18c2a65a02e513b930f7aa26ebec4fc91103634cafb6d7287d8afd892d2a092e82'


def get_user_id(user_id):
    params = {
        'user_ids': user_id,
        'access_token': TOKEN,
        'fields': 'screen_name',
        'v': VERSION
    }
    response = requests.get('https://api.vk.com/method/users.get', params)
    return response.json()['response'][0]['id']


def get_user_friend_ids(user_id):
    params = {
        'user_id': user_id,
        'access_token': TOKEN,
        'order': 'name',
        'fields': 'screen_name',
        'v': VERSION
    }
    response = requests.get('https://api.vk.com/method/friends.get', params)
    time.sleep(0.5)
    ids_list = [u_id['id'] for u_id in response.json()['response']['items']]
    return ids_list


def get_user_groups_info(user_id):
    params = {
        'user_id': user_id,
        'access_token': TOKEN,
        'extended': '1',
        'fields': 'name',
        'v': VERSION
    }
    response = requests.get('https://api.vk.com/method/groups.get', params)
    time.sleep(0.5)
    dict_of_groups = {}
    for item in response.json()['response']['items']:
        dict_of_groups[item['id']] = item['name']
    return dict_of_groups


USER_FRIENDS = get_user_friend_ids(get_user_id('ksmolov')).copy()
USER_GROUPS = get_user_groups_info(get_user_id('ksmolov'))
pprint(USER_GROUPS)


def get_all_users_in_group(user_id, group_id):
    params = {
        'group_id': group_id,
        'user_id': user_id,
        'access_token': TOKEN,
        # 'filter': 'friends',
        'v': VERSION
    }
    response = requests.get('https://api.vk.com/method/groups.isMember', params)
    time.sleep(0.5)

    return response.json()['response']

for group in USER_GROUPS:
    for friend in USER_FRIENDS:
        pprint('{}: {}'.format(group, get_all_users_in_group(friend, group)))


# def get_user_friends_groups_info():
#     dict_of_groups_of_user_friends = {}
#     for user_id in DICT_OF_USER_FRIENDS:
#         try:
#             dict_of_groups_of_user_friends[DICT_OF_USER_FRIENDS[user_id]] = get_user_groups_info(user_id)
#         except KeyError:
#             print('Пользователь {} был заблокирован или удалил свою страницу.'
#                   .format(DICT_OF_USER_FRIENDS[user_id]))
#             continue
#         print('.')
#     return dict_of_groups_of_user_friends


# FRIENDS_GROUPS = get_user_friends_groups_info().copy()

# for friend in FRIENDS_GROUPS:
#     for group in FRIENDS_GROUPS[friend]:
#         if group in USER_GROUPS:
#             print('{} : {}'.format(friend, group))
#             del USER_GROUPS[group]
# pprint(USER_GROUPS)



# def get_friend_lists_of_user_friends():
#     dict_friends_of_user_friends = {}
#     for user_id in DICT_OF_CURRENT_USER_FRIENDS:
#         try:
#             dict_friends_of_user_friends[DICT_OF_CURRENT_USER_FRIENDS[user_id]] = (get_user_friend_list(user_id))
#         except KeyError:
#             print('Пользователь {} был заблокирован или удалил свою страницу.'
#                   .format(DICT_OF_CURRENT_USER_FRIENDS[user_id]))
#             continue
#     return dict_friends_of_user_friends
#
#
# def find_most_frequent_crossing_of_friends():
#     list_of_all_users = []
#     friends_of_user_friends = get_friend_lists_of_user_friends().copy()
#     for current_user_friend in friends_of_user_friends:
#         for friend_of_friend in friends_of_user_friends[current_user_friend]:
#             list_of_all_users.append(friends_of_user_friends[current_user_friend][friend_of_friend])
#     number_of_intersections_of_friends = Counter(list_of_all_users)
#     return number_of_intersections_of_friends
#
#
# def get_path_to_file(file_name):
#     path_to_work_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
#     return path_to_work_dir
#
#
# def create_new_folder(file_name='Results'):
#     if not os.path.isdir(get_path_to_file(file_name)):
#         os.mkdir(get_path_to_file(file_name))
#         print('\nПапка с именем "{}" создана в директории "{}"'.format(file_name, get_path_to_file('')))
#
#
# def recording_dict_to_file(input_dictionary):
#     with open('Results/crossing_friends.txt', 'w', encoding='utf-8') as f:
#         for key in input_dictionary:
#             f.write('{}: {}\n'.format(str(key), str(input_dictionary[key])))
#
#
# def dialog_window():
#     while True:
#         print('\nВведите команду из списка:\n\
#             uf - user friends (вывести список друзей пользователя программы)\n\
#             ff - friends of user friends (вывести список друзей друзей пользователя)\n\
#             cf - crossing of friends (вывести частоту пересечения общих друзей) \n\
#             q - quit (прекратить выполнение программы)')
#         command = input().lower()
#         if command == 'uf':
#             pprint(DICT_OF_CURRENT_USER_FRIENDS)
#             create_new_folder()
#             recording_dict_to_file(DICT_OF_CURRENT_USER_FRIENDS)
#         elif command == 'ff':
#             create_new_folder()
#             dict_of_friends_of_friends = get_friend_lists_of_user_friends().copy()
#             with open('Results/friends_of_friends.txt', 'w', encoding='utf-8') as f:
#                 for user_friend in dict_of_friends_of_friends:
#                     f.write('\nДрузья {}:\n\n'.format(user_friend))
#                     for friend_of_friend in dict_of_friends_of_friends[user_friend]:
#                         f.write('{}: {}\n'
#                                 .format(str(friend_of_friend),
#                                         str(dict_of_friends_of_friends[user_friend][friend_of_friend]))
#                                 )
#         elif command == 'cf':
#             create_new_folder()
#             dict_of_most_frequent_crossing = find_most_frequent_crossing_of_friends().copy()
#             pprint(dict_of_most_frequent_crossing)
#             recording_dict_to_file(dict_of_most_frequent_crossing)
#         elif command == 'q':
#             exit()
#         else:
#             print('\nВы ввели неправильную команду\n')
#
# if __name__ == '__main__':
#     dialog_window()
