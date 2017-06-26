#-*- coding: utf-8 -*-

def input_file_name():
    file_name = input('Введите имя файла(без расширения):\n').lower()
    file_extention = '.json'
    file = file_name + file_extention
    print('Чтение файла {} ...'.format(file))
    return file

def identify_and_decode_file_encoding(file_name):
    import chardet
    with open(file_name, 'rb') as file:
        data = file.read()
        detected_encoding = chardet.detect(data)
        file_encoding = detected_encoding['encoding']
    return file_encoding

def read_news_from_file():
    file_name = input_file_name()
    import json
    with open(file_name, 'r', encoding=identify_and_decode_file_encoding(file_name)) as nf:
       news_file = json.load(nf)
    return news_file


def output_most_frequent_word():
    news_file = read_news_from_file()
    text_from_all_news = []
    for news_index, item in enumerate(news_file['rss']['channel']['items']):
        words_at_description = news_file['rss']['channel']['items'][news_index]['description'].split()
        words_at_title = news_file['rss']['channel']['items'][news_index]['title'].split()
        text_from_all_news += words_at_title + words_at_description
    text_from_all_news = [w.lower() for w in text_from_all_news if len(w)>=6]
    from collections import Counter
    dict_repetition_words = Counter(text_from_all_news)
    dict_of_most_freq_words = {}
    for i in range(10):
        most_frequent_word = max(dict_repetition_words, key=lambda word: dict_repetition_words[word])
        dict_of_most_freq_words[most_frequent_word] = dict_repetition_words[most_frequent_word]
        dict_repetition_words.pop(most_frequent_word)
    # number_of_occurences = dict_repetition_words[most_frequent_word]
    print(dict_of_most_freq_words)


output_most_frequent_word()