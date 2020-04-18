# 1. print 1^2, 2^2, ..., 9^2, 10^2, 9^3, 8^3, ..., 1^3
for i in range(1, 20):
    if i <= 10:
        print(i*i)
    else:
        print((20-i)**3)

# 2. find the smallest positive integer x>=2 such that 2^x > x^10
x = 2
while 2**x <= x**10:
    x = x+1
    print(x, 2**x, x**10)
