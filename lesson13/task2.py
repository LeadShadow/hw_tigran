# Приклад 2
# """ Створіть файл nums.txt, що містить кілька чисел, записаних через пропуск.
# Напишіть програму, яка підраховує і виводить на екран загальну суму чисел, що
# зберігаються в цьому файлі.

from random import randint


def num_input():
    f = open('nums.txt', 'w')
    for i in range(7):
        i = str(randint(0, 10)) + ' '
        f.write(i)
    f.close()


def sum_nums():
    result = 0
    with open('nums.txt', 'r') as fh:
        f = fh.read().strip().split(' ')
        for i in f:
            result = result + int(i)
    return result


num_input()
print(sum_nums())
