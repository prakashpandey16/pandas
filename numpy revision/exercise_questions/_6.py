# 6.  Create a 3x3 matrix with values ranging from 0 to 8
import numpy as np
arr = np.arange(0,9)
matrix = arr.reshape((3,3))
print(matrix)
matrix_arr = np.arange(0,9).reshape((3,3))
print(matrix_arr)