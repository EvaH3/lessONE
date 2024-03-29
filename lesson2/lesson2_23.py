import numpy as np
import matplotlib.pyplot as plt

t = 6

vmax = 10
dv = 0.0001
v = np.arange(1, vmax, dv)

func = np.sin((v*np.cos(2*np.pi*t)))

signal = np.fft.fft(func)
freqs = np.fft.fftfreq(t)

print(max(abs(freqs)))