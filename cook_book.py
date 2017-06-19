#-*- coding: utf-8 -*-

def read_cook_book_from_file():
    cook_book = {}
    with open('recipes.txt', 'r', encoding='utf-8') as cb:
        cb.readline()
        for line in cb:
            dish_name = line.strip().lower()
            number_of_ingredient = int(cb.readline())
            ingredients_for_dish = []
            for i in range(number_of_ingredient):
                ingred = cb.readline()
                ingred_list = ingred.split()
                for k, item in enumerate(ingred_list):
                    if item == '|':
                        ingred_list.pop(k)
                ingredients_for_dish.append({'ingridient_name' : ingred_list[0].lower(), 'quontity' : int(ingred_list[1]),\
                                             'measure' : ingred_list[2].lower()})
                cook_book[dish_name] = ingredients_for_dish

            cb.readline()
    return cook_book

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