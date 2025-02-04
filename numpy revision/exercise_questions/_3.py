# 3.  Create a NumPy array of shape (3,3) filled with True values
import numpy as np
bool_arr = np.ones((3,3),dtype = bool)
print(bool_arr)
bool_arr = np.zeros((3,3),dtype = bool)
print(bool_arr)
bool_arr = np.full((3,3),True)
print(bool_arr)