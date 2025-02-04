# 12. Create a 2D array with 1 on the border and 0 inside (shape 5x5). 
import numpy as np
arr = np.pad(np.zeros((3,3),dtype=int),pad_width=1,mode="constant",constant_values=1)
print(arr)
