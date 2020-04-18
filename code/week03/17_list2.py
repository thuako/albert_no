chr_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(chr_list[1])
print(chr_list[::2])
print(chr_list[::-1])

del chr_list[1]
print(chr_list)

big_list = [chr_list, 1, 'albert']
print(big_list)
print(big_list[0])
print(big_list[0][1])

big_list[1] = 0
print(big_list)
