a = 5
while a > 0:
    print(a)
    a = a-1
print('while loop ended')

b = 5
while True:
    b = b-1
    if b > 0:
        print('b is larger than zero')
        continue
    else:
        print('b<=0')
        print('closing loop')
        break
print(b)
