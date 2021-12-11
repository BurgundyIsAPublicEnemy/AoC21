import numpy as np
from skimage import data, filters, color, morphology
from skimage.segmentation import flood, flood_fill
from random import *


f = open("Day9.txt", "r")
lines = f.readlines()

uniqueC = []
N = len(lines[0]) - 1
M = len(lines)

zeros = [ [-1] * N for _ in range(M)]
 
# Create matrix
for r in range(0, len(lines)):
    for c in range (0, len(lines[r].strip())):
        if (int(lines[r][c].strip()) == 9):
            zeros[r][c] = 100
        else:
            zeros[r][c] = int(lines[r][c].strip())

a = np.array(zeros)

for r in range(0, 1000):
    for c in range (0, 1000):
        try:
            if (a[r][c] != 100):
                m = (randint(200, 10000)) 
                while(True):
                    if (m not in uniqueC):
                        uniqueC.append(m)
                        break
                    m = (randint(200, 10000)) 
                
                a = flood_fill(a, (r,c), m, connectivity=1, tolerance=9)
        except:
            pass

b = a.flatten()
b = np.delete(b, np.where(b == 100))

unique, frequency = np.unique(b, 
                              return_counts = True)

frequency = sorted(frequency, reverse=True)
print(frequency[0] * frequency[1] * frequency[2])