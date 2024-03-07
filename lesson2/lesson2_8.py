import numpy as np

r = 2.5
v = 1
vecs = np.array( [ [1.0, 0.0, 2.0],
                   [-1.0, 0.5, 2.0],
                   [-2.0, 1.5, 0.0],
                   [2.5, -1.2, -0.5],
                   [1.5, 0.2, -0.2]])

def closest(vecs, v, r):
    count=0
    for i in range (len(vecs)):
        dist = np.linalg.norm(vecs[i],2)
        if dist<r: count+=1
    return (count-1) #так как проверяем расстояние до атома, который является выбранным изначально

print(closest(vecs, v, r)) # Вернет 2
