import numpy as np

A = np.array([3,2,5,4,1,7], dtype=np.int64)
for i in range (3):
    a=np.min(A)
    coord = np.where(A == a)[0][0]
    print(coord)
    A = np.delete(A,coord)
