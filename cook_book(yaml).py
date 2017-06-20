#-*- coding: utf-8 -*-

def read_cook_book_from_file():
    import  yaml
    from pprint import pprint
    with open('cook_book.yml', 'r', encoding='utf-8') as cb:
     cook_book = yaml.load(cb)
    return cook_book
read_cook_book_from_file()

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_cook_book_from_file()
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item['quontity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quontity'] += new_shop_list_item['quontity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{ingridient_name} {quontity} {measure}'.format(**shop_list_item))

def create_shop_list():
    dishes = input('Введите блюдо в расчете на одного человека:').lower().split(', ')
    person_count = int(input('Введите количество человек:'))
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)

create_shop_list()