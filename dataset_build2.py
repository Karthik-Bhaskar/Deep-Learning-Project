#
# preprocessing images with checkers
#

import os
import pickle
import numpy as np
from PIL import Image

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
PNG_PROCESSED_DIR = os.path.join(CURRENT_DIR, "TEST")
CHECKER_DIR = os.path.join(CURRENT_DIR, "CHECKER2")
MARK_DIR = os.path.join(CURRENT_DIR, "MARK2")

i, n = 0, -1
ONLY_PROCESSED = True
BREAK_ONERROR = True

mark_csv = open('dataset2.csv', 'w')

print("building dataset.")
dataset = {}
for checkerfilename in sorted(os.listdir(CHECKER_DIR)):
    if not checkerfilename.endswith("_mask.txt"):
        # ignore not mask files
        continue

    if n < 0 or i < n:
        i += 1
    else:
        break

    image_filename = checkerfilename.replace("_mask.txt", ".PNG")
    if not os.path.isfile(os.path.join(PNG_PROCESSED_DIR, image_filename)) and ONLY_PROCESSED:
        continue

    try:
        # output dictionary
        checker_csv = np.genfromtxt(os.path.join(CHECKER_DIR, checkerfilename), delimiter=',')
        ROI = checker_csv[0]
        coords = checker_csv[1:]
        polys = []
        for i in range(0, coords.shape[0], 2):
            xm = coords[i] + ROI[0]
            ym = coords[i + 1] + ROI[1]
            polys.append(np.array([xm, ym]).T)

        imgdata = { "ROI": ROI, "polys": polys } #, "coords": coords }
        dataset[image_filename] = imgdata

        # mark txt file per image
        mark_filename = image_filename.replace(".PNG", ".txt")
        image_size = Image.open(os.path.join(PNG_PROCESSED_DIR, image_filename)).size
        mark_csv = open(os.path.join(MARK_DIR, mark_filename), 'w')

        # output csv
        for i in range(len(polys)):
            p = polys[i]
            x1 = min(p[0][0], p[3][0]) # min(x1, x4)
            y1 = min(p[0][1], p[1][1]) # min(y1, y2)
            x2 = max(p[2][0], p[1][0]) # max(x3, x2)
            y2 = max(p[2][1], p[3][1]) # max(y3, y4)
            x_center = (x1 + x2) / 2
            y_center = (y1 + y2) / 2
            width = x2 - x1
            height = y2 - y1
            x_center /= image_size[0]
            y_center /= image_size[1]
            width /= image_size[0]
            height /= image_size[1]
            mark_csv.write(f"{i} {x_center} {y_center} {width} {height}\n")
            #dataset_csv.write(f"{os.path.join('PNG_PROCESSED', image_filename)},{x1},{y1},{x2},{y2},{i}\n")

    except Exception as err:
        print("Exception: {0}".format(err))
        if BREAK_ONERROR:
            break

print("dumping dataset.")
pickle.dump(dataset, open("dataset.pickle", "wb"))
print("done!")
