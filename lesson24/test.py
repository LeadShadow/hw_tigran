# Функція як об'єкт першого класу
def func(x, y):
    return x + y


test = func
print(test(10, 20))


def sum_func(x, y):
    return x + y


def sub_func(x, y):
    return x - y


def test_func(x, y, func):
    return func(x, y)


dict1 = {'+': sum_func, '-': sub_func}


def get_operator(operator):
    return dict1[operator]
    # if operator == '+':
    #     return sum_func
    # elif operator == '-':
    #     return sub_func
    # elif operator == '*':
    #     return sub_func
    # elif operator == '/':
    #     return sub_func


result = test_func(2, 3, sum_func)
result = test_func(2, 3, sub_func)

action = get_operator('+')
print(action(10, 20))

SOME_VAR = 3


def func(x):
    global SOME_VAR
    SOME_VAR = x
    print(SOME_VAR)


def procedure():
    print(SOME_VAR)


procedure()
func(5)
print(SOME_VAR)


GLOBAL_SCOPE_VAR = 1


def func():
    enclosed_scope_var = 2
    def inner():
        inner_var = 3


