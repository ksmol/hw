#-*- coding: utf-8 -*-

import os
import subprocess

def get_path_to_folder(folder_name):
    path_to_work_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), folder_name)
    return path_to_work_dir


def get_image_list(source_folder):
    list_of_image_files = [image for image in os.listdir(get_path_to_folder(source_folder)) if '.jpg' in image]
    return list_of_image_files

def create_new_folder(folder_name):
    if os.path.isdir(get_path_to_folder(folder_name)) == False:
        os.mkdir(get_path_to_folder(folder_name))
        print('\nПапка с именем "{}" создана в директории "{}"'.format(folder_name, get_path_to_folder('')))


def convert_all_images(source_folder, output_folder):
    create_new_folder(output_folder)
    list_of_image_files = get_image_list(source_folder)
    for image_file_name in list_of_image_files:
        subprocess.check_call(get_path_to_folder('convert ')
                              + os.path.join(get_path_to_folder(source_folder), image_file_name)
                              + ' -resize 200x '
                              + os.path.join(get_path_to_folder(output_folder), image_file_name))
    print('\nИзображения успешно конвертированы и находятся по адресу: {}'.format(get_path_to_folder(output_folder)))

def dialog_window():
    source_folder = input('Введите имя папки, в которой вы хотите конвертировать изображения:\n')
    if os.path.isdir(get_path_to_folder(source_folder)) == False:
        print('\nУказанной папки нет в рабочей директории.')
        exit(1)
    else:
        output_folder = input('\nВведите имя папки, в которую будут сохранены изображения:\n')
        convert_all_images(source_folder, output_folder)

if __name__ == '__main__':
    dialog_window()