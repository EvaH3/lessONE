from scipy.integrate import odeint
import numpy as np

f0 = float(input())
dt = 0.0001
t = np.arange(0,1.1,dt)

func = lambda f, t: f+t
res = odeint(func, y0 = f0, t = t)

res2 = float(res[10001]) # 1/0.0001 + 1=10000+1=10001
res2=round(res2, 2)
print(res2)