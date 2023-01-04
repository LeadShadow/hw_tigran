def func(a, b=5, c=10):
    print(f'a == {a}, b == {b}, c == {c}')


func(3, 7, 7)
func(25, c=24)
func(c=50, b=20, a=10)


def say(message, times=1):
    print((message + ' ') * times)


say('Кукуріку', 5)


def func(a, b=5):
    pass


def total(a=5, *numbers, **phone_numbers):
    print(f'a == {a}')
    for item in numbers:
        print(f'item == {item}')

    for part1, part2 in phone_numbers.items():
        print(part1, part2)


total(10, 1, 2, 3, 4, 5, 6, Tom=1500, Sasha=1000, Misha=2000)


a = {
    'name': 'Sasha',
    'age': 18,
    'pet': 'cat'
}
