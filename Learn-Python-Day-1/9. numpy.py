import numpy as np

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

np_kg = np.array(weight_kg)
np_lbs = np_kg*2.2

print(np_lbs)