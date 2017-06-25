#-*- coding: utf-8 -*-

def input_file_name():
    file_name = input('Введите имя файла')
    file_extention = '.json'
    file = file_name + file_extention
    print(file)
    return file

def identify_and_decode_file_encoding(file_name)
    file_name = input_file_name()
    import chardet

def read_cook_book_from_file():
    from pprint import pprint
    import  json
    with open(input_file_name(), 'r', encoding='utf-8') as cb:
     cook_book = json.load(cb)
    pprint(cook_book)
    return cook_book

read_cook_book_from_file()