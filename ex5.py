import numpy as np

def f(x):
    return 0.5*x**2 - 0.1/np.exp(-x) + (0.5*np.cos(2*x))-2

coord_x = np.arange(-5, 5.0, 0.1) # ox
coord_y = f(coord_x) #oy

sz= len(coord_x)

w= np.array([-1.59, -0.69, 0.278,0.497,-0.106])
a_x = w[0] + w[1]*(coord_x) + w[2]*(coord_x**2) + w[3]*(np.cos(coord_x*2)) + w[4]*(np.sin(coord_x*2))
loss = np.abs((a_x-coord_y))
Q = np.mean(loss)/sz
print(Q)
