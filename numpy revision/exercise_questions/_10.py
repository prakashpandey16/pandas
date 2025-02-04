# 10. Create a 10x10 array with random values and find the minimum & maximum. 
import numpy as np
arr = np.random.randint(0,101,(10,10))
print(arr)
print(arr.max())
print(arr.min())
max_ele = -(2**31-1)
min_ele = 2**31-1
for i  in range(len(arr)):
    for j in range(len(arr[0])):
        if(arr[i][j]>max_ele):
            max_ele = arr[i][j]
        if(arr[i][j]<min_ele):
            min_ele = arr[i][j]
print(max_ele)
print(min_ele)