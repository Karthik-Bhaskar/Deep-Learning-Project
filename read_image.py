import matplotlib.pyplot as plt
import numpy as np
import os


def read_image(image_path):
    # We read the image
    try:
        image = plt.imread(image_path)
    except OSError as err:
        print("Error: "+str(err))
        return None

    # We take the maximum pixel value of each filter
    max = np.max(image, axis=0)
    max = np.max(max, axis=0, keepdims=True)
    max = np.tile(max, (image.shape[0], image.shape[1], 1))

    # We take the minimum pixel value of each filter
    min = np.min(image, axis=0)
    min = np.min(min, axis=0, keepdims=True)
    min = np.tile(min, (image.shape[0], image.shape[1], 1))

    # and we do a min-max normalization
    image = ((image - min) / (max-min))**(1/2.2)

    return image
