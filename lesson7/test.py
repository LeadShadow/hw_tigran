# впорядкованність, змінність, унікальність

my_list = list()
my_list1 = []
print(my_list)
print(my_list1)
print(my_list == my_list1)

list1 = [1, 2, 'user']
print(list1)
iterable = ['a', 'b', 'c']
first_letter = iterable[0]
second_letter = iterable[1]
third_letter = iterable[2]
print(first_letter, second_letter, third_letter)

first_letter = iterable[-3]
second_letter = iterable[-2]
third_letter = iterable[-1]
print(first_letter, second_letter, third_letter)
iterable[0] = 'd'
print(iterable)

some_str = 'This is awesome string'
first_five = some_str[0:5]
print(first_five)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = numbers[::2]
even_numbers = numbers[1::2]
three_numbers = numbers[2::3]
print(odd_numbers)
print(even_numbers)
print(three_numbers)

numbers_copy = numbers[:]
print(numbers_copy)
print(numbers_copy == numbers)

# append
chars = ['a', 'b']
chars.append('c')
print(chars)

# clear
num = [1, 2, 2]
num.clear()
print(num)

# remove
chars.remove('c')
print(chars)

# pop, chars = ['a', 'b']
last = chars.pop()
print(chars)
print(last)
chars.append('b')

# extend
numbers = [1, 2]
chars.extend(numbers)  # ['a', 'b', 1, 2]
print(chars)

# insert
chars = ['a', 'b']
chars.insert(1, 'c')
print(chars)

# index
chars = ['a', 'b', 'c', 'd']
c_ind = chars.index('c')
print(c_ind)

# count
chars = ['a', 'b', 'c', 'a']
a_count = chars.count('a')
print(a_count)

# sort
chars = ['x', 'a', 'b']
chars.sort(reverse=True)
print(chars)

# reverse
chars = ['a', 'b', 'x']
chars.reverse()
print(chars)

# copy
chars = ['a', 'b']
chars_copy = chars.copy()
print(chars_copy == chars)
