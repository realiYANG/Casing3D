import lasio
from sys import stdout

import numpy as np
import pandas as pd


# las = lasio.read("ning209H13-4_resampled_3200-4000.las")
# print(las.keys())

npzfile = np.load("78-11-14.npz")
print(npzfile.files)
print(npzfile['casingdata'])

np.savetxt(".\\npz-inspect\\mfc.txt", npzfile['mfc'])
np.savetxt(".\\npz-inspect\\mtdSpline.txt", npzfile['mtdSpline'])
np.savetxt(".\\npz-inspect\\mfcSpline.txt", npzfile['mfcSpline'])
np.savetxt(".\\npz-inspect\\depth.txt", npzfile['depth'])
np.savetxt(".\\npz-inspect\\casingdata.txt", npzfile['casingdata'])
np.savetxt(".\\npz-inspect\\mtd.txt", npzfile['mtd'])