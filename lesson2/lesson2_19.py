import numpy as np
import warnings
from scipy.optimize import minimize

warnings.filterwarnings('ignore')
def get_path(xc):
    global path
    path.append(xc)

dx = 0.001
x = np.arange(-4, 4, dx)
f = lambda x: -(x**2 * ( x - 4 )**2 * np.exp(-x**2)) #для поиска максимума с помощью ф-ции минимума перевернум функцию

x0 = float(input())
path = [x0]
result = minimize(f, x0=x0, tol=1e-2, callback=get_path)
x1 = result.x
get_path(x1)
print(result)