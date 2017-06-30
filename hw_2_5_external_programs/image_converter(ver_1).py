#-*- coding: utf-8 -*-

def get_image_list():
    import os
    list_of_image_files = [image for image
                      in os.listdir(os.path.join( os.path.dirname(__file__), 'Source'))
                      if '.jpg' in image]
    return list_of_image_files

def create_new_folder_at_working_dir(folder_name):
    import os
    if os.path.isdir(os.path.join(os.path.abspath(os.path.dirname(__file__)), folder_name)) == False:
        os.mkdir(os.path.join(os.path.abspath(os.path.dirname(__file__)), folder_name))

        print('\nПапка с именем "{}" создана в директории "{}"'
                .format(folder_name, os.path.abspath(os.path.dirname(__file__))))


def convert_all_images(source_folder, name_of_output_folder):
    import subprocess
    import os
    create_new_folder_at_working_dir(name_of_output_folder)
    list_of_image_files = get_image_list()
    for i, image_file_name in enumerate(list_of_image_files):
        subprocess.check_call(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'convert ')
                + os.path.join(os.path.abspath(os.path.dirname(__file__)), source_folder, image_file_name)
                + ' -resize 200x '
                + os.path.join(os.path.abspath(os.path.dirname(__file__)), name_of_output_folder, image_file_name))
    print('\nИзображения успешно конвертированы и находятся по адресу: {}'
                .format(os.path.join(os.path.abspath(os.path.dirname(__file__)), name_of_output_folder)))

def dialog_window():
    import os
    source_folder = input('Введите имя папки, в которой вы хотите конвертировать изображения:\n')
    if os.path.isdir(os.path.join(os.path.abspath(os.path.dirname(__file__)), source_folder)) == False:
        print('\nУказанной папки нет в рабочей директории.')
        exit(1)
    else:
        output_folder = input('\nВведите имя папки, в которую будут сохранены изображения:\n')
        convert_all_images(source_folder, output_folder)

if __name__ == '__main__':
    dialog_window()