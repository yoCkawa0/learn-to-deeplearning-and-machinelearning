import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A.shape)
print(B.shape)
print(np.dot(A, B))

C = np.array([[1, 2, 3], [4, 5, 6]])
print(C.shape)
D = np.array([[1, 2], [3, 4], [5, 6]])
print(D.shape)
print(np.dot(C, D))

X = np.array([1, 2])
print(X.shape)

W = np.array([[1, 3, 5], [2, 4, 6]])
print(W.shape)
print(W)

Y = np.dot(X, W)
print(Y)
