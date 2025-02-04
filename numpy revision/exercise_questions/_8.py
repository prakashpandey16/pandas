# 8.  Create a 3x3 identity matrix (I). 
import numpy as np
identity_matrix = np.eye(3,dtype=int)
print(identity_matrix)

identity_matrix = np.identity(3,dtype=int)
print(identity_matrix)

identity_matrix = np.diag([1,1,1])
print(identity_matrix)