import time
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 - 5*x + 5

def df(x):
    return 2*x - 5

N = 20
xx= 0
lmd = 0.1

x_plt = np.arange(0,5,0.1)
f_plt = [f(x) for x in x_plt]

plt.ion()
fig, ax = plt.subplots()
ax.grid(True)

ax.plot(x_plt, f_plt)
point = ax.scatter(xx,f(xx), color='red')

for i in range(N):
    xx = xx - lmd * df(xx)
    point.set_offsets([xx, f(xx)])

    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.02)

plt.ioff()
print(xx)
ax.scatter(xx,f(xx), color='blue')
plt.show()
