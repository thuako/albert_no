import numpy as np


def polar(a, b):
    r_ = np.sqrt(a * a + b * b)
    theta_ = np.arctan2(b, a)

    return [r_, theta_]


def polar_np(a, b):
    z = a + b * 1j
    r_ = np.abs(z)
    theta_ = np.angle(z)
    return [r_, theta_]


[r, theta] = polar(1, -2)
print('r = {}, theta = {}'.format(r, theta))

[r, theta] = polar_np(1, -2)
print('r = {}, theta = {}'.format(r, theta))
