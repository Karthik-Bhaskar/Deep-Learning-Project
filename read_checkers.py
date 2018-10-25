#
# read checker files
#

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches

image_name = "Canon1DsMkIII_0022";
csv = pd.read_csv(f"CHECKER\\{image_name}_mask.txt", header=None)
ROI = csv.iloc[0]

fig, axs = plt.subplots(1)

img = plt.imread(f"PNG_PROCESSED\\{image_name}.png")
axs.imshow(img)

rect = patches.Rectangle((ROI[0], ROI[1]), ROI[2], ROI[3],
                        linewidth=1, edgecolor='r', facecolor='none')
axs.add_patch(rect)

l1 = csv.iloc[1]
rect1 = patches.Rectangle((l1[0] + ROI[0], l1[1] + ROI[1]), l1[2], l1[3],
                        linewidth=1, edgecolor='g', facecolor='none')
axs.add_patch(rect1)

#l2 = csv.iloc[2]
#rect2 = patches.Rectangle((l2[0] + ROI[0], l2[1] + ROI[1]), l2[2], l2[3],
#                        linewidth=1, edgecolor='g', facecolor='none')
#ax1.add_patch(rect2)

plt.show()