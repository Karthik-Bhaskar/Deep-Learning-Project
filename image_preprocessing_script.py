import cv2
import pandas as pd
import numpy as np
import os

def reading_the_images(directory_path,new_processed_directory,gamma_coorection=2.2):
    for filename in os.listdir(directory_path):
        if filename.endswith('.PNG'):

            absolute_path = os.path.join(directory_path, filename)
            processed_image=process_image(absolute_path)

            # TODO save processed image


def process_image(image_path):
    image = cv2.imread(image_path)
    image[x,y]
