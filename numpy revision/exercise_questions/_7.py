# 7.  Find indices of non-zero elements in the array [1,2,0,0,4,0]. 
import numpy as np
arr = np.array([1,2,0,0,4,0])
for i in range(len(arr)):
    if(arr[i]>0):
        print(i)