import random


def birthday():
    cnt = 0
    num_list = []
    while True:
        x = random.randint(1, 365)
        cnt += 1
        if x in num_list:
            num_list.append(x)
            return cnt
        else:
            num_list.append(x)


num_sample = 10000
cnt_sum = 0
for idx in range(num_sample):
    cnt_out = birthday()
    cnt_sum += cnt_out

cnt_avg = cnt_sum / num_sample

print(cnt_avg)