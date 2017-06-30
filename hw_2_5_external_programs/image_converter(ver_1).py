#-*- coding: utf-8 -*-

import os
import subprocess

def get_path_to_work_dir():
    path_to_work_dir = os.path.abspath(os.path.dirname(__file__))
    return path_to_work_dir


def get_image_list():
    list_of_image_files = [image for image
                      in os.listdir(os.path.join(get_path_to_work_dir(), 'Source'))
                      if '.jpg' in image]
    return list_of_image_files

def create_new_folder_at_working_dir(folder_name):
    if os.path.isdir(os.path.join(get_path_to_work_dir(), folder_name)) == False:
        os.mkdir(os.path.join(get_path_to_work_dir(), folder_name))

        print('\nПапка с именем "{}" создана в директории "{}"'.format(folder_name, get_path_to_work_dir()))


def convert_all_images(source_folder, name_of_output_folder):
    create_new_folder_at_working_dir(name_of_output_folder)
    list_of_image_files = get_image_list()

    for image_file_name in list_of_image_files:
        subprocess.check_call(os.path.join(get_path_to_work_dir(), 'convert ')
                + os.path.join(get_path_to_work_dir(), source_folder, image_file_name)
                + ' -resize 200x '
                + os.path.join(get_path_to_work_dir(), name_of_output_folder, image_file_name))

    print('\nИзображения успешно конвертированы и находятся по адресу: {}'
          .format(os.path.join(get_path_to_work_dir(), name_of_output_folder)))

def dialog_window():
    source_folder = input('Введите имя папки, в которой вы хотите конвертировать изображения:\n')
    if os.path.isdir(os.path.join(get_path_to_work_dir(), source_folder)) == False:
        print('\nУказанной папки нет в рабочей директории.')
        exit(1)
    else:
        output_folder = input('\nВведите имя папки, в которую будут сохранены изображения:\n')
        convert_all_images(source_folder, output_folder)

if __name__ == '__main__':
    dialog_window()