# 13. Create a 8x8 checkerboard pattern (0 and 1 alternate).
import numpy as np
check_board = np.tile([[1,0],[0,1]],(4,4))
print(check_board)