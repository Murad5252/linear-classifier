import numpy as np

def batch_gradient_descent(X, y, lr=0.01 , epochs = 100):
    n_samples,n_features = X.shape
    w= np.zeros(n_features)

    for i in range(epochs):
        y_pred = np.dot(X,w)

        gradient = (1/n_samples) * np.dot(X.T,(y_pred - y))

        w = w - lr * gradient
    return w
