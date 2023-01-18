# pop(key) -> повертає значення елемента і видалє пару ключ-значення з словника
chars = {
    'a': 1,
    'b': 2,
    'c': 3
}
b_num = chars.pop('b')
print(chars)
print(b_num)

# update(another_dict) -> розширює словник значеннями з іншого словника
chars.update({'b': 2})
print(chars)

# clear() -> очищує словник не створюючи нового
chars.clear()
print(chars)

# copy() -> повертає копію словника
chars = {
    'a': 1,
    'b': 2,
    'c': 3
}
chars_copy = chars.copy()
print(chars_copy == chars)

# get(key[, default]) -> не викликає помилку якшо ключа немає в словнику

c_1 = chars.get('d', 1)
print(c_1)

people = {
    'name': 'Oleksandr'
}

for k, v in people.items():
    print(f"It's human and he has {k} - {v}")


# set ----------
# {1, 2, 3, 5, 7, 8, 10, 10}
a = set('hello')
print(a)


# add -> додає елемент в множину
numbers = {1, 2, 3}
numbers.add(4)
print(numbers)

# remove -> видаляє елемент з множини і викликає помилку якшо такого елементу немає
numbers.remove(3)
print(numbers)

# discard -> видаляє елемент з множини і не викликає помилку якшо такого елементу немає
numbers.discard(10)
print(numbers)

# tuple
points = {
    (0, 0): 'O',
    (1, 1): 'A',
    (2, 2): 'B'
}

