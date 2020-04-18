name = 'albert'

print(name)
print(name[0])
print(name[:3])
#name[0] = 'c'
print(name)

last_name = 'no'
full_name = name + ' ' + last_name
print(full_name)

for idx in name:
    print(idx)

big_list = [4, 1, [1, 2, 3]]
for idx in big_list:
    print(idx)

print(list(range(2, 10)))

num_list = [4, 1, 8, 5]
num_list.sort()
print(num_list)
