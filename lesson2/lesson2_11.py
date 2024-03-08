import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import math

R=6
r=2
fi = np.outer(np.linspace(0, (2*math.pi), 100), np.ones(100))
tet = fi.copy().T

x=((R+r*np.cos(fi))*np.cos(tet))
y=((R+r*np.sin(fi))*np.sin(tet))
z=(r*np.sin(fi))

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_surface(x, y, z)
plt.axis('auto')
plt.show()