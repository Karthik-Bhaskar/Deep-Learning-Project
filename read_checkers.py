#
# read checker files
#

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches

image_name = "Canon1DsMkIII_0001"
csv = np.genfromtxt(os.path.join("CHECKER", f"{image_name}_mask.txt"), delimiter=',')
ROI = csv[0]
coords = csv[1:]

fig, axs = plt.subplots(1)

img = plt.imread(os.path.join("PNG_PROCESSED", f"{image_name}.PNG"))
axs.imshow(img)

rect = patches.Rectangle((ROI[0], ROI[1]), ROI[2], ROI[3],
                         linewidth=1, edgecolor='r', facecolor='none')
axs.add_patch(rect)

for i in range(0, coords.shape[0], 2):
    xm = coords[i] + ROI[0]
    ym = coords[i + 1] + ROI[1]
    poly = patches.Polygon(np.array([xm, ym]).T)
    axs.add_patch(poly)

plt.show()
