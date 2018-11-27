#
# preprocessing images with checkers
#

import os
import pickle
import numpy as np

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
PNG_PROCESSED_DIR = os.path.join(CURRENT_DIR, "PNG_PROCESSED")
CHECKER_DIR = os.path.join(CURRENT_DIR, "CHECKER")

i, n = 0, -1
BREAK_ONERROR = True

dataset_csv = open('dataset.csv', 'w')

print("building dataset.")
dataset = {}
for image_filename in sorted(os.listdir(PNG_PROCESSED_DIR)):
    if not image_filename.endswith(".PNG"):
        print(f"Error: '{image_filename}' is not an image!")
        if BREAK_ONERROR:
            break

    if n < 0 or i < n:
        i += 1
    else:
        break

    try:
        # output dictionary
        checkerfilename = image_filename.replace(".PNG", "_mask.txt")
        checker_csv = np.genfromtxt(os.path.join("CHECKER", checkerfilename), delimiter=',')
        ROI = checker_csv[0]
        coords = checker_csv[1:]
        polys = []
        for i in range(0, coords.shape[0], 2):
            xm = coords[i] + ROI[0]
            ym = coords[i + 1] + ROI[1]
            polys.append(np.array([xm, ym]).T)

        imgdata = { "ROI": ROI, "polys": polys } #, "coords": coords }
        dataset[image_filename] = imgdata

        # output csv
        for i in range(len(polys)):
            p = polys[i]
            x1 = min(p[0][0], p[3][0]) # min(x1, x4)
            y1 = min(p[0][1], p[1][1]) # min(y1, y2)
            x2 = max(p[2][0], p[1][0]) # max(x3, x2)
            y2 = max(p[2][1], p[3][1]) # max(y3, y4)
            #width = x2 - x1
            #height = y2 - y1
            dataset_csv.write(f"{os.path.join('PNG_PROCESSED', image_filename)},{x1},{y1},{x2},{y2},{i}\n")

    except Exception as err:
        print("Exception: {0}".format(err))
        if BREAK_ONERROR:
            break

print("dumping dataset.")
pickle.dump(dataset, open("dataset.pickle", "wb"))
print("done!")
