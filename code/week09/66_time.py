import numpy as np
import time


for i in range(5):
    print(i)
    #time.sleep(0.5)

n_array = np.arange(0, 100, 0.001)
start = time.time()
s = 0
for n in n_array:
    s += n
print(s)
end = time.time()
print(end-start)

start = time.time()
print(n_array.sum())
end = time.time()
print(end-start)