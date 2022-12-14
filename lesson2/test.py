x = int(input('X: '))
y = int(input('Y: '))

if x == 0:
    print("X can't be equal to zero")
    x = int(input('X: '))

    if x == 0:
        print("X can't be equal to zero")
        x = int(input('X: '))

        if x == 0:
            print("X can't be equal to zero")
            x = int(input('X: '))

            if x == 0:
                print("X can't be equal to zero")
                x = int(input('X: '))

                if x == 0:
                    print("X can't be equal to zero")
                    x = int(input('X: '))

result = y / x
print(result)

fruit = 'apple'
for i in fruit:
    print(i)
print('apple')

a = 1
while a <= 5:
    print(a)
    a = a + 1


a = 0
while True:
    print(a)
    if a >= 20:
        break
    a += 1


while True:
    user_input = input('Введіть слово exit - щоб вийти: ')
    print(user_input)
    if user_input == 'exit':
        break


a = 0
while a < 6:
    a += 1
    if a % 2 == 1:
        continue
    else:
        print(a)


while True:
    number = input('number == (exit that leave): ')
    if number == 'exit':
        break
    else:
        number = int(number)
    while True:
        print(number)
        number -= 1
        if number < 0:
            break
