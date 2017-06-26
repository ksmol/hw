#-*- coding: utf-8 -*-

def input_file_name():
    file_name = input('Введите имя файла(без расширения):\n')
    file_extention = '.json'
    file = file_name + file_extention
    print('Чтение файла {} ... .'.format(file))
    return file

def identify_and_decode_file_encoding(file_name):
    import chardet
    with open(file_name, 'rb') as file:
        data = file.read()
        detected_encoding = chardet.detect(data)
        file_encoding = detected_encoding['encoding']
        print(detected_encoding)
    return file_encoding

def read_news_from_file():
    file_name = input_file_name()
    import json
    with open(file_name, 'r', encoding=identify_and_decode_file_encoding(file_name)) as nf:
       news_file = json.load(nf)
    return news_file


news_file = read_news_from_file()
text_from_all_news = []
for news_index, item in enumerate(news_file['rss']['channel']['items']):
    words = news_file['rss']['channel']['items'][news_index]['description'].split()
    text_from_all_news += words
text_from_all_news = [w.lower() for w in text_from_all_news if len(w)>=5]
text_from_all_news.sort()
maybe_most_frequent_word = text_from_all_news[0]
counter = 0
for word in text_from_all_news:
    if word == maybe_most_frequent_word:
        counter +=1
print(counter)



print(text_from_all_news)