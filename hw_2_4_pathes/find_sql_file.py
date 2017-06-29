#-*- coding: utf-8 -*-

def input_command():
    command = input().lower()
    return command

def input_word_for_search():
    word_for_search = input().upper()
    return word_for_search

def get_list_of_sql_files():
    import os
    list_dir = [files for files in os.listdir(os.path.abspath('Migrations')) if '.sql' in files]
    return list_dir

def find_file_by_keyword(keyword, list_of_files):
    import os
    file_counter = 0
    file_list_iterations = []
    for file_name in list_of_files:
        with open(os.path.join(os.path.abspath('Migrations'),file_name), 'r') as f:
            data = f.read()
            if keyword in data:
                file_counter += 1
                file_list_iterations.append(file_name)

    return file_counter, file_list_iterations

def dialog_window():
    while True:
        print('Введите команду из списка:\n\
            e - enter a word to search and show list of found files\n\
            q - quit (прекратить выполнение программы)')

        command = input_command()
        if command == 'e':
            list_of_files = get_list_of_sql_files()
            i = True
            while i == True:
                print('Введите слово для поиска:')
                keyword = input_word_for_search()
                results = find_file_by_keyword(keyword, list_of_files)
                list_of_files = results[1]
                print('\nCлово "{}" найдено в {} следующих файлах:\n'.format(keyword, results[0]))
                for file_name in list_of_files:
                    print(file_name)
                print('\nВы хотите продолжить поиск в этом списке?(y/n)')
                yn_command = input_command()
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