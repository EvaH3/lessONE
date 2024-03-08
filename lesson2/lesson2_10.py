import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

x = np.outer(np.linspace(-4, 4, 32), np.ones(32))
y = x.copy().T # transpose
z = (np.sin((x**2)+(y**2))/((x**2)+(y**2)))

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_surface(x, y, z, cmap='Blues', edgecolor='Grey')
ax.set_title('Поверхность  функции z(x,y)')
plt.show()
