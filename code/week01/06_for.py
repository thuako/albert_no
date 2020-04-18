for i in range(1, 5):
    print(i)

for i in range(3, 9, 2):
    print(i)

for i in range(3):
    for j in range(1, 4):
        print(i, j)

for i in range(10):
    print(i)
    if i > 4:
        break
    print('keep running')
