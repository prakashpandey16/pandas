# 9.  Create a 3x3x3 array with random values.
import numpy as np
arr_3d = np.random.randint(0,28,(3,3,3))
print(arr_3d)
arr_3d = np.random.random((3,3,3))
print(arr_3d)
print("\n")
arr_3d = np.random.randn(3,3,3)
print(arr_3d)