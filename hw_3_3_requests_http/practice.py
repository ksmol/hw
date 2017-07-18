# coding=utf-8

import os
import requests
import time


def return_path_to_file(file_name):
    path_to_work_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
    return path_to_work_dir


def create_new_folder(folder_name):
    if not os.path.isdir(return_path_to_file(folder_name)):
        os.mkdir(return_path_to_file(folder_name))
        print('\nПапка с именем "{}" создана в директории "{}"'.format(folder_name, return_path_to_file('')))


def identify_file_encoding(file_name):
    import chardet
    with open(file_name, 'rb') as file:
        data = file.read()
        detected_encoding = chardet.detect(data)
        file_encoding = detected_encoding['encoding']
    return file_encoding


def open_file(file_name):
    with open(return_path_to_file(file_name), 'r', encoding=identify_file_encoding(file_name)) as f:
        text = f.read()
    return text


def translate_it(text, in_language='en', out_language='ru'):
    """
        YANDEX translation plugin
        docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/
        https://translate.yandex.net/api/v1.5/tr.json/translate ?
        key=<API-ключ>
            & text=<переводимый текст>
            & lang=<направление перевода>
            & [format=<формат текста>]
            & [options=<опции перевода>]
            & [callback=<имя callback-функции>]
        :param text: <str> text for translation.
        :param in_language: <str> the language from which we translate,
        :param out_language: <str> language to which we translate.
        :return: <str> translated text.
       """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    params = dict(key=key, lang=str(in_language) + "-" + str(out_language), text=text)
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))


def dialog_window():
    file_name = input('Введите имя файла, который хотите перевести:\n')
    in_language = input('Введите язык, с которого будет осуществен перевод, например:\n\
    en - для перевода с английского языка\n\
    de - для перевода с немецкого языка\n\
    es - для перевода с испанского языка\n\
    fr - для перевода с французского языка\n')

    if not os.path.isfile(return_path_to_file(file_name)):
        print('\nУказанного файла нет в рабочей директории.')
        exit(1)
    else:
        out_language = input('Введте язык, на который хотите перевести текст\n'
                             '(нажмите Enter, чтобы по умолчанию перевести на русский язык)\n')
        if out_language == '':
            out_language = 'ru'
        output_folder = input('\nВведите имя папки, в которую будут сохранены изображения:\n')
        clc = time.time()
        create_new_folder(output_folder)
        with open(os.path.join(return_path_to_file(output_folder), file_name), 'w', encoding='utf-8') as f:
            f.write(translate_it(open_file(return_path_to_file(file_name)), in_language, out_language))
        clc = time.time() - clc
        print("\nВремя  выполнения программы составило {0:.2f} секунд".format(clc))


if __name__ == '__main__':
    dialog_window()
