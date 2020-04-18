x = 50


def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)


func(x)
print('x is still', x)


# optional argument
def say_many(message, times=1):
    """
    :param message: message that you want to print
    :param times: number of repeats
    :return: None
    """
    for i in range(times):
        print(message)
    print("done!")


# note def say_many(times=1, message): is not valid
say_many("hello")
say_many("albert", 5)
say_many("hi", times=5)
