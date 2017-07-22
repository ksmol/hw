# -*-coding=utf-8-*-

import osa
import os
import chardet
import re

URL_FOR_TEMP = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'
URL_FOR_CURRENCIES = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'


def return_path_to_file(path):
    path_to_file = os.path.abspath(path)
    return path_to_file


def identify_file_encoding(file_name):
    with open(file_name, 'rb') as file:
        data = file.read()
        detected_encoding = chardet.detect(data)
        file_encoding = detected_encoding['encoding']
    return file_encoding


def read_data_file(path_to_file):
    list_with_values = []
    with open(path_to_file, 'r', encoding=identify_file_encoding(path_to_file)) as file:
        for line in file:
            line_to_list = line.split(':')
            if len(line_to_list) >= 2:
                value_to_convert = line_to_list[1].split()
                list_with_values.append(value_to_convert)
            else:
                value_to_convert = line_to_list[0].split()
                list_with_values.append(value_to_convert)
    return list_with_values


def dialog_window():
    while True:
        print('Введите команду из списка:\n\
            t - temperature (посчитать среднюю температуру)\n\
            p - path (посчитать суммарное расстояние поездки)\n\
            b - budget (посчитать суммарный бюджет поездки)\n\
            q - quit (прекратить выполнение программы)')
        command = input()

        if command == 't':
            list_of_temps = read_data_file('Homework/temps.txt')
            number_of_temps = len(list_of_temps)
            sum_temp = 0
            for value in list_of_temps:
                temp = int(value[0])
                if value[1] == 'F':
                    measure = 'degreeFahrenheit'
                elif value[1] == 'K':
                    measure = 'degreeKalvin'
                elif value[1] == 'C':
                    measure = 'degreeCelsius'
                else:
                    print('Неизвестная мера исчисления температуры')

                client_for_temp = osa.client.Client(URL_FOR_TEMP)
                response_for_temp = client_for_temp.service.ConvertTemp(Temperature=temp,
                                                                              FromUnit=measure,
                                                                              ToUnit='degreeCelsius'
                                                                              )
                sum_temp += response_for_temp
                avg_temp = round(sum_temp/number_of_temps)

            print('\nСредняя температура за 7 дней в градусах Цельсия равна {} C.\n'.format(avg_temp))

        elif command == 'p':
            list_of_paths = read_data_file('Homework/travel.txt')
            sum_path = 0
            for value in list_of_paths:
                distance = re.sub(',', '', value[0])
                t = int(distance)
                # sum_path += distance
            print(t)

        elif command == 'b':
            list_with_wasts = read_data_file('Homework/currencies.txt')
            sum_of_wasts = 0
            for wast in list_with_wasts:
                client_for_currencies = osa.client.Client(URL_FOR_CURRENCIES)
                response_for_currencies = client_for_currencies.service.ConvertToNum(toCurrency='RUB', fromCurrency=wast[1], amount=wast[0], rounding=True)
                sum_of_wasts += response_for_currencies
            print(round(sum_of_wasts))
        elif command == 'q':
            exit()
        else:
            print('\nВы ввели неправильную команду\n')


if __name__ == '__main__':
    dialog_window()
