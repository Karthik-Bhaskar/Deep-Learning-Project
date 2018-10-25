#
# process png images
#

import os
import cv2

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
PNG_DIR = os.path.join(CURRENT_DIR, "PNG")
PNG_PROCESSED_DIR = os.path.join(CURRENT_DIR, "PNG_PROCESSED")
if not os.path.exists(PNG_PROCESSED_DIR): os.mkdir(PNG_PROCESSED_DIR)

GAMMA, RGB_RANGE = 2.2, 4095.0
i, n = 0, 10
force_process = True

for filename in sorted(os.listdir(PNG_DIR)):
    if filename.lower().endswith(".png"):
        if n < 0 or i < n:
            i += 1
        else:
            break

        if os.path.isfile(os.path.join(PNG_PROCESSED_DIR, filename)) and not force_process:
            continue

        try:
            print("processing '{0}'".format(filename))
            filepath = os.path.join(PNG_DIR, filename)
            image = cv2.imread(filepath, cv2.IMREAD_UNCHANGED)

#            maxrgb = image.max(axis=0).max(axis=0)
#            minrgb = image.min(axis=0).min(axis=0)
#            RGB_RANGE = (maxrgb - minrgb)

            # apply inverse gamma correction
            image = image / RGB_RANGE
            image = image ** (1.0/GAMMA)
            image = image * 255.0

            filepath = os.path.join(PNG_PROCESSED_DIR, filename)
            cv2.imwrite(filepath, image)
        except Exception as err:
            print("Exception: {0}".format(err))
