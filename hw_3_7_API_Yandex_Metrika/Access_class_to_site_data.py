# coding=utf-8

from urllib.parse import urlencode, urljoin
import requests
from pprint import pprint


class YandexMetrikaGetToken:
    AUTHORIZE_URL = 'https://oauth.yandex.ru/authorize'

    def print_url_to_get_token(self, app_id='1d2e25a83d9d41dbbeb217c18d20d1ee'):
        auth_data = {
            'response_type': 'token',
            'client_id': app_id
        }
        return '?'.join((self.AUTHORIZE_URL, urlencode(auth_data)))


class YandexMetrikaKeyURLs:
    MANAGEMENT_URL = 'https://api-metrika.yandex.ru/management/v1/'
    STAT_URL = 'https://api-metrika.yandex.ru/stat/v1/data'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        headers = {
            'Authorization': 'OAuth {}'.format(self.token),
            'Content-Type': 'application / x - yametrika + json'
        }
        return headers


class YandexMetrikaCountersIds(YandexMetrikaKeyURLs):
    def get_ymetrika_counters(self):
        counters_url = urljoin(self.MANAGEMENT_URL, 'counters')
        response = requests.get(counters_url, headers=self.get_headers(), params={'pretty': 1})
        counters_dict = response.json()['counters']
        counters_ids_list = [YandexMetrikaData(self.token, counter_data['id']) for counter_data in counters_dict]
        return counters_ids_list


class YandexMetrikaData(YandexMetrikaKeyURLs):
    visits = 'ym:s:visits'
    views = 'ym:s:pageviews'
    users = 'ym:s:users'

    def __init__(self, token, counter_id):
        self.id = counter_id
        super().__init__(token)

    def get_metrics(self, metrics, period):
        params = {
            'group': period,
            'id': self.id,
            'metrics': metrics
        }
        response = requests.get(self.STAT_URL, params, headers=self.get_headers())
        return response.json()


def get_metrics_data(token, metrics_attribute, period='Week'):
    yametrika = YandexMetrikaCountersIds(token)
    counters = yametrika.get_ymetrika_counters()
    for counter in counters:
        pprint(counter.get_metrics(metrics_attribute, period))


def dialog_window():
    print('\n{}'.format(YandexMetrikaGetToken().print_url_to_get_token()))
    token = input('\nПожалуйста, выполните следующие действия:\n'
                  '1. Перейдите по ссылке выше;\n'
                  '2. Разрешите доступ приложению;\n'
                  '3. Скопируйте Ваш ТОКЕН;\n'
                  '4. Введите Ваш ТОКЕН ниже:\n')
    while True:
        print('\nВведите команду из списка:\n\
            vst - visitors (вывести информацию по визитам на страницу)\n\
            vws - views (вывести информацию о просмотрах страницы)\n\
            usr - users (вывести информацию о посетителях страницы) \n\
            q - quit (прекратить выполнение программы)')

        command = input().lower()

        if command == 'vst':
            get_metrics_data(token, YandexMetrikaData.visits)
        elif command == 'vws':
            get_metrics_data(token, YandexMetrikaData.views)
        elif command == 'usr':
            get_metrics_data(token, YandexMetrikaData.users)
        elif command == 'q':
            exit()
        else:
            print('\nВы ввели неправильную команду\n')


if __name__ == '__main__':
    dialog_window()
