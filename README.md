# linear-classifier
import numpy as np

w = np.array([15/7, -9/7, -1])
x_test = np.array([(1, -8, -4), (1, -2, 2), (1, 4, 8), (1, 6, 3)])
y_test = np.array([1, 1, -1, -1]) 

margin = (y_test * (x_test @ w)).tolist()
