import numpy as np


def powering(a, n):
    powered = 1
    for i in range(n):
        powered = powered * a
    return powered


def powering_rec(a, n):
    if n == 1:
        return a
    else:
        return a * powering_rec(a, n-1)


k = 16
print(powering(2, k))
print(powering_rec(2, k))
print(2 ** k)
print(np.power(2, k))
