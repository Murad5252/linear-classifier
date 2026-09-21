import numpy as np


def func(x):
    return 0.1 * x ** 2 - np.sin(x) + 5.


coord_x = np.arange(-5.0, 5.0, 0.1)
coord_y = func(coord_x)

sz = len(coord_x)
eta = np.array([0.1, 0.01, 0.001, 0.0001])
w = np.array([0., 0., 0., 0.])
N_epochs = 200
S = np.vstack([np.ones(sz), coord_x, coord_x ** 2, coord_x ** 3]).T

G = np.zeros((sz, 4))

g_avg = np.zeros(4)

for epoch in range(N_epochs):

    for _ in range(sz):
        i = np.random.randint(0, sz)

        x_i = S[i]
        y_i = coord_y[i]

        a_i = x_i @ w
        error_i = a_i - y_i

        g_new = 2 * error_i * x_i

        g_avg = g_avg - (G[i] / sz) + (g_new / sz)

        G[i] = g_new

        w = w - eta * g_avg

a = S @ w
Q = np.sum((a - coord_y) ** 2) / sz
w = list(w)

print("Финальные веса:", w)
print("MSE ошибка (Q):", Q)