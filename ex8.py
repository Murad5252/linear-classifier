import numpy as np


def func(x):
    return 0.1 * x ** 2 - np.sin(x) + 5.


coord_x = np.arange(-5.0, 5.0, 0.1)
coord_y = func(coord_x)
sz = len(coord_x)

eta = np.array([0.1, 0.01, 0.001, 0.0001])
w = np.array([0., 0., 0., 0.])
N = 200


S = np.vstack([np.ones(sz), coord_x, coord_x ** 2, coord_x ** 3]).T


for i in range(N):

    a = S @ w

    error = a - coord_y


    grad = (2 / sz) * (S.T @ error)

    w = w - eta * grad


a = S @ w
Q = np.sum((a - coord_y) ** 2) / sz


w = list(w)