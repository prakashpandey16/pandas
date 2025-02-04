# 5.  Reverse a NumPy array (first element becomes last).
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr)
reversed_arr = arr[::-1]
print(reversed_arr)
reversed_arr = np.flip(arr)
print(reversed_arr)