import numpy as np
import matplotlib.pyplot as plt

def euler_system(f, t0, tf, Y0, h):
    t_values = [t0]
    Y_values = [Y0]
    t = t0
    Y = np.array(Y0, dtype=float)
    
    while t < tf:
        Y = Y + h * np.array(f(t, Y))
        t += h
        t_values.append(t)
        Y_values.append(Y.copy())
    
    return np.array(t_values), np.array(Y_values)
