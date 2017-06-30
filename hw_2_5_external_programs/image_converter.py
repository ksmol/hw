#-*- coding: utf-8 -*-

def get_image_list():
    import os
    list_of_images = [image for image in
                      os.listdir(os.path.join( os.path.dirname(__file__), 'Source'))
                      if '.jpg' in image]
    print(list_of_images)
    return list_of_images

import subprocess
subprocess.Popen('covert')