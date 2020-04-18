import numpy as np

z = np.zeros(4)
print(f"z4 = {z}")

z = np.zeros([4, 1])
print(f"z41 = {z}")

z = np.zeros([1, 4])
print(f"z14 = {z}")

z = np.zeros([4, 4])
print(f"z44 = {z}")

o = np.ones([4, 3])
print(f"o43 = {o}")
