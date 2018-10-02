#
# process png images
#

import os
import cv2
import numpy as np

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
PNG_DIR = os.path.join(CURRENT_DIR, "PNG")
PNG_PROCESSED_DIR = os.path.join(CURRENT_DIR, "PNG_PROCESSED")

GAMMA = 2.2
RGB_RANGE = 255.0

for filename in os.listdir(PNG_DIR):
    if filename.lower().endswith(".png"):
        try:
            filepath = os.path.join(PNG_DIR, filename)
            image = cv2.imread(filepath)
            
            # apply inverse gamma correction
            image = image / RGB_RANGE
            image = image ** (1.0/GAMMA)
            image = image * RGB_RANGE

            # apply inverse gamma correction
            #table = np.array([((i / RGB_RANGE) ** (1.0/GAMMA)) * 255 
            #    for i in np.arange(0, 256)]).astype("uint8")
            #image = cv2.LUT(image, table)

            filepath = os.path.join(PNG_PROCESSED_DIR, filename)
            cv2.imwrite(filepath, image)
        except Exception as err:
            print("processing '{0}' Exception:\n'{1}'".format(filename, err))
