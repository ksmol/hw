#-*- coding: utf-8 -*-

import os
import subprocess
import time

def get_path_to_file(file_name):
    path_to_work_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
    return path_to_work_dir


def get_image_list(source_folder):
    list_of_image_files = [image for image in os.listdir(get_path_to_file(source_folder)) if '.jpg' in image]
    return list_of_image_files

def create_new_folder(file_name):
    if os.path.isdir(get_path_to_file(file_name)) == False:
        os.mkdir(get_path_to_file(file_name))
        print('\nПапка с именем "{}" создана в директории "{}"'.format(file_name, get_path_to_file('')))


def convert_all_images(source_folder, output_folder):
    create_new_folder(output_folder)
    list_of_image_files = get_image_list(source_folder)
    for image_file_name in list_of_image_files:
        subprocess.check_call(get_path_to_file('convert ')
                              + os.path.join(get_path_to_file(source_folder), image_file_name)
                              + ' -resize 200x '
                              + os.path.join(get_path_to_file(output_folder), image_file_name))
    print('\nИзображения успешно конвертированы и находятся по адресу: {}'.format(get_path_to_file(output_folder)))

def dialog_window():
    source_folder = input('Введите имя папки, в которой вы хотите конвертировать изображения:\n')
    if os.path.isdir(get_path_to_file(source_folder)) == False:
        print('\nУказанной папки нет в рабочей директории.')
        exit(1)
    else:
        output_folder = input('\nВведите имя папки, в которую будут сохранены изображения:\n')
        clc = time.time()
        convert_all_images(source_folder, output_folder)
        clc = time.time() - clc
        print("\nВремя  выполнения программы составило {0:.2f} секунд".format(clc))

if __name__ == '__main__':
    dialog_window()