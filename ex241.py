import numpy as np

def func(x):
    return -0.5 * x + 0.2 * x ** 2 - 0.01 * x ** 3 - 0.3 * np.sin(4*x)
def dfunc(x):
    return -0.5 + 0.4 * x - 0.03 * x ** 2 - 1.2 * np.cos(4*x)

N=200
x= -3.5
eta=0.1
gamma=0.8
v=0

for _ in range(N):
    v = gamma*v+ (1-gamma)*eta*dfunc(x)
    x= x - v
