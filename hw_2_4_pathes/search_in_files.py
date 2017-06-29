#-*- coding: utf-8 -*-

def enter_data():
    data = input()
    return data

def get_list_of_all_sql_files_at_dir():
    import os
    list_of_all_sql_files = [files for files in
                             os.listdir(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Migrations'))
                             if '.sql' in files]
    return list_of_all_sql_files

def find_file_by_keyword(keyword, list_of_all_sql_files):
    import os
    file_counter = 0
    list_of_found_files = []
    for file_name in list_of_all_sql_files:
        with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Migrations', file_name), 'r') as f:
            data = f.read()
            if keyword in data:
                file_counter += 1
                list_of_found_files.append(file_name)

    return file_counter, list_of_found_files

def dialog_window():
    while True:
        print('Введите команду из списка:\n\
            e - enter (ввод строки, по которой будет осуществлен поиск)\n\
            q - quit (прекратить выполнение программы)')
        command = enter_data().lower()
        if command == 'e':
            list_of_files = get_list_of_all_sql_files_at_dir()
            i = True
            while i == True:
                print('Введите слово для поиска:')
                keyword = enter_data().upper()
                results = find_file_by_keyword(keyword, list_of_files)
                list_of_files = results[1]
                print('\nСтрока "{}" найдена в {} следующих файлах:\n'.format(keyword, results[0]))
                for file_name in list_of_files:
                    print(file_name)
                print('\nВы хотите продолжить поиск в этом списке?(y/n)')
                yn_command = enter_data()
                if yn_command == 'y':
                    i = True
                else:
                    i = False
                    print('\nПосле ввода команды "e" вы сможете начать поиск по файлам заново.\n')
        elif command == 'q':
            exit()
        else:
            print('\nВы ввели неправильную команду\n')


if __name__ == '__main__':
    dialog_window()