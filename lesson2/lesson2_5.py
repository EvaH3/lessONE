import numpy as np
I = np.eye(2) #задаем квадратную матрицу 2х2 c единичными диагональными элементами
A = np.array([[0, 1], [1, 0]])
x = np.sum(np.dot(A, I))
y = np.sum(A * I)
print(x, y)