import numpy as np

a = np.arange(10, 30, 5)
print(f"a = {a}")

a = np.arange(10, 31, 5)
print(f"a = {a}")

a = np.arange(10, 15, 0.5)
print(f"a = {a}")

x = np.linspace(0, 2*np.pi, 100)
f = np.sin(x)

print(x)
print(f)