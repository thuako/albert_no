# 1. generate the list of primes from 1 to 1000
def prime_checker(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


prime_list = []
for i in range(2, 1000):
    if prime_checker(i):
        prime_list.append(i)

print(prime_list)
# 2. keep printing random number between 1 and 365 until you get the same number
# count the number of random number you printed

import random
cnt = 0
num_list = []
while True:
    x = random.randint(1, 365)
    cnt += 1
    if x in num_list:
        num_list.append(x)
        break
    else:
        num_list.append(x)

print(num_list)
print(cnt)
