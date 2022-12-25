def say_hello():
    print('Привіт, світ!')


s = say_hello
s()


def print_max(a, b):  # -> a, b -> параметри
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, '==', b)
    else:
        print(b, 'максимально')


print_max(3, 4)  # пряма передача значень у функцію
x = 5
y = 7
print_max(x, y)  # непряма передача значень(перадача зміннихх в якості аргументів)


def plus(a, b):
    return a + b


print(plus(3, 4))

