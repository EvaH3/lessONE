import numpy as np

def nonzero(A):
    column = np.sum(A, axis=0)
    row = np.sum(A, axis=1)
    for i in range (len(column)):
        if (column[i]!=0): y = i
    for j in range(len(row)):
        if (row[j] != 0): x = j
    return x, y

A = np.zeros((100,100))
A[56,70] = 1

print(nonzero(A))