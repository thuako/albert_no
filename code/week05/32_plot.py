import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 4*np.pi, 1000)
y_sin = np.sin(x)

plt.plot(x, y)
plt.show()

# plot cosine function from 0 to 4*pi
y_cos = np.cos(x)

#plt.plot(x, y_sin, 'b', x, y_cos, 'r')
#plt.show()

# plot np.sin(i*x) for i =1, 2, ..., 10
# x = np.linspace(0, 2 * np.pi, 1000)
# for i in range(1, 11):
#     y = np.sin(i * x)
#     plt.plot(x, y)
#plt.show()