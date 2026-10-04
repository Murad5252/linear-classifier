import numpy as np

def f(x):
    return 0.4 * x + 0.1 * np.sin(2*x) + 0.2 * np.cos(x*3)

def df(x):
    return 0.4 + 0.2 * np.cos(2*x) - 0.6 * np.sin(x*3)
eta= 1.0
x= 4.0
N= 500
gamma = 0.7
v= 0


for _ in range(N):
    x_lookahead = x - gamma * v
    v = gamma * v + (1 - gamma) * eta * df(x_lookahead)
    x = x-v
