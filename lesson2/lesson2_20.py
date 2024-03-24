import numpy as np
import warnings
from scipy.optimize import minimize

warnings.filterwarnings('ignore')
def get_path(xc):
    global path
    path.append(xc)


a = float(0)
b = float(0)

dx = 0.001
x = np.arange(-1, 1, dx)
dy = 0.001
y = np.arange(-1, 1, dy)

def f(x,y,a,b):
    return ((x+y)**2 - 2*x*(y+a) - 2*y*b + a + b)

path = [0, 0]
result = minimize(f(x,y,a,b), np.ndarray(shape=(2,2), x0=0, y0=0), callback=get_path)
x1 = result.x
get_path(x1)
print(result)