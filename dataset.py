#
# dataset reader
#

import pickle

data = pickle.load(open("dataset.pickle", "rb"))

if __name__ == "__main__":
    access_roi = data['Canon1DsMkIII_0001.PNG']['ROI']
    access_polys = data['Canon1DsMkIII_0001.PNG']['polys']
    #access_coords = data['Canon1DsMkIII_0001.PNG']['coords']