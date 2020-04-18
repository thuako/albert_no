import numpy as np
### 1. invert the matrix A using numpy library

A = np.array([[1, 2], [3, 4]])


### 2. def function that takes binary numpy array as an input and returns the longest consecutive 1's
def count_longest(bin_array):
    cnt = 0
    longest_run = 0
    for bit in bin_array:
        if bit == 1:
            cnt += 1
            if longest_run < cnt:
                longest_run = cnt
        else:
            cnt = 0
    return longest_run


bin_arr = np.array([1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1])
cnt_out = count_longest(bin_arr) # is 4
print(cnt_out)

n = np.power(10, 6)
binarray = np.random.randint(0, 2, n)
print(len(binarray))
print(count_longest(binarray))