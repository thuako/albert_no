def is_sorted(input_list):
    for i in range(len(input_list)):
        if input_list[i] > input_list[i+1]:
            return False
    return True


def is_sorted2(input_list):
    copy_list = input_list[:]
    copy_list.sort()
    if copy_list == input_list:
        return True
    return False


def is_sorted3(input_list):
    copy_list = input_list[:]
    copy_list.sort()
    return copy_list == input_list
