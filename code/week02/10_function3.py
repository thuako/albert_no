def addition(x, y):
    """
    :param x: input argument
    :param y: input argument
    :return: return sum of two input arguments
    """
    return x+y


a = 1
b = 3
s = addition(a, b)
print(s)
print(addition(9, 2))


def minimum(x, y):
    """
    :return: return the minimum of two input arguments
    """
    if x <= y:
        return x
    else:
        return y


c = minimum(a, b)
print(c)
print(minimum(11, 5))
