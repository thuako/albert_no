a = 2
b = a
b = 1
print(a)


num_list = [2, 3, 5, 7]
copy_list = num_list
copy_list[0] = 1
print(num_list)


num_list = [2, 3, 5, 7]
copy_list = num_list[:]
copy_list[0] = 1
print(num_list)

num_list = [2, 3, 5, 7]
copy_list = num_list.copy()
copy_list[0] = 1
print(num_list)
