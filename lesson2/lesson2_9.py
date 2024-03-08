import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(2, 8, 140)
y=np.linspace(0, 5, 140)
func=(0.25*np.sin((0.5*(x**2))-y)-np.exp(-(((x-5)**2)+((y-2)**2))))

plt.grid(lw=0.5, ls='--')
X, Y = np.meshgrid(x,y)
print("X:", X)
print("Y:", Y)
plt.plot(x, func, lw = 1.5, color='blue')
plt.show()
