import numpy
import random

x = numpy.exp(3)
print(x)

y = numpy.log(x)
print(y)

while True:
    x = random.randint(1, 10)
    print(x)
    if x == 7:
        break
