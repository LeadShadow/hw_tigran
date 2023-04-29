def adder(value):
    def inner(x):
        return x + value
    return inner


two_adder = adder(2)
print(two_adder(3))

three_adder = adder(3)
print(three_adder(5))


print(id(100) == id(100))


def sum_func(x, y):
    return x + y


def sub_func(x, y):
    return x + y


operations = {
    '-': sub_func,
    '+': sum_func,
}


def get_handler(operator):
    return operations[operator]

