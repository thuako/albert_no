# 1. find the second largest number in the list of numbers
def second_largest(num_list):
    copy_list = num_list[:]
    copy_list.sort()
    return copy_list[-2]

print(second_largest([1, 4, 2, 3]))

# 2. define mutate_string(message, idx, new_chr)
# mutate_string("abcd", 0, "e") should be "ebcd"
# mutate_string("abcd", 2, "a") should be "abad"
def mutate_string(message, idx, new_chr):
    out_str = message[:idx] + new_chr + message[idx+1:]
    return out_str

print(mutate_string("abcd", 0, "e"))
# 3. generate a dictionary where the keys are integers from 2 to 100
# and the value is the largest divisor except itself


def largest_divisor(num):
    for idx in range(num-1, 0, -1):
        if num % idx == 0:
            return idx


largest_dict = {}

for n in range(2, 1001):
    largest_dict[n] = largest_divisor(n)

print(largest_dict)