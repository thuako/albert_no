def say_hi():
    print("hi")
    print("hi!!")


print("call function")
say_hi()
print("again")
say_hi()


def print_difference(a, b):
    if a >= b:
        print(f"{a} is larger than {b}")
        print(a-b)
    else:
        print(f"{b} is larger than {a}")
        print(b-a)


print_difference(4, 7)

x = 3
y = 1
print_difference(x, y)
