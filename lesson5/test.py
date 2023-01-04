x = 50


def func():
    x = 2
    print('Заміна глобального х на', x)


func()
print('x досі', x)


def func2():
    global x
    print('x ==', x)
    x = 2
    print('Заміна глобального х на', x)


func2()
print('Значення х ==', x)
