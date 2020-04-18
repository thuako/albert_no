import numpy as np

a = np.array([1, 2, -1, -4])

b = np.array([[1, 2, 3, -1], [0, 2, 3, 0.3]])

print(f"a = {a}")
print(f"b = {b}")
print(f"b.T = {b.T}")
print(f"b*a = {b*a}")
print(f"b.dot(a) = {b.dot(a)}")

print(f"size of a = {a.size}")
print(f"shape of a = {a.shape}")
print(f"size of b = {b.size}")
print(f"shape of b = {b.shape}")