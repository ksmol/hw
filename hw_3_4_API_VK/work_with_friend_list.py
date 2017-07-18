# coding=utf-8
import os
from pprint import pprint
import requests
from urllib.parse import urlencode

def return_path_to_file(file_name):
    path_to_work_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
    return path_to_work_dir

def create_new_folder(folder_name):
    if not os.path.isdir(return_path_to_file(folder_name)):
        os.mkdir(return_path_to_file(folder_name))
        print('\nПапка с именем "{}" создана в директории "{}"'.format(folder_name, return_path_to_file('')))

AUTHORIZE_URL = 'https://oauth.vk.com/authorize'
APP_ID = 6117192
VERSION = '5.67'


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

TOKEN = input('\nПожалуйста, выполните следующие действия:\n\
              1. Перейдите по ссылке;\n\
              2. Разрешите доступ приложению;\n\
              3. Скопируйте Ваш ТОКЕН;\n\
              4. Введите Ваш ТОКЕН ниже:\n')

params = {
    'access_token': TOKEN,
    'order': 'name',
    'fields': 'nickname',
    'v': VERSION
}

response = requests.get('https://api.vk.com/method/friends.get', params)
response_list = response.json()
friends_id_list = []
for index, item in enumerate(response_list['response']['items']):
    friends_id_list.append(item['id'])

friends_of_friends = []
for id in friends_id_list:
    new_params = {
        'access_token': TOKEN,
        'user_id': id,
        'order': 'name',
        'fields': 'nickname',
        'v': VERSION
    }
    new_response = requests.get('https://api.vk.com/method/friends.get', new_params)
    friends_of_friends.append(new_response.json())

pprint(friends_of_friends)


# output_folder = input('\nВведите имя папки, в которую будут сохранены изображения:\n')
# create_new_folder(output_folder)
# with open(os.path.join(return_path_to_file(output_folder), __file__), 'w', encoding='utf-8') as f:
#     f.write(friend_list)
