def prime_checker(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


check_seven = prime_checker(7)
check_twelve = prime_checker(12)
print(check_seven)
print(check_twelve)
print(prime_checker(121541))
