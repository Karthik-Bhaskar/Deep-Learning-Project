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
        checkerfilename = image_filename.replace(".PNG", "_mask.txt")
        csv = np.genfromtxt(os.path.join("CHECKER", checkerfilename), delimiter=',')
        ROI = csv[0]
        coords = csv[1:]
        polys = []
        for i in range(0, coords.shape[0], 2):
            xm = coords[i] + ROI[0]
            ym = coords[i + 1] + ROI[1]
            polys.append(np.array([xm, ym]).T)

        imgdata = { "ROI": ROI, "polys": polys } #, "coords": coords }
        dataset[image_filename] = imgdata

    except Exception as err:
        print("Exception: {0}".format(err))
        if BREAK_ONERROR:
            break

print("dumping dataset.")
pickle.dump(dataset, open("dataset.pickle", "wb"))
print("done!")
