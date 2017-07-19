# -*- coding: utf-8 -*-


def input_command():
    command = input().lower()
    return command


def input_file_name():
    file_name = input().lower()
    file_extention = '.json'
    file = file_name + file_extention
    print('Чтение файла {} ...'.format(file))
    return file


def identify_file_encoding(file_name):
    import chardet
    with open(file_name, 'rb') as file:
        data = file.read()
        detected_encoding = chardet.detect(data)
        file_encoding = detected_encoding['encoding']
    return file_encoding


def read_news_from_file(file_name):
    import json
    with open(file_name, 'r', encoding=identify_file_encoding(file_name)) as nf:
        news_file = json.load(nf)
    return news_file


def identify_ten_most_common_words(news_file):
    text_from_all_news = []
    for index, news in enumerate(news_file['rss']['channel']['items']):
        words_at_description = news_file['rss']['channel']['items'][index]['description'].split()
        words_at_title = news_file['rss']['channel']['items'][index]['title'].split()
        text_from_all_news += words_at_title + words_at_description
        text_from_all_news = [w.lower() for w in text_from_all_news if len(w) >= 6]
    dict_repetition_words = dict.fromkeys(text_from_all_news, 0)
    for word_key in text_from_all_news:
        if word_key in dict_repetition_words:
            dict_repetition_words[word_key] += 1
    sorted_list_repet_words = sorted(dict_repetition_words.items(), key=lambda item: item[1], reverse=True)
    list_of_ten_most_freq_words = []
    for i in range(10):
        list_of_ten_most_freq_words.append(sorted_list_repet_words[i])
    return list_of_ten_most_freq_words


def output_results(dict_with_results):
    for file in dict_with_results:
        print('\nВ файле {} наиболее часто встречаются следующие слова:'.format(file))
        for ind, item in enumerate(dict_with_results[file]):
            print('{}. Cлово "{}" встречается {} раз'.format(ind+1, item[0], item[1]))


def dialog_window():
    dict_with_results = {}
    while True:
        print('Введите команду из списка:\n\
            a - add file(добавить имя файла)\n\
            s - show result (вывести результат и покинуть программу)\n\
            q - quit (прекратить выполнение программы)')
        command = input_command()
        if command == 'a':
            i = True
            while i:
                print('Введите имя файла без расширения:')
                try:
                    file_name = input_file_name()
                    news_file = read_news_from_file(file_name)
                    dict_with_results[file_name] = identify_ten_most_common_words(news_file)
                    print('Хотите прочитать еще один файл(y/n)?')
                    yn_command = input_command()
                    if yn_command == 'y':
                        i = True
                    else:
                        i = False
                except FileNotFoundError:
                    i = False
        elif command == 's':
            output_results(dict_with_results)
            break
        elif command == 'q':
            exit()
        else:
            print('\nВы ввели неправильную команду\n')

if __name__ == '__main__':
    dialog_window()
