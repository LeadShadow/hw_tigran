def interval_generator(x, y):
    while x <= y:
        yield x
        x += 1


five_to_ten_generator = interval_generator(5, 10)
print(five_to_ten_generator)

print(next(five_to_ten_generator))
print(next(five_to_ten_generator))
print(next(five_to_ten_generator))
print(next(five_to_ten_generator))
print(next(five_to_ten_generator))
print(next(five_to_ten_generator))


for i in range(5, 11):
    print(i)


# lambda x, y: x + y
sum_lambda = lambda x, y: x + y

numbers = [1, 2, 3, 4, 5]

for i in map(lambda x: x ** 2, numbers):
    print(i)


# lambda x: x ** 2 -> def amount(numbers):
#                         list1 = []
#                         for i in numbers:
#                              list1.append(i ** 2)
#                         return list1

# Наприклад виведемо список чисел які діляться на 2 з залишком в інтервалі від 1 до 10
for i in filter(lambda x: x % 2 == 1, range(1, 11)):
    print(i)


def odd_numbers():
    list1 = []
    for i in range(1, 11):
        if i % 2 == 1:
            list1.append(i)
        else:
            continue
    return list1


for i in odd_numbers():
    print(i)


some_str = 'aaAbbB C F DDd EEe'

for i in filter(lambda x: x.islower(), some_str):
    print(i)
