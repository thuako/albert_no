def n_cube(n):
    n_cubic = n*n*n
    return n_cubic


def print_n_cube(n):
    n_cubic = n*n*n
    print(n_cubic)


print(n_cube(3))
print_n_cube(3)
print(print_n_cube(3))

cube_sum = 0
for idx in range(10):
    cube_sum += n_cube(idx)

cube_sum = 0
for idx in range(10):
    cube_sum += print_n_cube(idx)

