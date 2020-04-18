def is_square(n):
    for i in range(n+1):
        if i*i == n:
            return True
    return False


def count_square(num_list):
    cnt = 0
    for num in num_list:
        if is_square(num):
            cnt += 1
    return cnt


print(count_square([1, 4, 3]))
