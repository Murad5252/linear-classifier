import numpy as np

def func(x):
    return 0.5 * x ** 2 - 0.1 * (1/np.e **(-x)) + 0.5 * np.cos(2*x) - 2

def get_features(x):
    return np.array([1, x, x**2, np.cos(2*x), np.sin(2*x)])

coord_x = np.arange(-5.0, 5.0,0.1)
coord_y = func(coord_x)
sz = len(coord_x)
eta = np.array([0.01, 0.001, 0.0001, 0.01, 0.01])
w = np.array([0., 0., 0., 0., 0.])
N = 500
lm = 0.02

X = np.array([get_features(x) for x in coord_x])
Qe = np.mean(np.dot(X, w) - coord_y)**2
np.random.seed(0)

for i in range(N):
    k = np.random.randint(0, sz)
    x_k = get_features(coord_x[k])
    y_k = coord_y[k]

    error = np.dot(x_k, w) - y_k

    L_k = error**2

    Qe= lm * L_k + (1 - lm) * Qe

    grad = 2 * error * x_k

    w = w - eta * grad


Q = np.mean((np.dot(X, w) - coord_y)**2)
w = w.tolist()