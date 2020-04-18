import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 4 * np.pi, 100)
y = np.sin(x)
z = np.cos(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'b-.', label='sin')
ax.plot(x, z, 'go', label='cos')
ax.legend(loc='upper right')
# increase the font of xlabel and add ylabel
plt.xlabel('x', fontsize=20)

plt.title('sin and cos')
plt.show()