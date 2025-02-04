# 14. Normalize a random 5x5 matrix (rescale values between 0 and 1)
import numpy as np
arr = np.random.randn(5,5)
print(arr)
print("\n")
arr_max = arr.max()
arr_min = arr.min()
rescale_array = (arr-arr_min)/(arr_max-arr_min)
print(rescale_array)