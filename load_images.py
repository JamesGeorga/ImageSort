'''
Given a folder directory, this function returns a set of pillow images.
'''

import os


def load_images(folder):

    supported_types = (".png", ".jpg", ".JPEG")
    images = []

    for file in os.listdir(folder):
        # check file is a supported image file
        if file.lower().endswith(supported_types):
            path = os.path.join(folder, file)
            images.append(path)

    return images