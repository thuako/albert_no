import numpy as np
from numpy import log

from function2 import say_many

# np = numpy
x = np.exp(3)
print(x)

# log can be used without np.
y = log(x)
print(y)

say_many("my bad", times=3)
