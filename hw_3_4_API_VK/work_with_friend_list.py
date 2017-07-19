# coding=utf-8

from pprint import pprint
import requests
from urllib.parse import urlencode
from collections import Counter

AUTHORIZE_URL = 'https://oauth.vk.com/authorize'
APP_ID = 6117192
VERSION = '5.67'


def print_url_to_authorize():
    auth_data = {
        'client_id': APP_ID,
        'redirect_url': 'https://oauth.vk.com/blank.html',
        'display': 'mobile',
        'scope': 'friends',
        'response_type': 'token',
        'v': VERSION
    }
    print('?'.join(
        (AUTHORIZE_URL, urlencode(auth_data))
    ))


print_url_to_authorize()

TOKEN = input('\nПожалуйста, выполните следующие действия:\n\
              1. Перейдите по ссылке;\n\
              2. Разрешите доступ приложению;\n\
              3. Скопируйте Ваш ТОКЕН;\n\
              4. Введите Ваш ТОКЕН ниже:\n')


def get_user_id():
    params = {
        'access_token': TOKEN,
        'v': VERSION
    }
    response = requests.get('https://api.vk.com/method/users.get', params)
    return response.json()['response'][0]['id']

CURRENT_USER_ID = get_user_id()


def get_user_friend_list(user_id):
    params = {
        'access_token': TOKEN,
        'user_id': user_id,
        'order': 'name',
        'fields': 'nickname',
        'v': VERSION
    }
    response = requests.get('https://api.vk.com/method/friends.get', params)
    dict_of_friends = {}
    for item in response.json()['response']['items']:
        dict_of_friends[item['id']] = ' '.join([item['first_name'], item['last_name']])
    return dict_of_friends


DICT_OF_CURRENT_USER_FRIENDS = get_user_friend_list(CURRENT_USER_ID)


def get_friend_lists_of_user_friends():
    dict_friends_of_user_friends = {}
    for user_id in DICT_OF_CURRENT_USER_FRIENDS:
        try:
            dict_friends_of_user_friends[DICT_OF_CURRENT_USER_FRIENDS[user_id]] = (get_user_friend_list(user_id))
        except KeyError:
            print('Пользователь {} был заблокирован или удалил свою страницу.'
                  .format(DICT_OF_CURRENT_USER_FRIENDS[user_id]))
            continue
    return dict_friends_of_user_friends


def find_most_frequent_crossing_of_friends():
    list_of_all_users = []
    friends_of_user_friends = get_friend_lists_of_user_friends()
    for current_user_friend in friends_of_user_friends:
        for friend_of_friend in friends_of_user_friends[current_user_friend]:
            list_of_all_users.append(friends_of_user_friends[current_user_friend][friend_of_friend])
    number_of_intersections_of_friends = Counter(list_of_all_users)
    return number_of_intersections_of_friends


def dialog_window():
    while True:
        print('\nВведите команду из списка:\n\
            uf - user friends (вывести список друзей пользователя программы)\n\
            ff - friends of user friends (вывести список друзей друзей пользователя)\n\
            cf - crossing of friends (вывести частоту пересечения общих друзей) \n\
            q - quit (прекратить выполнение программы)')
        command = input()
        if command == 'uf':
            pprint(DICT_OF_CURRENT_USER_FRIENDS)
        elif command == 'ff':
            pprint(get_friend_lists_of_user_friends())
        elif command == 'cf':
            pprint(find_most_frequent_crossing_of_friends())
        elif command == 'q':
            exit()
        else:
            print('\nВы ввели неправильную команду\n')

if __name__ == '__main__':
    dialog_window()
