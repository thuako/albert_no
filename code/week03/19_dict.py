alph_list = ['apple', 'banana', 'carrot']
print(alph_list[1])

alph_dict = {'a': 'apple',
             'b': 'banana',
             'c': 'carrot', # check this last comma
}
print(alph_dict['b'])

for key in alph_dict:
    print("key  = ", key)
    print("value = ", alph_dict[key])
    print(" ")

num_dict = {3: 1,
            5: 2}

print(num_dict[5])
del num_dict[3]
print(num_dict)
