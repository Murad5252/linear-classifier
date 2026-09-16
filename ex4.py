import numpy as np

def func(x):
    return 0.1*x**2 - np.sin(x) + 0.1* np.cos(5*x) + 1

coord_x = np.arange(-5, 5.0, 0.1) # ox
coord_y = func(coord_x) #oy

sz= len(coord_x)

w= np.array([1.11, -0.26, 0.061, 0.0226, 0.00178])

a_x = w[0] + w[1]*coord_x + w[2]*(coord_x**2) + w[3]*(coord_x**3) + w[4]*(coord_x**4)

loss = (a_x-coord_y)**2
print("Q =", np.mean(loss)/sz)


