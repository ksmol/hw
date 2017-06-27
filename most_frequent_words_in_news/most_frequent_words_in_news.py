#-*- coding: utf-8 -*-

def input_command():
    command = input('Введите команду из списка:\n\
    a - add file(добавить имя файла)\n\
    s - show result (вывести результат и покинуть программу)\n\
    q - quit (прекратить выполнение функции)\n')
    return command

def input_file_name():
    file_name = input('\nВведите имя файла(без расширения):\n').lower()
    file_extention = '.json'
    file = file_name + file_extention
    print('Чтение файла {} ...\n'.format(file))
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
    text_from_all_news = [w.lower() for w in text_from_all_news if len(w)>=6]
    from collections import Counter
    dict_repetition_words = Counter(text_from_all_news)
    dict_of_ten_most_freq_words = {}
    for i in range(10):
        most_frequent_word = max(dict_repetition_words, key=lambda word: dict_repetition_words[word])
        dict_of_ten_most_freq_words[most_frequent_word] = dict_repetition_words[most_frequent_word]
        dict_repetition_words.pop(most_frequent_word)
    return dict_of_ten_most_freq_words

def output_results(dict_of_resuls):
    for file in dict_of_resuls:
        print('\nВ файле {} наиболее часто встречаются следующие слова:'.format(file))
        for word in dict_of_resuls[file]:
            print('Cлово "{}" встречается {} раз'.format(word, dict_of_resuls[file][word]))

def dialog_window():
    dict_of_results = {}
    while True:
        command = input_command()
        if command == 'a':
            file_name = input_file_name()
            news_file = read_news_from_file(file_name)
            dict_of_results[file_name] = identify_ten_most_common_words(news_file)
        elif command == 's':
            output_results(dict_of_results)
            break
        elif command == 'q':
            exit()
        else:
            print('\nВы ввели неправильную команду\n')
            True

if __name__ == '__main__':
    dialog_window()