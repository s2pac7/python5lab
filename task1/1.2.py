import numpy as np

X = np.ones((12, 3), dtype = int)
X[:, 1] = np.random.randint(25, 37, 12)
X[:, 2] = np.random.randint(60, 82, 12)

Y = np.random.uniform(13.5, 18.6, (12, 1))

print(X)
print()
print(Y)

print()
A = np.linalg.inv(X.T @ X) @ (X.T @ Y) # A = (np.linalg.inv((X.T).dot(X))).dot(((X.T).dot(Y)))
print("А:")
print(A)

check_Y = X @ A

print()

print("Равны ли изначальные значения Y с Y(регр.)\nY:")
print(Y)
print("Y(регр.):")
print(check_Y)

