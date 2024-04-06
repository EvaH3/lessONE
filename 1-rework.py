import numpy as np
import warnings
from scipy import optimize

warnings.filterwarnings('ignore')

a = float(input())
b = float(input())

def f(coords):
    x, y = coords
    return ((x + y) ** 2 - 2 * x * (y + a) - 2 * y * b + a + b)

x0=float(0)
y0=float(0)

result = optimize.minimize(f, x0=(0,0))

x1 = result.x
print(x1)
