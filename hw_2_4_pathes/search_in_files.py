#-*- coding: utf-8 -*-

import os

def return_path_to_file(file_name):
    path_to_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
    return path_to_file

def get_list_of_all_sql_files_at_dir():
    list_of_all_sql_files = [file for file in os.listdir(return_path_to_file('Migrations'))
                             if file.endswith('.sql')]
    return list_of_all_sql_files

def find_file_by_keyword(keyword, list_of_all_sql_files):
    list_of_found_files = []
    for file_name in list_of_all_sql_files:
        with open(os.path.join(return_path_to_file('Migrations'), file_name), 'r') as f:
            data = f.read()
            if keyword in data:
                list_of_found_files.append(file_name)
    return len(list_of_found_files), list_of_found_files

def dialog_window():
    while True:
        print('Введите команду из списка:\n\
            e - enter (ввод строки, по которой будет осуществлен поиск)\n\
            q - quit (прекратить выполнение программы)')
        command = input().lower()
        if command == 'e':
            list_of_files = get_list_of_all_sql_files_at_dir()
            main_state = True
            while main_state:
                print('Введите слово для поиска:')
                keyword = input().upper()
                results = find_file_by_keyword(keyword, list_of_files)
                list_of_files = results[1]
                print('\nСтрока "{}" найдена в {} следующих файлах:\n'.format(keyword, results[0]))
                if list_of_files:
                    print('\n'.join(list_of_files))
                print('\nВы хотите продолжить поиск в этом списке?(y/n)')
                yn_command = input()
                if yn_command == 'y':
                     continue
                else:
                    main_state = False
                    print('\nПосле ввода команды "e" вы сможете начать поиск по файлам заново.\n')
        elif command == 'q':
            exit()
        else:
            print('\nВы ввели неправильную команду.\n')


if __name__ == '__main__':
    dialog_window()